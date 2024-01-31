from django.db import models

from core.abstract.models import AbstractManager, AbstractModel


class CategoryManager(AbstractManager):
    pass


class Category(AbstractModel):
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.category_name}"


class HealthcenterManager(AbstractManager):
    pass


class Healthcenter(AbstractModel):
    healthcenter_name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(default='', blank=True)
    phone_number = models.CharField(max_length=18, default='', blank=True)
    address = models.CharField(max_length=200, default='', blank=True)
    #long = models.
    #lat = models.

    category = models.ForeignKey(
        to=Category, null=True, on_delete=models.SET_NULL
    )

    #insurances

    def __str__(self):
        return f"{self.healthcenter_name}"