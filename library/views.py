from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


class BookListCreateView(generics.ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        genre = self.request.query_params.get('genre')
        is_available = self.request.query_params.get('is_available')

        if genre:
            queryset = queryset.filter(genre=genre)

        if is_available is not None:
            queryset = queryset.filter(is_available=is_available.lower() == 'true')

        return queryset


class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
