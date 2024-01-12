from django.urls import path
from . import views


urlpatterns = [
    path('',views.home , name= "tunes.home"),
    path('artist/',views.artist , name= "tunes.artist"),
    path('add/song/',views.add_song , name= "tunes.add_songs"),
    path('add/artist/',views.add_artist , name= "tunes.add_artist"),
]
