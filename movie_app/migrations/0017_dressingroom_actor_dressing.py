# Generated by Django 5.1.5 on 2025-02-12 06:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0016_alter_movie_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='DressingRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.ImageField(upload_to='')),
                ('number', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='actor',
            name='dressing',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie_app.dressingroom'),
        ),
    ]
