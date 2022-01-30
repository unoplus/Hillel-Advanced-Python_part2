from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
from .utils import TimeStampMixin


class Post(TimeStampMixin):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='post name')
    content = models.TextField(null=False, blank=False, verbose_name='content preview')
    images = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODULE, null=True, blank=False, on_delete=models.SET_NULL,
                             verbose_name='user name')
    count_views = models.IntegerField(default=0, verbose_name='count view')

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse_lazy("post_view", kwargs={"pk": self.pk})


class Like(TimeStampMixin):
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODULE, null=False, blank=False, on_delete=models.CASCADE)
    status = models.BooleanField(null=True, blank=True)
 