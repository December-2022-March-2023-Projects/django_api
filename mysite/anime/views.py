from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AnimeSerializer
from .models import Animedata

# Create your views here.

class AnimeViewSet(viewsets.ModelViewSet):
  queryset = Animedata.objects.all()
  serializer_class = AnimeSerializer