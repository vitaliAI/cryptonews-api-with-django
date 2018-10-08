from django.shortcuts import render
from crypto.models import CryptoNews
from rest_framework import generics
from .serializers import NewsSerializer

class NewsList(generics.ListAPIView):
    queryset = CryptoNews.objects.all()
    serializer_class = NewsSerializer
