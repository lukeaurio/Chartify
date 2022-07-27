import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
import flask
import json
import os

def main():
    #only if you want to use a config file. I just use Environment variables
    #f = open("./config.json")
    #configs = json.loads(f)
    #f.close()
    auth_man = SpotifyClientCredentials(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),#or configs["client_id"]
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")#or configs["client_secret"] 
    )
    sp = spotipy.Spotify(auth_manager=auth_man)

    playlists = sp.user_playlists(user=os.getenv("SPOTIPY_USER"))
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            print(f"{i+1}: {playlist['name']} {playlist['uri']}")
            #print(json.dumps(playlist,indent=4,sort_keys=True, default=str))
            for j, song in enumerate(sp.playlist_tracks(playlist['id'])['items']):
                #json.dumps(song['track'],indent=4,sort_keys=True,default=str)
                print(f"\t\t{j} {song['track']['name']} by {[t['name'] for t in song['track']['artists']]} ")
                print(f"\t\t\t{song['track']['id']}")
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None

    return 0

if __name__=="__main__":
    main()
