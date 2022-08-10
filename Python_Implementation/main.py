import spotify_service
import os
import helpers as h
import plotly.io as pio
import plotly.graph_objects as go

def main():
    pio.renderers.default = 'browser'
    sp = spotify_service.SpotifyService()
    playlists = sp.get_all_user_playlists(user_id = os.getenv("SPOTIPY_USER"))
    print(h.dumpIt(playlists[0].toDict()))

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x = playlists[0].track_names,
        y = [i.energy for i in playlists[0].trackStats],
        name = "energy",
        line =dict(color='royalblue', width=4),
        connectgaps=True
        )
    )

    fig.update_layout(title=f"Flow of {playlists[0].Name}",
                   xaxis_title='Track Title',
                   yaxis_title='Value')
    fig.show()

    print("fin")

if __name__=="__main__":
    main()
