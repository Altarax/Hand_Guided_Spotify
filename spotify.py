import spotipy, time
from secret import APP_CLIENT_ID, APP_CLIENT_SECRET
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=APP_CLIENT_ID,
                                               client_secret=APP_CLIENT_SECRET,
                                               redirect_uri="http://example.com/",
                                               scope="user-modify-playback-state"))

def next_song():
    sp.next_track()
    time.sleep(2)

def previous_song():
    sp.previous_track()
    time.sleep(2)

def pause_song():
    sp.pause_playback()
    time.sleep(2)