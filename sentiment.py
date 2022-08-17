import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def sentiment_scores(song_titles):
    song_scores = {}
    for song_name, lyric in songs:  
     
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

        avgpos = pos_score_total/pos_total
        avgneg = neg_score_total/neg_total

        if avgpos > avgneg:
            song_scores[song_name] = avgpos
        else: 
            song_scores[song_name] = avgneg * -1
    return song_scores



        # lyrics = lyrics.lower()
        # from nltk.tokenize import word_tokenize
        # from nltk.corpus import stopwords

        # text_tokens = word_tokenize(lyrics)
        
        # newlyrics = [word for word in text_tokens if not word in stopwords.words()]
        # newlyrics
        

        
        # fd = nltk.FreqDist(newlyrics)
        # fd.most_common(30)