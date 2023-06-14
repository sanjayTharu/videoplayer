from django import forms
from .models import Video,Playlist

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'file', 'owner')


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ('name', 'videos', 'owner')
