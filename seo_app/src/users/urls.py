from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    RegisterView, WebPasswordResetView, register_confirm, SendMailConfirmView,
    SetPasswordView, LoginView, LogoutView
)


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('register/', RegisterView.as_view(), name="register"),
    path("register_confirm/<token>/", register_confirm, name="register_confirm"),
    path('send_mail_confirm_view/', SendMailConfirmView.as_view(), name='send_mail_for_confirm'),

    path('set_password/', SetPasswordView.as_view(), name='set_password'),
    path("password_reset/", WebPasswordResetView.as_view(), name="password_reset"),


]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)