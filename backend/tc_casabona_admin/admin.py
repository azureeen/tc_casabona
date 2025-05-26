# backend/app/admin.py

from django.contrib import admin
from .models import SiteConfig, BlogPost

@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ('title', 'contact_email')


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'tags')
    search_fields = ('title', 'tags')
    list_filter = ('date',)