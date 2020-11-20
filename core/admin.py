from django.contrib import admin
from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created')
    list_filter = ('created',)
    search_fields = ('title',)
    ordering = ('created',)
    list_per_page = 20
