from django.contrib import admin
from django.utils.timezone import now

from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'created_by', 'published_at', 'published_by', 'is_premium')
    search_fields = ('title', 'body')
    list_filter = ('is_premium', 'created_at', 'published_at')
    actions = ['mark_published', 'mark_unpublished']

    @admin.action(description='Publicar postagens selecionadas')
    def mark_published(self, request, queryset):
        count = queryset.filter(published_at__isnull=True).update(published_at=now(), published_by=request.user)
        msg = '%s postagem publicada.' if count == 1 else '%s postagens publicadas.'
        self.message_user(request, msg % count) 

    @admin.action(description='Despublicar postagens selecionadas')
    def mark_unpublished(self, request, queryset):
        count = queryset.filter(published_at__isnull=False).update(published_at=None, published_by=None)
        msg = '%s postagem despublicada.' if count == 1 else '%s postagens despublicadas.'
        self.message_user(request, msg % count)