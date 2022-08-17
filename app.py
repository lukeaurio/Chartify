from flask import Flask
from spotify_service import spotify_service
import os
from helpers import helpers as h
from spotifysongtest import getSentiment 
import plotly.io as pio
import plotly.graph_objects as go

app = Flask(__name__)
sp = spotify_service.SpotifyService()

@app.route("/analysis/playlist/<playlist_id>/<measure>")
def specific_measure_route(playlist_id,measure: str):
    if measure not in spotify_service.TrackStats.acceptedValues():
        return "Not a proper value"
    playlist = sp.processPlaylistById(playlist_id)
    
    return generate_chart(playlist, [measure], measure.capitalize())

@app.route("/analysis/playlist/<playlist_id>")
def all_measure_route(playlist_id):
    playlist = sp.processPlaylistById(playlist_id)
    
    return generate_chart(playlist, spotify_service.TrackStats.acceptedValues())

@app.route("/user/playlists/<user_id>")
def user_playlist_route(user_id):
    playlists = sp.get_all_user_playlists(user_id = user_id)
    return h.dumpIt([i.basicStats() for i in playlists])

#print(getSentiment("zacmac310", 0))
#songs = getSentiment("zacmac310", 0)

@app.route("/user/playlists/<user_id>/<playlistNum>")
def sentiment_route(user_id, playlistNum):
    song = getSentiment(user_id, playlistNum)
    return generate_chart(song)


def generate_chart(songs, graph_scope = ""):
    fig = go.Figure()
    
    # fig.add_trace(go.Scatter(
    #     x = list(songs.keys()),
    #     y = list(songs.values()),
    #     #name = measure.capitalize(),
    #     line =dict( width=2),
    #     connectgaps=False
    #     ))
    
    fig.add_trace(go.Bar(
        x = list(songs.keys()),
        y = list(songs.values()),
        
        ))


    fig.update_layout(title=f"{graph_scope}Flow of Zac's Wedding playlist",
                   xaxis_title='Track Title',
                   yaxis_title='Value',
                   template = "plotly_dark"
                   )
    return fig.to_html()

