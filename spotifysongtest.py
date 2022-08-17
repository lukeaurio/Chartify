from spotify_service import spotify_service
import lyricsgenius as lg
from helpers import helpers as h
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

from nltk.sentiment import SentimentIntensityAnalyzer

sp = spotify_service.SpotifyService()

#takes username and playlist #

def lyricgrabber(user_id, playlistNum):

    playlist = sp.get_all_user_playlists(user_id)


    x = sp.processPlaylist(playlist[int(playlistNum)])

    genius = lg.Genius(INSERT_GENIUS_API_KEY, 
    skip_non_songs=True, 
    excluded_terms=["(Remix)", "(Live)"], 
    remove_section_headers=True)

    songlyricsmap = {}
    for track in x.track_names:

        try:
            songlyrics = genius.search_song(track).lyrics
            songlyricsmap[track] = songlyrics
        except:
            pass
    return songlyricsmap


def sentiment_scores(song_titles):
    song_scores = {}

    for song_name in song_titles:
        lyric = song_titles[song_name]
    # for song_name, lyric in song_titles:  
    #     print(song_name, lyric)
        sia = SentimentIntensityAnalyzer()

        linebyline = lyric.split('\n')

        pos_total = 0
        neg_total = 0

        pos_score_total = 0
        neg_score_total = 0

        for l in linebyline:
            if sia.polarity_scores(l)['pos'] != 0:
                pos_total += 1
                pos_score_total += sia.polarity_scores(l)['pos']

            if sia.polarity_scores(l)['neg'] != 0:
                print(l, sia.polarity_scores(l))
                neg_total += 1
                neg_score_total += sia.polarity_scores(l)['neg']
        if pos_total > 0 and neg_total > 0:
            avgpos = pos_score_total/pos_total
            avgneg = neg_score_total/neg_total

            if avgpos > avgneg:
                song_scores[song_name] = avgpos
            else: 
                song_scores[song_name] = avgneg * -1
    return song_scores

def getSentiment(user_id, playlistNum):
    return sentiment_scores(lyricgrabber(user_id, playlistNum))

def getWordFreq(user_id, playlistNum):
    return word_frequency(lyricgrabber(user_id, playlistNum))
    
def word_frequency(song_map):
    for song_name in song_map:
        lyrics = song_map[song_name]

        lyrics = lyrics.lower()
    
        text_tokens = word_tokenize(lyrics)
 
    newlyrics = [word for word in text_tokens if not word in stopwords.words()]
    
 