SentimentAnalysisOnTweet
========================

## Collecting Twitter Data
Run TwitterStream.py with access codes to get tweets from Twitter API.


## Calculating Tweet sentiment
Program to compute the sentiment of each tweet based on the sentiment scores of the terms in the tweet. The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet.


to execute use below command :
python tweetSentiment.py AFINN-111.txt tweets.txt


## Calculating sentiment score of unknow term 
termSentiment.py calculates sentiment score for terms which sentiment score is not provided. Based on metric score of tweet and positive and negative word occurence in the tweet.

to execute use below command :
python termSentiment.py AFINN-111.txt tweets.txt


## Frequency histogram of Livestream Twitter Data
frequency.py to compute the term frequency histogram of the livestream data

to execute use below command :
python frequency.py tweets.txt


## Predicting happiest state in USA using sentiment score and geo-location
happiest_state.py calculates the happiest state in United states based on sentiment score and Geo-Location of tweets and returns the name of the happiest state as a string.

to execute use below command :
$ python happiest_state.py <sentiment_file> <tweet_file>


## Top Ten HashTags
top_ten.py that computes the ten most frequently occurring hashtags from the data you gathered.

to execute use below command :
$ python top_ten.py <tweet_file>
