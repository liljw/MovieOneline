from django.db import models
from django.conf import settings

from movie.models import Movie

class Oneline(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.FloatField()

class Reply(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    oneline = models.ForeignKey(Oneline, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)


