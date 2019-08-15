import datetime
from django.db import models
from django.urls import reverse

from zbook.system.models import BaseModel
from .choices import AccountType


class AccountSubType(BaseModel):
    name = models.CharField(max_length=64)
    type = models.IntegerField(choices=AccountType.choices, default=AccountType.Asset)
    order = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f'{self.name}#{self.get_type_display()}#{self.order}'

    def get_absolute_url(self):
        return reverse('account:subtype:detail-update', args=[self.pk])

    @property
    def type_text(self):
        return self.get_type_display()


class Account(BaseModel):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, default=None, null=True, blank=True)
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64)
    type = models.IntegerField(choices=AccountType.choices, default=AccountType.Asset, blank=True)
    sub_type = models.ForeignKey(AccountSubType, on_delete=models.DO_NOTHING)
    depth = models.IntegerField(default=0, null=True, blank=True)
    entry_date = models.DateField(default=datetime.date.today, null=True, blank=True)
    description = models.TextField(default='', null=True, blank=True)
    # TODO: Needs to bring currency column

    def __str__(self):
        return f'{self.name}:{self.code}' + ('#' + str(self.parent) if self.parent else '')

    @property
    def type_text(self):
        return self.get_type_display()

    @property
    def sub_type_text(self):
        return self.sub_type.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.depth = self.parent.depth + 1 if self.parent else 0
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
