from django.db import models
from django.contrib.auth.models import AbstractUser
from critic.models import Oneline, Reply

from movie.models import Movie

class User(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='follower')
    like_oneline = models.ManyToManyField(Oneline, related_name='like_oneline_user')
    rated_movie = models.ManyToManyField(Movie, related_name='rated_user')
    