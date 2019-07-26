from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class BaseModel(models.Model):
    created_by = models.ForeignKey(User, related_name='%(class)s_created_by', on_delete=models.DO_NOTHING)
    updated_by = models.ForeignKey(User, related_name='%(class)s_updated_by', on_delete=models.DO_NOTHING,
                                   blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    inactive = models.BooleanField(default=False, blank=True, null=True)
    deleted = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        abstract = True
