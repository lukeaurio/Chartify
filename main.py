from spotify_service import spotify_service
import os
from helpers import helpers as h
import plotly.io as pio
import plotly.graph_objects as go

def main():
    pio.renderers.default = 'browser'
    sp = spotify_service.SpotifyService()
    playlists = sp.get_all_user_playlists(user_id = os.getenv("SPOTIPY_USER"), process=True)
    print(h.dumpIt(playlists[0].toDict()))
    print("fin")

if __name__=="__main__":
    main()
