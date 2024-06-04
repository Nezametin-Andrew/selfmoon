from .models import AnonymousUser


class AnonymousUserMixin:
    def get_anonymous_data(self, request):
        context = {}
        sesid = None
        if 'sesid' in request.COOKIES:
            sesid = request.COOKIES.get('sesid')
        try:
            context['anonim'] = AnonymousUser.objects.get(sesid=sesid)
        except AnonymousUser.DoesNotExist as e:
            context['anonim'] = None
        return context
