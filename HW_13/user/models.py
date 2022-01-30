from django.db import models
from django.contrib.auth.models import User
from .utils import ChoicesMixin


class UserProfile(ChoicesMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.PositiveIntegerField(null=True, blank=True, verbose_name='phone number')
    gender = models.CharField(max_length=50, null=True, blank=False, choices=ChoicesMixin.GENDER,
                              default='Not specified', verbose_name='gender')
    profile_pic = models.ImageField(null=True, blank=True, upload_to='profiles_pic/%Y/%m/%d/')

    def __str__(self):
        return str(self.user)
