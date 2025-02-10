from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from transliterate import translit


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
