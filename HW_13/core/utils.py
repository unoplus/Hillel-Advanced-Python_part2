from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creation date')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='update date')

    class Meta:
        abstract = True
