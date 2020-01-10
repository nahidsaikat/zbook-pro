from django.db import models
from django.urls import reverse

from zbook.system.models import BaseModel
from zbook.account.models import Account


class Inventory(BaseModel):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=16, null=True, blank=True)
    address = models.TextField(default='', null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('account:subtype:detail-update', args=[self.pk])
