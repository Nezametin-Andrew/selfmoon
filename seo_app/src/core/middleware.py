from datetime import timedelta

from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

from .models import AnonymousUser, IpAddress
from .utils import generate_unique_sesid
from ..account.models import Account


class AnonymousUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        sesid = request.COOKIES.get('sesid')
        ip_address = request.META.get('REMOTE_ADDR', None)

        if ip_address is None or ip_address == '':
            ip_address = request.META.get('HTTP_X_REAL_IP', None)
        if ip_address is None or ip_address == '':
            ip_address = request.META.get('HTTP_X_FORWARDED_FOR', None)
        if ip_address is None or ip_address == '':
            return request
        user = None

        end_date = timezone.now()
        start_date = end_date - timedelta(days=60)
        if sesid:
            try:
                user = AnonymousUser.objects.get(sesid=sesid)
            except AnonymousUser.DoesNotExist as e:
                account = Account.objects.create()
                user = AnonymousUser.objects.create(sesid=sesid, account=account)
                IpAddress.objects.create(ip=ip_address, user=user)
        else:
            ip_exists = IpAddress.objects.filter(ip=ip_address, created_at__range=(start_date, end_date)).exists()
            if ip_exists:
                user = IpAddress.objects.get(ip=ip_address).user
            else:
                account = Account.objects.create()
                user = AnonymousUser.objects.create(sesid=generate_unique_sesid(), account=account)
                IpAddress.objects.create(ip=ip_address, user=user)
        request.anonymous_user = user

    def process_response(self, request, response):
        if not request.COOKIES.get('sesid'):
            response.set_cookie('sesid', request.anonymous_user.sesid, expires=None)
        return response
