from django.db import models

# Create your models here.

class Song(models.Model):

    songName = models.TextField()
    album = models.TextField()
    artist = models.TextField()

    def __unicode__(self):
    	return self.songName