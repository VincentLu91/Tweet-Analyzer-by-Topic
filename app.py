from flask import Flask, render_template, request
import GetOldTweets3 as got
from textblob_sentiment import textblobGetLabel
from vader_sentiment import vaderGetLabel

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    classifiers = ['Textblob', 'VADER']
    if request.method == "POST":
        topicName = request.form['content']
        if not topicName:
            error = 'Field is empty'
            return render_template('index.html', error=error)
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(topicName).setMaxTweets(10)
        tweets = got.manager.TweetManager.getTweets(tweetCriteria)
        return render_template('index.html', tweets=tweets, classifiers=classifiers)
    else:
        return render_template('index.html')

app.jinja_env.globals.update(textblobGetLabel=textblobGetLabel)
app.jinja_env.globals.update(vaderGetLabel=vaderGetLabel)

if __name__ == "__main__":
    app.run(debug=True)