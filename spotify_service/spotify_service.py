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

class Track:
    def __init__(self, id ="", name = "",artists="") -> None:
        self.id = id
        self.name = name
        self.artists = artists
        self.stats = None

    def toTrackDict(self):
        return {
            "title" : self.name,
            "trackId" : self.id,
            "artists" : self.artists,
            "stats" : self.stats.toStatDict()
        }

class Playlist:
    def __init__(self, Name, id) -> None:
        self.Name = Name
        self.id = id
        self.tracks = []
        
    def toDict(self):
        return {
            "Name" : self.Name, 
            "playlistId" : self.id, 
            "tracks" : [ track.toTrackDict() for track in self.tracks],
        } 
    def basicStats(self):
        return {
            "Name" : self.Name, 
            "id" : self.id
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

    def get_all_user_playlists(self, user_id:'int',process=False) -> 'list()':
        playlists = self.client.user_playlists(user=user_id)
        ret = []
        while playlists:
            for i, playlist in enumerate(playlists['items']):
                currentPlaylist = Playlist(playlist['name'], playlist['id'])
                ret.append(self.processPlaylist(currentPlaylist) if process else currentPlaylist)
            
            if playlists['next']:
                playlists = self.client.next(playlists)
            else:
                playlists = None
        return ret

    def analyzePlaylistByTrackIds(self, trackList = []):
        res = self.client.audio_features( t.id for t in trackList)
        ret = 0
        for x in res:
            trackList[ret].stats = TrackStats(x)
            ret +=1
        return trackList
    def analyzePlaylistById(self, playlistId:'int'):
        return self.processPlaylistById(playlistId)

    def processPlaylist(self, playlist: Playlist):     
        for i, song in enumerate(self.client.playlist_tracks(playlist.id)['items']):
            playlist.tracks.append(Track(song['track']['id'],song['track']['name'], [a["name"]for a in song['track']['artists']]))
        playlist.tracks = self.analyzePlaylistByTrackIds(playlist.tracks)  
        return playlist

    def processPlaylistById(self, playlistId: int):
        playlist = self.client.playlist(playlistId)
        currentPlaylist = Playlist(playlist['name'], playlist['id'])
        return self.processPlaylist(currentPlaylist)