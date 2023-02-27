import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from secret import APP_CLIENT_ID, APP_CLIENT_SECRET

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=APP_CLIENT_ID,
                                                           client_secret=APP_CLIENT_SECRET))

if __name__ == "__main__":
    print(sp)