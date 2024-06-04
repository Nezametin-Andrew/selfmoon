import secrets
import string
import uuid
from datetime import timedelta

from django.conf import settings
from django.contrib.auth.views import PasswordResetView
from django.core.cache import cache
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views import View
from django.template import loader
from django.http import HttpResponse

from .models import Person
from .forms import RegisterForm, LoginForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate, login, logout


class LoginView(View):
    form_class = LoginForm
    template_name = 'users/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                if request.POST.get('remember') is not None:
                    request.session.set_expiry(timedelta(weeks=1).seconds)
                login(request, user)
                return redirect('profile')
            else:
                return render(request, self.template_name, {'form': form, 'error': 'Неправильное имя пользователя или пароль'})
        return render(request, self.template_name, {'form': form})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('main')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'users/register_page.html'
    success_url = reverse_lazy("send_mail_for_confirm")

    def form_valid(self, form):
        person, created = Person.objects.get_or_create(email=form.cleaned_data["email"])
        new_pass = None

        if created:
            alphabet = string.ascii_letters + string.digits
            new_pass = ''.join(secrets.choice(alphabet) for i in range(8))
            person.set_password(new_pass)
            person.username = f"user: n{str(person.id)}"
            person.save(update_fields=["password", "username"])

        if new_pass or person.is_active is False:
            token = uuid.uuid4().hex
            redis_key = settings.SEO_USER_CONFIRMATION_KEY.format(token=token)
            cache.set(redis_key, {"person_id": person.id}, timeout=settings.SEO_USER_CONFIRMATION_TIMEOUT)
            cache.set(f'us{str(person.id)}', {"passw": new_pass, 'email': form.cleaned_data['email']})

            confirm_link = self.request.build_absolute_uri(
                reverse_lazy(
                    "register_confirm", kwargs={"token": token}
                )
            )
            message = _(f"Перейдите по этой ссылке %s \n"
                        f"для завершения регистрации на {settings.DOMAIN} ! \n" % confirm_link)
            if new_pass:
                message += f"Ваш логин : {person.email} \nВаш пароль:  {new_pass} \n "

            send_mail(
                subject=_("Please confirm your registration!"),
                message=message,
                from_email=settings.DEFAULT_EMAIL,
                recipient_list=[person.email, ]
            )
        return super().form_valid(form)


def register_confirm(request, token):
    redis_key = settings.SEO_USER_CONFIRMATION_KEY.format(token=token)
    person_info = cache.get(redis_key) or {}

    if person_id := person_info.get("person_id"):
        person = get_object_or_404(Person, id=person_id)
        person.is_active = True
        person.save(update_fields=["is_active"])

        us_data = cache.get(f'us{str(person_id)}')
        user = authenticate(request, email=us_data.get('email'), password=us_data.get('passw'))
        if user is not None:
            login(request, user)

        return redirect(to=reverse_lazy("set_password"))
    else:
        return redirect(to=reverse_lazy("register"))


class SetPasswordView(View):
    def get(self, request):
        return HttpResponse(loader.get_template('users/set_password.html').render(request=request, context={}))

    def post(self, request):
        return HttpResponse(loader.get_template('users/send_to_mail_confirm.html').render(request=request, context={}))


class WebPasswordResetView(PasswordResetView):
    template_name = 'web/password_reset_email.html'


class SendMailConfirmView(View):
    def get(self, request):
        return HttpResponse(loader.get_template('users/send_to_mail_confirm.html').render(request=request, context={}))

    def post(self, request):
        return HttpResponse(loader.get_template('users/send_to_mail_confirm.html').render(request=request, context={}))


