from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostList(ListAPIView):
    queryset = BlogPost.objects.filter(published_at__isnull=False)
    serializer_class = BlogPostSerializer
    ordering = ['-created_at']
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'body']
    ordering_fields = ['created_at','published_at', 'title']

