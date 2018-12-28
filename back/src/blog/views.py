from django.shortcuts import render

from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from rest_framework import viewsets, routers

from .models import Category, Post
from .serializers import CategorySerializer, PostDocumentSerializer
from .documents import PostDocument


class CategoryViewSet(viewsets.ModelViewSet):
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class PostViewSet(viewsets.ModelViewSet):

#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostViewSet(DocumentViewSet):
    document = PostDocument
    serializer_class = PostDocumentSerializer

    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]

    # Filter fields
    filter_fields = {
        'id': {
            'field': 'id',
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ],
        },
        'title': 'title.raw',
        'content': 'body.raw',
        'author': {
            'field': 'author_id',
            'lookups': [
                LOOKUP_QUERY_IN,
            ]
        },
        'created': 'created',
        'modified': 'modified',
        'pub_date': 'pub_date',
    }

    # Define search fields
    search_fields = (
        'title',
        'content',
    )


# router_blog = routers.DefaultRouter()
# router_blog.register(r'category', CategoryViewSet)
# router_blog.register(r'post', PostViewSet)

router_blog = routers.SimpleRouter()
router_blog.register(
    prefix='posts',
    base_name='posts',
    viewset=PostViewSet
)