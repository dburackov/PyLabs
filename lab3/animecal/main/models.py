from django.db import models


class Animes(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    poster = models.ImageField(upload_to="photos/")
    data = models.DateField()
    episodes = models.IntegerField()


class Comments(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField(blank=False)
    data = models.DateTimeField(auto_now_add=True)
