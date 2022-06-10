from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60, blank=True)
    telephone = models.CharField(max_length=20)
    email = models.CharField(max_length=255, blank=True)
    created_in = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name
