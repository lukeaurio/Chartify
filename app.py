from flask import Flask
from spotify_service import spotify_service
import os
from helpers import helpers as h
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

def generate_chart(playlist, measures, graph_scope = ""):
    fig = go.Figure()

    for measure in measures:
        fig.add_trace(go.Scatter(
            x = [i.name + ": (" + i.artists[0] + ")" for i in playlist.tracks],#playlist.track_names,
            y = [(i.stats.toStatDict()[measure] if i.stats.toStatDict()[measure] > .001 else None) for i in playlist.tracks],
            name = measure.capitalize(),
            line =dict( width=2),
            connectgaps=True
            )
        )

    fig.update_layout(title=f"{graph_scope} Flow of {playlist.Name}",
                   xaxis_title='Track Title',
                   yaxis_title='Value',
                   template = "plotly_dark"
                   )
    return fig.to_html()
