from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    telephone = models.CharField(max_length=20)
    email = models.CharField(max_length=255, blank=True, null=True)
    created_in = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    profile_picture = models.ImageField(
        blank=True,
        upload_to='agenda/img/%Y/%m/%d'
    )
    to_show = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name
