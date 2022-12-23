from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import UserProfile
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "c0f1d110ef394239a361685bd18e9264"
CLIENT_SECRET = "ffacd9cb464f457caf00e1a09ad1fa62"


client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)


sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def compare_playlists(request, username):
    user = UserProfile.objects.get(username=username)
    users = UserProfile.objects.exclude(username=username)
    similar_songs = {}
    for u in users:
        playlist1_url = user.spotify_playlist
        playlist2_url = u.spotify_playlist
        playlist1_id = playlist1_url[34:56]
        playlist2_id = playlist2_url[34:56]


        playlist1 = sp.playlist_tracks(playlist_id=playlist1_id)
        playlist2 = sp.playlist_tracks(playlist_id=playlist2_id)


        track_names1 = [track['track']['name'] for track in playlist1["items"]]    
        track_names2 = [track['track']['name'] for track in playlist2["items"]]

        fav_artist1=[track['track']['artists'][0]['name'] for track in playlist1["items"]]
        fav_artist2=[track['track']['artists'][0]['name'] for track in playlist2["items"]]

        fav_songs_list=[]
        for i in track_names1:
            for j in track_names2:
                if i == j and i not in fav_songs_list:
                    fav_songs_list.append(i)


        similar_song = len(set(track_names1).intersection(set(track_names2)))
        tot_songs=len(set(track_names1).union(set(track_names2)))
        similar=int((similar_song/tot_songs)*100)
        similar_songs[u.username] = [str(similar),u.instagram_link]
    return render(request, 'compare_playlists.html', {'user': user, 'similar_songs': similar_songs})


from django.shortcuts import render, redirect
from .forms import UserProfileForm

def create_user(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserProfileForm()
    return render(request, 'sign-up.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = UserProfile.objects.get(username=username)
        if user.password==password:
            return redirect("http://127.0.0.1:8000/get/{}".format(username))

    return render(request, 'login.html')