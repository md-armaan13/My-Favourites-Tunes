from django.contrib import admin
from django.http import HttpRequest
from .models import Artist , Song
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html


@admin.register(Artist)
class ArtistsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'songs_count' , 'image')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    ordering = ('id',)

    @admin.display(ordering='songs_count')
    def songs_count(self,product):
        
        return product.songs_count

    def get_queryset(self, request: HttpRequest):
        return super().get_queryset(request).annotate(songs_count = Count('song'))

@admin.register(Song)
class SongsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist_link', 'streams', 'likes', 'release_date')
    list_display_links = ('id', 'title', 'artist_link')
    search_fields = ('title', 'artist__name')
    list_filter = ('artist',)
    ordering = ('id',)

    def artist_link(self, obj):
        url = reverse("admin:TuneTracker_artist_change", args=[obj.artist.id])
        return format_html('<a href="{}">{}</a>', url, obj.artist.name)
    artist_link.short_description = 'Artist'