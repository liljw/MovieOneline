from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.TextField()
    director = models.CharField(max_length=50)
    released_date = models.TextField()
    running_time = models.TextField()
    rating = models.FloatField()
    actors = models.ManyToManyField('Actor', related_name="starred_movies")
    genre = models.ManyToManyField('Genre', related_name="genre_movies")

class Actor(models.Model):
    name = models.CharField(max_length=100)

class Genre(models.Model):
    name = models.CharField(max_length=100)
    