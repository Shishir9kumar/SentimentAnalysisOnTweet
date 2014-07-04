import sys
import json

phrase = []

def getPhrases(afinn):
    # analyze AFINN file and get all the phrases
    for line in afinn:
        temp = line.split("\t")[0]
        if len(temp.split(" ")) >1 :
            phrase.append(temp)

def calculateScore(text,sent_file):
    #  get the word sentimental score from AFINN-111.txt
    sentiment = {}
    sentiment = givenSentimentScore(sent_file)
    score=0
    for str in phrase:
        if text.find(str) >= 0:
            score+=(text.count(str)*sentiment[str])
            text = text.replace(str,"")
    tokens = text.split(" ")
    for token in tokens:
        if sentiment.has_key(token.lower()):
            score+=sentiment[token.lower()]
    print score


def givenSentimentScore(sent_file):
    score = {}       #  dictionary for storing sentiment score
    for line in sent_file:
        term, scor = line.split("\t")       #  store word and respective score
        score[term] = int(scor)
    return score


def sentimentScore(output,sent_file):
    # store tweets in data
    data = []
    for line in output:
        data.append(json.loads(line))
    #calculate sentiment score
    for tweet in data:
        if tweet.has_key("text"):
            calculateScore(tweet["text"],sent_file)
            sent_file.seek(0,0)

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[2])
    getPhrases(open(sys.argv[1]))
    sentimentScore(tweet_file,open(sys.argv[1]))
    #lines(sent_file)
    #lines(tweet_file)


if __name__ == '__main__':
    main()
