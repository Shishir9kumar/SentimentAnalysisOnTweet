import sys
import json



def wordCount(tweet_file):
    data = []
    totalWord = 0  # total number of words
    wordCount = {}  # occurence of each word
    for line in tweet_file:
        data.append(json.loads(line))
    for tweet in data:
        if tweet.has_key("text"): # get the text of tweet
            tokens = tweet["text"].lower().split(" ")
            totalWord += len(tokens) # calculate total numner of words in collection
            for token in tokens:
                if wordCount.has_key(token):
                    wordCount[token] = wordCount[token]+1 # calculate each word count
                else:
                    wordCount[token] = 1
    printFrequency(totalWord, wordCount) # print frequency



def printFrequency(totalWord, wordCount):
    for word in wordCount.keys():
        frequency = wordCount[word]/float(totalWord)
        print word.lstrip(),frequency



def main():
    tweet_file = open(sys.argv[1])
    wordCount(tweet_file)



if __name__ == '__main__':
    main()
