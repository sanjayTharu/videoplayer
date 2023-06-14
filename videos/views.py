from django.shortcuts import render,redirect
from .models import Video,Playlist
from django.http import HttpResponseRedirect,HttpResponseBadRequest
from django.contrib.auth import login
# import oauth2_provider
from .forms import VideoForm,PlaylistForm
# from oauth2_provider.views.generic import OAuth2LoginView

# Create your views here.
def index(request):
    videos = Video.objects.all()
    return render(request, 'videos/index.html', {'videos': videos})


def get_videos(request):
    videos = Video.objects.all()
    return render(request,'videos/list.html',{'videos':videos})

def add_videos(request):
    if request.method=='POST':
        form=VideoForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return redirect('videos:list')
        
    return render(request,'videos/add_videos.html',{'form':form})


def get_playlist(request):
    playlist=Playlist.objects.all()
    return render(request,'videos/playlist.html',{'playlist':playlist})

def add_playlist(request):
    if request.method=='POST':
        form=PlaylistForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('videos:playlists')
        
    return render(request,'videos/add_playlist.html',{'form':form})

def add_video_to_playlist(request,playlist_id,video_id):
    Playlist.objects.get(id=playlist_id).videos.add(video_id)
    return redirect('videos:playlists')

def remove_video_from_playlist(request,playlist_id,video_id):
    Playlist.objects.get(id=playlist_id).videos.remove(video_id)
    return redirect('videos:playlists')

def play_video(request,video_id):
    video=Video.objects.get(id=video_id)
    url=video.file.url
    return HttpResponseRedirect(url)

# def oauth2_callback(request):
#     if request.user.is_authenticated():
#         return redirect('videos:list')
#     else:
#         user = oauth2_provider.get_user_from_auth_token(request.GET['access_token'])
#         if user is not None:
#             login(request, user)
#             return redirect('videos:list')
#         else:
#             return HttpResponseBadRequest('Invalid access token.') 


# class MyLoginView(OAuth2LoginView):
#     pass
       
        


