from django.utils.translation import gettext_lazy as _
from django.db import models

from core.abstract.models import AbstractManager, AbstractModel


class InsuranceManager(AbstractManager):
    pass


class Insurance(AbstractModel):
    name = models.CharField(max_length=150, unique=True)
    email = models.EmailField(_("email address"), default='', blank=True)
    phone_number = models.CharField(max_length=15, default='', blank=True)
    address = models.CharField(max_length=200, default='', blank=True)
    comment = models.TextField(default='', blank=True)

    objects = InsuranceManager()

    def __str__(self):
        return f"{self.name}"
