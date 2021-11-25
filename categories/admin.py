from django.contrib import admin
from categories.models import Category, models

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'published']