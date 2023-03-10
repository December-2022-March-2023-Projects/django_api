from rest_framework import serializers
from .models import Animedata

class AnimeSerializer(serializers.ModelSerializer):
  image = serializers.ImageField(max_length=None, use_url=True)
  class Meta:
    model = Animedata
    fields = ['id', 'name', 'duration', 'rating', 'genre', 'image']