import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
import os
import json

class Playlist:
    def __init__(self, Name, id) -> None:
        self.Name = Name
        self.id = id
        self.track_ids = []
        self.track_names = []

class SpotifyService:
    #only if you want to use a config file. I just use Environment variables
    #f = open("./config.json")
    #configs = json.loads(f)
    #f.close()
    def __init__(self) -> None:
        self.auth_manager = SpotifyClientCredentials(
            client_id=os.getenv("SPOTIPY_CLIENT_ID"),#or configs["client_id"]
            client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")#or configs["client_secret"] 
            )
        self.client = spotipy.Spotify(auth_manager=self.auth_manager)

    def get_all_user_playlists(self, user_id:'int') -> 'list()':
        playlists = self.client.user_playlists(user=user_id)
        ret = []
        while playlists:
            for i, playlist in enumerate(playlists['items']):
                #print(f"{i+1}: {playlist['name']} {playlist['uri']}")
                currentPlaylist = Playlist(playlist['name'], playlist['id'])
                #print(json.dumps(playlist,indent=4,sort_keys=True, default=str))
                
                ret.append(self.processPlaylist(currentPlaylist))
            if playlists['next']:
                playlists = self.client.next(playlists)
            else:
                playlists = None
        return ret

    def analyzePlaylistByTrackIds(self, trackIds = []):
        ret = self.client.audio_features( trackIds)
        return ret
    def analyzePlaylistById(self, playlistId:'int'):
        return self.analyzePlaylistByTrackIds(self.processPlaylistById(playlistId).track_ids)

    def processPlaylist(self, playlist: Playlist):        
        for i, song in enumerate(self.client.playlist_tracks(playlist.id)['items']):
            playlist.track_ids.append(song['track']['id'])
            playlist.track_names.append(song['track']['name'])
            #json.dumps(song['track'],indent=4,sort_keys=True,default=str) // useful method to get raw json out of your methods. the dcoumentation isn't always clear about all of this
        return playlist

    def processPlaylistById(self, playlistId: int):
        playlist = self.client.playlist(playlistId)
        currentPlaylist = Playlist(playlist['name'], playlist['id'])
        return self.processPlaylist(currentPlaylist)