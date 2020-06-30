from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
from nltk.corpus import stopwords
import re
import string
import os
from textblob.translate import Translator
from langdetect import detect

def vaderGetPolarity(text):
    vader_analyzer = SentimentIntensityAnalyzer()
    sentiment_dict = vader_analyzer.polarity_scores(text)
    return sentiment_dict['compound']

def vaderGetLabel(text):
    if detect(text) != 'en':
        translator = Translator()
        #return 'Non-English'
        text = translator.translate(text, to_lang='en')
    if vaderGetPolarity(text) <= - 0.05:
        return 'Negative'
    elif vaderGetPolarity(text) >= 0.05:
        return 'Positive'
    else:
        return 'Neutral'