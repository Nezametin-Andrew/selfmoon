from django.shortcuts import render
from django.views import View
from django.http import JsonResponse


class CreateLinkTask(View):

    def get(self, request):
        return render(request, 'short_link/create_task.html', {})

    def post(self, request):
        print(request.POST)
        return JsonResponse({})
