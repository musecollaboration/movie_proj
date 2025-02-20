# Generated by Django 5.1.5 on 2025-02-10 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0009_movie_director_alter_movie_budget_alter_movie_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('director_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
    ]
