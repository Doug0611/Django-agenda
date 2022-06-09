from django.contrib import admin
from .models import Category, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    ...
