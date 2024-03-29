# Tweet Analyzer by Topic

Written in Flask, the Tweet Analyzer takes in any topic entered by the user and returns the 10 most recent tweets regarding a topic along with their timestamps, username, permalinks, and their sentiment (negative, neutral, or positive).

The Tweet Analyzer uses both Textblob and VADER sentiment analysis algorithms and compares between the two. It also uses a translator library - [translate](https://pypi.org/project/translate/) to translate non-English tweets to English tweets in the backend before applying the algorithms to determine whether it is negative, neutral, or positive. However, it returns tweets written in their original languages with the sentiments computed. 

The original intention was to build the analyzer for companies to analyze tweets about them, but due to the scope of the project, it was revised so that a user can input any topic and it returns results. This is a more general use case and feasibility study to assess any topic being analyzed. If more tweets returned about a given topic is negative, then it stands to reason that there is something about said topic that is inherently negative, and gives users insights into the sentiments of a topic.

I have elaborated on the Tweet Analyzer in the following blog post: https://vincentlu91.github.io/2020/06/29/Sentiment-Analysis-on-Tweets-of-Companies.html

## How to access the data app

### Deployed App

You can use the following link here: https://analyze-tweets-proj.herokuapp.com. 

Update (October 7 2022): when scraping tweets in Heroku, there would be a H13 desc="Connection closed without response" error. You may want to consider testing the application in development environment. The data application is otherwise live in production

(October 8 2022): Starting November, Heroku's free dynos will no longer be available therefore the application can no longer run on Heroku.

### Alternatively, you can access the application in development environment

Libraries and their versions are included in requirements.txt. To install the virtual environment, run the following:

```
python3 -m venv env # or python -m venv env
source env/bin/activate
pip3 install -r requirements.txt # or pip install -r requirements.txt
```

At this point the environment should be set up with required libraries to run the application. To run the app, enter:
```
python app.py
```

Then in the browser, enter ```localhost:5000```

## How to use the data app
You will see a prompt to enter the topic.
![martymcfly](https://user-images.githubusercontent.com/3411100/86506250-b0ae1280-bd9b-11ea-9771-fe2d92197bf0.png)
  
You could enter any topic you like, and find the 10 most recent tweets about the topic you entered, along with the attitudes expressed.
For example, I entered 'samsung', and here are the recent tweets:

![martymcfly](https://user-images.githubusercontent.com/3411100/86506278-f5d24480-bd9b-11ea-8543-0614f47b67e3.png)
