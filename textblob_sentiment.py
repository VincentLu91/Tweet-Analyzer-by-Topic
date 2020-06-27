from textblob import TextBlob
from nltk.corpus import stopwords
import re
import string
import os
from os import listdir
from langdetect import detect

def textblobGetPolarity(text):
    return TextBlob(text).sentiment.polarity

def textblobGetLabel(text):
    if detect(text) != 'en':
        return 'Non-English'
    if textblobGetPolarity(text) < 0:
        return 'Negative'
    elif textblobGetPolarity(text) == 0:
        return 'Neutral'
    else:
        return 'Positive'