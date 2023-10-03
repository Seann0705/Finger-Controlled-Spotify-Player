import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

#important info of spotify account
DEVICE_ID = 'x'
CLIENT_ID = 'y'
CLIENT_SECRET = 'z'


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                    redirect_uri="http://localhost:8080",
                                                       scope="user-read-playback-state,user-modify-playback-state"))

#sp.transfer_playback(device_id=DEVICE_ID, force_play=False)

def skipToNext(): 
    sp.next_track()
    time.sleep(2)

def skipToPrevious():
    sp.previous_track()
    time.sleep(2)

def changeVolume(volume):
    sp.volume(volume_percent=volume, device_id=DEVICE_ID)

