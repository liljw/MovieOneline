from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.TextField()
    released_date = models.TextField()
    running_time = models.TextField()
    # tmdb_pk = models.IntegerField()
    def __str__(self):
        return f'{self.title}'
    

    @property
    def poster_url(self):
        return f'https://image.tmdb.org/t/p/w200{ self.poster }'
    
