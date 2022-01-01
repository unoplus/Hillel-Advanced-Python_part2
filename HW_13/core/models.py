from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F


class SetTimeData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(SetTimeData):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    images = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODULE, null=True,
                                blank=False, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Like(SetTimeData):
    post = models.ForeignKey('Post', null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODULE, null=False, blank=False, on_delete=models.CASCADE)
    status = models.BooleanField(null=True, blank=True)
