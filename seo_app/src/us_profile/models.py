import os
import uuid

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from ..users.models import Person
from ..account.models import Account


class Profile(models.Model):
    user = models.OneToOneField(
        Person, on_delete=models.CASCADE,
        related_name='profile', related_query_name='profile', verbose_name='Пользователь'
    )

    full_name = models.CharField(max_length=255, verbose_name="",  blank=True)
    job = models.CharField(max_length=255, verbose_name="",  blank=True)
    country = models.CharField(max_length=255, verbose_name="",  blank=True)
    city = models.CharField(max_length=255, verbose_name="", blank=True)
    address = models.CharField(max_length=255, verbose_name="", blank=True)
    phone = models.CharField(max_length=255, verbose_name="", blank=True)
    vk = models.CharField(max_length=255, verbose_name="", blank=True)
    gmail = models.EmailField(verbose_name="",  blank=True)
    yandex = models.EmailField(verbose_name="",  blank=True)
    tg = models.CharField(max_length=255, verbose_name="",  blank=True)
    avatar = models.ImageField(upload_to=f"", blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    about = models.TextField(verbose_name="users/avatar/", blank=True)

    # def save(self, *args, **kwargs):
    #     if self.avatar:
    #         _, ext = os.path.splitext(self.avatar.name)
    #         filename = f"{uuid.uuid4()}{ext}"
    #         self.avatar.name = os.path.join('users', 'avatars', filename)
    #     super().save(*args, **kwargs)


@receiver(post_save, sender=Person)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()