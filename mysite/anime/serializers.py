from rest_framework import serializers
from .models import Animedata

class AnimeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Animedata
    fields = ['id', 'name', 'duration', 'rating', 'genre']