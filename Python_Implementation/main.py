import spotify_service
import os
import helpers as h
def main():
    sp = spotify_service.SpotifyService()
    x = sp.get_all_user_playlists(user_id = os.getenv("SPOTIPY_USER"))
    print(h.dumpIt(x[0].toDict()))



    print("fin")

if __name__=="__main__":
    main()
