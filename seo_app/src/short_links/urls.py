from django.urls import path
from .views import CreateLinkTask


urlpatterns = [
    path('create/', CreateLinkTask.as_view(), name='short_link_create'),
]