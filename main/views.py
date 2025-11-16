from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# Create your views here.

class AllView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_fields = ['country', 'year']
    search_fields = ['fullname', 'country', 'books__name', 'books_desc']

class SingleAuthorView()
