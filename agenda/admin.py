from django.contrib import admin
from .models import Category, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'telephone',
        'email',
        'category'
        ]

    list_display_links = ['id', 'first_name', 'last_name']
    list_per_page = 10
    search_fields = ['first_name', 'last_name', 'telephone']
