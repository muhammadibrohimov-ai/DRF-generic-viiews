from rest_framework import serializers
from .models import Book, Author
from datetime import datetime as dt


class BookSerializer(serializers.ModelSerializer):
    
    author = serializers.PrimaryKeyRelatedField(
        queryset = Author.objects.all()
    )
    author_name = serializers.CharField(source='author.fullname', read_only=True)
    
    class Meta:
        model = Book
        fields = ['id', 'name', 'desc', 'author', 'year', 'price', 'created_at', 'author_name']
        read_only_fields = ['id', 'author_name', 'created_at']
        

class AuthorSerializer(serializers.ModelSerializer):
    
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['id', 'fullname', 'country', 'created_at', 'books', 'year']
        read_only_fields = ['id', 'created_at', 'books']
        
        



