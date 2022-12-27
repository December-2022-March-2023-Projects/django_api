from django.db import models

# Create your models here.

class Animedata(models.Model):

  def __str__(self):
    return self.name

  name = models.CharField(max_length=200)
  anime_type = models.CharField(max_length=20, default='series')
  episodes = models.IntegerField(default=0)
  duration = models.FloatField()
  rating = models.FloatField()
  genre = models.CharField(max_length=200, default='slice of life')