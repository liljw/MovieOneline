from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.TextField()
    released_date = models.TextField()
    running_time = models.TextField()

    def __str__(self):
        return f'{self.title}'
    
    