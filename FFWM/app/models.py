from django.db import models

# Create your models here.


class UserProfile(models.Model):
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    spotify_playlist = models.CharField(max_length=100)
    instagram_link = models.URLField(blank=True)
    password = models.CharField(max_length=128, blank=True)