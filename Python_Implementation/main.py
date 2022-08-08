import spotify_service
import os
def main():
    sp = spotify_service.SpotifyService()
    x = sp.get_all_user_playlists(user_id = os.getenv("SPOTIPY_USER"))
    print(sp.analyzePlaylistByTrackIds(x[0].track_ids))

    print("fin")

if __name__=="__main__":
    main()
