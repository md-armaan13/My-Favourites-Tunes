from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Artist , Song
from django.db.models import Count


def home(request):

    try :
        if  not request.user.is_authenticated:
            return redirect('users.login')  
      
        context = {}
        user = request.user
        context['email'] = user.email
        songs = Song.objects.filter(user=user).select_related('artist')
        context['songs'] = songs
        return render(request,'TuneTracker/index.html',context)
      
    except  Exception as e:
        print(e)
        return HttpResponse("ERROR 404 NOT FOUND")

def artist(request):

    try :
        if  not request.user.is_authenticated:
            return redirect('users.login')  
        
        context = {}
        user = request.user
        context['email'] = user.email
        artists = Artist.objects.filter(user=user).annotate(songs_count=Count('song'))
        context['artists'] = artists
        return render(request,'TuneTracker/artist.html',context)
        
    except  Exception as e:
        print(e)
        return HttpResponse("ERROR 404 NOT FOUND")
    

def add_song(request):

    try:  
        
        if  not request.user.is_authenticated:
            return redirect('users.login')  
        
        if request.method == 'POST':
            title = request.POST['title']
            artist_id = request.POST['artist']
            release_date = request.POST['release_date']
            streams = request.POST['streaming']
            likes = request.POST['like']

            if 'image' in request.FILES:
                image = request.FILES['image']
            else:
                image = None 

            if(title == '' or artist_id == '' or release_date == '' or image == None or streams == '' or likes == ''):
                messages.error(request, 'Fields cannot be empty')
                return redirect('tunes.add_songs')
            
            if(Song.objects.filter(title=title).exists()):
                messages.error(request, 'Song already exists')
                return redirect('tunes.add_songs')
            
            artist_obj = Artist.objects.get(id=artist_id)

            song = Song(title=title, artist=artist_obj, release_date=release_date, image=image ,user = request.user , streams=streams , likes=likes)
            song.save()

            return redirect('tunes.home')
        
        else :
            artists = Artist.objects.all()
            context = {'artists':artists}
            return render(request,'TuneTracker/uploadSong.html',context)
        
    except  Exception as e:
        print(e)
        return HttpResponse("ERROR 404 NOT FOUND")
    
def add_artist(request):
    try:
        if  not request.user.is_authenticated:
            return redirect('users.login')
        
        if request.method == 'POST':
            name = request.POST['name']
            age = request.POST['age']
            listners = request.POST['listners']

            if 'image' in request.FILES:
                image = request.FILES['image']
            else:
                image = None 
            if(name == '' or age == '' or listners == '' or image == None):
                messages.error(request, 'Fields cannot be empty')
                return redirect('tunes.add_artist')

            if(Artist.objects.filter(name=name).exists()):
                messages.error(request, 'Artist already exists')
                return redirect('tunes.add_artist')
            
            artist = Artist(name=name, age=age, image=image ,user = request.user , listners=listners)
            artist.save()

            return redirect('tunes.artist')
        else :
            return render(request,'TuneTracker/addArtist.html')
        
    except  Exception as e:
        print(e)
        return HttpResponse("ERROR 404 NOT FOUND")
