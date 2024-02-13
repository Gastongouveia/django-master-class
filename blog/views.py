from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostList(ListAPIView):
    queryset = BlogPost.objects.filter(published_at__isnull=False)
    serializer_class = BlogPostSerializer

