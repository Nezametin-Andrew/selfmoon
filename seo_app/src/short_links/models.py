from django.db import models


class AnonimUser(models.Model):
    pass


class GroupLink(models.Model):

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена задания')


class LinkService(models.Model):
    title = models.CharField(max_length=255)
    default_link = models.CharField(max_length=255, unique=True)
    api_link = models.CharField(max_length=255)
    alias = models.BooleanField(default=True)
    group = models.ForeignKey(GroupLink, on_delete=models.CASCADE)
    description = models.TextField()


class TaskLink(models.Model):

    task = models.OneToOneField(GroupLink, on_delete=models.CASCADE)
    user = models.ForeignKey(AnonimUser, on_delete=models.CASCADE)
    passed_task = models.BooleanField(default=False)
    access_key = models.CharField(max_length=255, unique=True, null=True, blank=True, default=None)


class ShortLink(models.Model):

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField()
    endpoint = models.CharField(max_length=255, unique=True)
    short_link = models.CharField(max_length=255)
    passed = models.BooleanField(default=False)
    task_link = models.ForeignKey(TaskLink, on_delete=models.CASCADE)
