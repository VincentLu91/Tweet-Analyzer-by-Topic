# Tweet Analyzer by Topic

The Tweet Analyzer takes in any topic entered by the user and returns the 10 most recent tweets regarding a topic along with their timestamps, username, and their sentiment (negative, neutral, or positive).

The Tweet Analyzer uses both Textblob and VADER sentiment analysis algorithms and compares between the two. It also uses a translator library - [translate](https://pypi.org/project/translate/) to translate non-English tweets in the backend before applying the algorithms to determine whether it is negative, neutral, or positive.

The original intention is to build the analyzer for companies to analyze tweets about them, but due to the scope of the project, it is revised so that a user can input any topic and it returns results. This is a more general use case and helpful feasibility study to assess any topic being analyzed. If more tweets returned about a given topic is negative, then it stands to reason that there is something about said topic that is inherently negative, and gives users insights into the sentiments of a topic.
