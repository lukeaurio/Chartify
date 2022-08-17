import lyricsgenius as lgfile = open("lyrics_.txt", "w")


token = ""

genius = lg.Genius(GENIUS_API_KEY, 
skip_non_songs=True, 
excluded_terms=["(Remix)", "(Live)"], 
remove_section_headers=True)

search = 'Villan Vibes'
genius_search_url = "http://api.genius.com/search?q=" + search + "&access_token=" + token

response = requests.get(genius_search_url)
json_data = response.json()

# for song in json_data['response']['hits']:
#     print(song['result']['full_title'])

test = genius.search_song("Villan Vibes").lyrics

print(test)
import requests



# def get_lyrics(arr, k):
#     c = 0
#     for name in arr:
#         try:
#             songs = (genius.search_artist(name, max_songs=k, sort='popularity')).songs
#             s = [song.lyrics for song in songs]
#             file.write("\n \n   <|endoftext|>   \n \n".join(s))
#             c += 1
#             print(f"Songs grabbed:{len(s)}")
#         except:
#             print(f"some exception at {name}: {c}")

# get_lyrics(['Logic', 'Frank Sinatra', 'Rihanna'], 3)