from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
from translate import Translator
from langdetect import detect

def vaderGetPolarity(text):
    vader_analyzer = SentimentIntensityAnalyzer()
    sentiment_dict = vader_analyzer.polarity_scores(text)
    return sentiment_dict['compound']

def vaderGetLabel(text):
    try:
        if detect(text) != 'en':
            translator = Translator(to_lang="en")
            text = translator.translate(text)
    except:
        return 'Cannot be processed'
    if vaderGetPolarity(text) <= - 0.05:
        return 'Negative'
    elif vaderGetPolarity(text) >= 0.05:
        return 'Positive'
    else:
        return 'Neutral'