from django.db import models

class Screenplay(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.CharField(max_length=30)
    writer = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    poster_url = models.URLField(blank=True)
    script_url = models.URLField(blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2)
    rotten_tomato_rating = models.DecimalField(max_digits=4, decimal_places=2)

