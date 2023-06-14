"""videoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from videos import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('accounts/', include('allauth.urls')),
    path('',views.index,name='index'),
    path('videos/',views.get_videos,name='videos'),
    path('videos/add/',views.add_videos,name='add_video'),
    path('videos/list/',views.get_videos,name='videos_list'),
    path('playlists',views.get_playlist,name='playlists'),
    path('playlists/add/',views.add_playlist,name='add_playlists'),
    path('playlists/add-video/',views.add_video_to_playlist,name='add_video_to_playlist'),
    path('playlists/remove-video/',views.remove_video_from_playlist,name='remove_video_from_playlist'),
    path('videos/play/<int:video_id>/',views.remove_video_from_playlist,name='play_video'),
    # path('oauth2/authorize/', views.MyLoginView.as_view(), name='oauth2_authorize'),
    # path('oauth2/callback/', views.oauth2_callback, name='oauth2_callback'),
]
