from django.shortcuts import render

from rest_framework import viewsets, routers

from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer


router_blog = routers.DefaultRouter()
router_blog.register(r'category', CategoryViewSet)
router_blog.register(r'post', PostViewSet)