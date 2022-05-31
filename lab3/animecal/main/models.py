from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name;


class Anime(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    poster = models.ImageField(upload_to="photos/")
    year = models.IntegerField()
    episodes = models.IntegerField()
    status = models.CharField(max_length=255)
    release_day = models.IntegerField(blank=True)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title;

    def get_absolute_url(self):
        return reverse('anime', kwargs={'pk': self.pk})


class Comment(models.Model):
    anime_id = models.ForeignKey(Anime, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    text = models.TextField()
    data = models.DateTimeField(auto_now_add=True)


