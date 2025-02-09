# Generated by Django 5.1.5 on 2025-02-09 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_movie_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='currency',
            field=models.CharField(choices=[('EUR', 'Euro'), ('USD', 'Dollar'), ('RUB', 'Rubles')], default='RUB', max_length=3),
        ),
    ]
