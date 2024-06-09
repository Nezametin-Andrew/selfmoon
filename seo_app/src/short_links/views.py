import uuid
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class CreateLinkTask(View):

    def get(self, request):
        return render(request, 'short_link/create_task.html', {})

    def post(self, request):
        print(request.POST)
        return JsonResponse({})


@method_decorator(csrf_exempt, name='dispatch')
class CreateTemplateLinkView(View):

    def post(self, request):
        if user := request.user:
            return JsonResponse({'short_link': f'{settings.DOMAIN}/short_link/{user.pk}/{str(uuid.uuid4())}'})
        return JsonResponse({'short_link': ''})