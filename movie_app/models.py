from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    years = models.IntegerField(null=True)
    budget = models.IntegerField(default=1000000)

    def __str__(self):
        return f'{self.name} - {self.rating}%'


# from movie_app.models import Movie
