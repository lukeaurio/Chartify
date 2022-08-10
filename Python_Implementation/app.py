from flask import Flask
from spotify_service import spotify_service
import os
from helpers import helpers as h
import plotly.io as pio
import plotly.graph_objects as go

app = Flask(__name__)

@app.route("/<user_id>/<playlist_id>/<measure>")
def root_route(user_id,playlist_id,measure):
    if measure not in spotify_service.TrackStats.acceptedValues():
        return "Not a proper value"
    pio.renderers.default = 'browser'
    sp = spotify_service.SpotifyService()
    #playlists = sp.get_all_user_playlists(user_id = os.getenv("SPOTIPY_USER"))
    playlist = sp.processPlaylistById(playlist_id)
    print(h.dumpIt(playlist.toDict()))

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x = playlist.track_names,
        y = [i.toStatDict()[measure] for i in playlist.trackStats],
        name = "energy",
        line =dict(color='royalblue', width=4),
        connectgaps=True
        )
    )

    fig.update_layout(title=f"Flow of {playlist.Name}",
                   xaxis_title='Track Title',
                   yaxis_title='Value')
    return fig.to_html()
    print("fin")

