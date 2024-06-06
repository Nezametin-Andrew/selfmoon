from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.urls import reverse


tasks = [
    {
        'img': 'assets/img/short_link.png',
        'title': 'Сокращенные ссылки',
        'description': '', 'create_link': '/short_link/create/',
        'min_price': '0.75', 'executor': '0.52', 'amount': '0', 'user_amount': '0'
    }
]


class CreateTaskView(View):

    def get(self, request):
        return render(request, 'tasks/task_create.html',
                      {
                          'navigation': [
                              {
                                  'section': 'Создать задание',
                                  'class': 'breadcrumb-item active',
                                  'title': 'Создать задачу',
                                  'url': reverse('create_task'),
                                  'url_class': 'active'

                              }
                          ],
                          'tasks': tasks
                      }
                      )
