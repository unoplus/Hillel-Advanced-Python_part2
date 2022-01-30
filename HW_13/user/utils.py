from django.db import models


class ChoicesMixin(models.Model):
    NOT_SPECIFIED = 'Not specified'
    MALE = 'Male'
    FEMALE = 'Female'
    GENDER = [
        (NOT_SPECIFIED, 'Not specified'),
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    class Meta:
        abstract = True