from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)

    def get_url(self):
        return reverse('url_actors', args=[self.id])

    def __str__(self):
        if self.gender == self.MALE:
            return f'Актер {self.first_name} {self.last_name}'
        return f'Актриса {self.first_name} {self.last_name}'


class Movie(models.Model):
    EURO = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICES = [
        (EURO, 'Euro'),
        (USD, 'Dollar'),
        (RUB, 'Rubles'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(100)
    ])
    years = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(
        default=1000000,
        blank=True,
        validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    slug = models.SlugField(default='', null=False, db_index=True)

    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    actors = models.ManyToManyField(Actor)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(translit(self.name, 'ru', reversed=True))
    #     super().save(*args, **kwargs)

    def get_url(self):
        return reverse('url_name', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}%'

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['slug'], name='slug_idx'),
        ]


# python manage.py shell_plus --print-sql
# from movie_app.models import Movie
# from django.db.models import Q   (& или , - AND), (| - OR), (~Q - NOT)
# python -m pip install django-debug-toolbar
