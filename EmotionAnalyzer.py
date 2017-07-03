import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_emotion_from_sentences(sentences, player):
    analyzer = SentimentIntensityAnalyzer()
    data = []
    emotion = {}
    for sentence in sentences:
        vs = analyzer.polarity_scores(sentence)
        data.append(vs)
    emotion[player] = data
    return emotion

