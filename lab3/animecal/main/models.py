from django.db import models


class Anime(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    poster = models.ImageField(upload_to="photos/")
    year = models.IntegerField()
    episodes = models.IntegerField()


class Comment(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField(blank=False)
    data = models.DateTimeField(auto_now_add=True)
