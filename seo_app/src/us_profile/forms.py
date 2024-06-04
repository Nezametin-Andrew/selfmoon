from django import forms
from .models import Profile


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'full_name', 'job', 'country', 'city', 'address', 'phone', 'vk', 'gmail', 'yandex', 'tg', 'avatar', 'about'
        ]