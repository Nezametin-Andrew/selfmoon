from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ProfileView, ProfileUpdateView, UploadImageView, SaveImageView, TrashAvatar


urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('edit/<int:pk>/', ProfileUpdateView.as_view(), name='edit_profile'),
    path('upload_img/', UploadImageView.as_view(), name='upload_image'),
    path('save_img/', SaveImageView.as_view(), name='save_image'),
    path('trash_avatar/', TrashAvatar.as_view(), name='trash_avatar'),

]