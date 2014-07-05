SentimentAnalysisOnTweet
========================

Program to compute the sentiment of each tweet based on the sentiment scores of the terms in the tweet. The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet.


to execute use below command :

python tweetSentiment.py AFINN-111.txt tweets.txt



termSentiment.py calculates sentiment score for terms which sentiment score is not provided. Based on metric score of tweet and positive and negative word occurence in the tweet.

to execute use below command :

python termSentiment.py AFINN-111.txt tweets.txt


frequency.py to compute the term frequency histogram of the livestream data

to execute use below command :

python frequency.py tweets.txt


