from lyricsgenius import Genius
import os
import json

class genius_service:
    def __init__(self):
        self.client = Genius(os.getenv("GENIUS_TOKEN"))
        self.client.remove_section_headers = True
        self.client.skip_non_songs = False
        self.client.excluded_terms = ["(Remix)", "(Live)"]
    
    def AnalyzeSong():
        return 0