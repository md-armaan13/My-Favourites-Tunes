# Generated by Django 5.0.1 on 2024-01-11 18:09

import TuneTracker.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TuneTracker', '0003_rename_artists_artist_rename_songs_song'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='artists-images', validators=[TuneTracker.models.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='songs-images/', validators=[TuneTracker.models.validate_file_size]),
        ),
    ]
