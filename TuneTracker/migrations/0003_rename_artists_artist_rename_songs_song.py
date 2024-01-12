# Generated by Django 5.0.1 on 2024-01-11 17:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TuneTracker', '0002_artists_user_songs_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Artists',
            new_name='Artist',
        ),
        migrations.RenameModel(
            old_name='Songs',
            new_name='Song',
        ),
    ]