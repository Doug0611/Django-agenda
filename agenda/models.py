from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    telephone = models.CharField(max_length=11)
    email = models.TextField()
    created_in = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
        )

    def __str__(self):
        return self.first_name
