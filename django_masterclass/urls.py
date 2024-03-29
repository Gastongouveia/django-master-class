"""
URL configuration for django_masterclass project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.contrib import admin
from django.urls import include, path

@api_view()
def root(request):
    return Response({
        'Blog': reverse('blog:post-list', request=request),
    })

urlpatterns = [
    # Django
    path('admin/', admin.site.urls),
    
    # third-party
    path('api-auth/', include('rest_framework.urls')),
    
    #local
    path('', root),
    path('blog/', include('blog.urls', namespace='blog')),
]
