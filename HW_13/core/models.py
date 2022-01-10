from django.db import models
from django.conf import settings


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        abstract = True


class Post(TimeStampMixin):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    images = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODULE, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Like(TimeStampMixin):
    post = models.ForeignKey('Post', null=False, blank=False, on_delete=models.CASCADE)
    status = models.BooleanField(null=True, blank=True)
