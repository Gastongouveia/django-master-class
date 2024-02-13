from django.contrib import admin

from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'created_by', 'published_at', 'published_by', 'is_premium')
    search_fields = ('title', 'body')
    list_filter = ('is_premium', 'created_at', 'published_at')