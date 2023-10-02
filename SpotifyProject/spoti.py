import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

DEVICE_ID = '150586ce83215a940752eacac810a978dd04df4f'
CLIENT_ID = '5ebc076cffba4119b006204218218836'
CLIENT_SECRET = '89008a17fda6494fa61ffebb8cf3885d'


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                    redirect_uri="http://localhost:8080",
                                                       scope="user-read-playback-state,user-modify-playback-state"))

#sp.transfer_playback(device_id=DEVICE_ID, force_play=False)

def skipToNext(): 
    #sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:3VqeTFIvhxu3DIe4eZVzGq'])
    sp.next_track()
    time.sleep(2)

def skipToPrevious():
    #sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:0dcnrLo8s1rhjm8euGjI4n'])
    sp.previous_track()
    time.sleep(2)

def changeVolume(volume):
    sp.volume(volume_percent=volume, device_id=DEVICE_ID)
    


#skipToNext()