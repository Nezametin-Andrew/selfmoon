from django.db import models

from ..account.models import Account


class AnonymousUser(models.Model):

    sesid = models.CharField(max_length=255, unique=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f"{str(self.pk)}: {self.sesid}"


class IpAddress(models.Model):

    ip = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(AnonymousUser, on_delete=models.CASCADE)