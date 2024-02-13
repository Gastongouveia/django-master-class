from rest_framework import serializers

from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'body',
            'is_premium',
            'created_at',
            'created_by',
            'published_at',
            'published_by',
        ]