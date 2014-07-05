import sys
import json

sentiScore = {}
newTerms = {}

def givenSentimentScore(senti_file):
    for line in senti_file:
        sentiScore[line.split("\t")[0]] = int(line.split("\t")[1])

def findNewTerms(tweet_file):
    data = []
    for line in tweet_file: # read file
        data.append(json.loads(line)) # use json and append in to list
    for tweet in data:
        if tweet.has_key("text"): # check for "text" attribute
            tokens = tweet["text"].split(" ")  # get text and split in tokens
            for token in tokens: # check if token is new term
                if not sentiScore.has_key(token.lower()):
                    newTerms[token.lower()] = 0 # if a new term add it to dictionary


def calculateNewTermsScore(tweet_file):
    data = []
    for line in tweet_file:  # read file
        data.append(json.loads(line))  # use json and append in to list
    pos = 1
    neg = 1
    for newTerm in newTerms:
        for tweet in data:
            if tweet.has_key("text"):  # check for "text" attribute
                text = tweet["text"].lower()
                if text.find(newTerm) >= 0:  # look for new term in tweet text
                    tokens = text.split(" ")  # split text in tokens
                    for token in tokens:
                        if sentiScore.has_key(token):   # check if token is given words
                            if sentiScore[token] > 0:   # check its value
                                pos += sentiScore[token] # if positive add it to pos score
                            else:
                                neg += sentiScore[token] # if negative add it to neg score
        if (pos+neg) == 0: # to avoid divide by zero error
            newScore = 0
        else:
            newScore = ((pos-neg)/(pos+neg))*5 # calculate new score
        pos = 1
        neg = 1
        print newTerm, newScore # print new term and respective sentiment score


def main():
    senti_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    givenSentimentScore(senti_file)  # read given sentiment score of words
    findNewTerms(tweet_file)  # find new terms
    tweet_file.seek(0,0)
    calculateNewTermsScore(tweet_file)  # calculate sentiment score for new terms


if __name__ == '__main__':
    main()
