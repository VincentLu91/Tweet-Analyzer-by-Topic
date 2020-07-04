from textblob import TextBlob
from translate import Translator
from langdetect import detect

def textblobGetPolarity(text):
    return TextBlob(text).sentiment.polarity

def textblobGetLabel(text):
    try:
        if detect(text) != 'en':
            translator = Translator(to_lang="en")
            text = translator.translate(text)
    except:
        return 'Cannot be processed'
    if textblobGetPolarity(text) < 0:
        return 'Negative'
    elif textblobGetPolarity(text) == 0:
        return 'Neutral'
    else:
        return 'Positive'