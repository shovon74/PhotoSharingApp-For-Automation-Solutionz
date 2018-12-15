from django.contrib.auth.models import Permission, User
from django.db import models
from django.urls import reverse


class Album(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Image(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image_title = models.CharField(max_length=250)
    image_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.image_title
