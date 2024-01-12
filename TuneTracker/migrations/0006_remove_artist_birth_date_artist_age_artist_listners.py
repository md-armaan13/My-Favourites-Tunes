# Generated by Django 5.0.1 on 2024-01-11 20:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TuneTracker', '0005_alter_artist_birth_date_alter_song_release_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='birth_date',
        ),
        migrations.AddField(
            model_name='artist',
            name='age',
            field=models.IntegerField(default=36, validators=[django.core.validators.MinValueValidator(0, message='Age should be positive')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artist',
            name='listners',
            field=models.IntegerField(default=170000000, validators=[django.core.validators.MinValueValidator(0, message='Listners should be positive')]),
            preserve_default=False,
        ),
    ]