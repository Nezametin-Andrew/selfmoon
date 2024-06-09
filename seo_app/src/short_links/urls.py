from django.urls import path
from .views import CreateLinkTask, CreateTemplateLinkView


urlpatterns = [
    path('create/', CreateLinkTask.as_view(), name='short_link_create'),
    path('create_link_template/', CreateTemplateLinkView.as_view(), name='create_template_link'),
]