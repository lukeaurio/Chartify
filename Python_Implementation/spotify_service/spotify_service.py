import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
import os
import json

def dumpIt(obj):
    return json.dumps(obj,indent=4,sort_keys=True,default=str)

class TrackStats:
    def __init__(self, trackAnalysis) -> None:
        self.acousticness    = trackAnalysis["acousticness"]
        self.danceability    = trackAnalysis["danceability"]
        self.energy          = trackAnalysis["energy"]
        self.instrumentalness= trackAnalysis["instrumentalness"]
        self.liveness        = trackAnalysis["liveness"]
        self.speechiness     = trackAnalysis["speechiness"]
        self.valence         = trackAnalysis["valence"]
    
    def acceptedValues():
        return ["acousticness","danceability","energy", "instrumentalness", "liveness", "speechiness", "valence" ]

    def toStatDict(self):
        return {
             "acousticness"       : self.acousticness,
             "danceability"       : self.danceability,
             "energy"             : self.energy,
             "instrumentalness"   : self.instrumentalness,
             "liveness"           : self.liveness,
             "speechiness"        : self.speechiness,
             "valence"            : self.valence 
        }

class Playlist:
    def __init__(self, Name, id) -> None:
        self.Name = Name
        self.id = id
        self.track_ids = []
        self.track_names = []
        self.trackStats = []
    def toDict(self):
        return {
            "Name" : self.Name, 
            "id" : self.id, 
            "track_ids" : self.track_ids, 
            "track_names" : self.track_names, 
            "trackStats" : [ stat.toStatDict() for stat in self.trackStats],
        } 

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
        res = self.client.audio_features( trackIds)
        ret = []
        for x in res:
            ret.append(TrackStats(x))
        return ret
    def analyzePlaylistById(self, playlistId:'int'):
        return self.analyzePlaylistByTrackIds(self.processPlaylistById(playlistId).track_ids)

    def processPlaylist(self, playlist: Playlist):        
        for i, song in enumerate(self.client.playlist_tracks(playlist.id)['items']):
            playlist.track_ids.append(song['track']['id'])
            playlist.track_names.append(song['track']['name'])
            #json.dumps(song['track'],indent=4,sort_keys=True,default=str) // useful method to get raw json out of your methods. the dcoumentation isn't always clear about all of this
        playlist.trackStats = self.analyzePlaylistByTrackIds(playlist.track_ids)  
        return playlist

    def processPlaylistById(self, playlistId: int):
        playlist = self.client.playlist(playlistId)
        currentPlaylist = Playlist(playlist['name'], playlist['id'])
        return self.processPlaylist(currentPlaylist)