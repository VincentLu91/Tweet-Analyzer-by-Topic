from textblob import TextBlob
from nltk.corpus import stopwords
import re
import string
import os
from textblob.translate import Translator
from langdetect import detect

def textblobGetPolarity(text):
    return TextBlob(text).sentiment.polarity

def textblobGetLabel(text):
    if detect(text) != 'en':
        translator = Translator()
        #return 'Non-English'
        text = translator.translate(text, to_lang='en')
    if textblobGetPolarity(text) < 0:
        return 'Negative'
    elif textblobGetPolarity(text) == 0:
        return 'Neutral'
    else:
        return 'Positive'