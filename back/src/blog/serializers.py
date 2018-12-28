from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .models import Category, Post
from .documents import PostDocument

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class PostDocumentSerializer(DocumentSerializer):

    class Meta:
        document = PostDocument
        fields = (
            'id',
            'author',
            'title',
            'content',
            'created_at',
            'updated_at'
        )
        