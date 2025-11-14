from django.shortcuts import render
from rest_framework.generics import ListAPIView,
from rest_framework import status
from rest_framework.response import Response

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# Create your views here.

class BookAPIView(ListAPIView):
    queryset =

