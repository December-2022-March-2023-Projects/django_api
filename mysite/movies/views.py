from django.shortcuts import render
from rest_framework import viewsets
from .seriallizers import MovieSerializer
from .models import Moviedata
# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
  queryset = Moviedata.objects.all()
  serializer_class = MovieSerializer

class HorrorViewSet(viewsets.ModelViewSet):
  queryset = Moviedata.objects.filter(genre='horror')