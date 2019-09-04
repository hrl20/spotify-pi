from django.db import models

# Create your models here.
class Song(models.Model):
	title = models.CharField(max_length=200)
	artist = models.CharField(max_length=200)
	spotify_url = models.TextField()
	queued = models.BooleanField(default=True)


	def __str__(self):
		return self.title