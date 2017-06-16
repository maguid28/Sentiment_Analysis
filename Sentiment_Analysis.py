# twitter sentiment analysis
# extracting and understanding human feelings from data

import tweepy
from textblob import TextBlob

#create a dev account with twitter to get this info
consumer_key = "xxx"
consumer_secret = "xxx"

access_token = "xxx"
access_token_secret = "xxx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

word = input("Enter a word to search (type x to exit): \n")

while word != "x":

    # store a list of tweets
    public_tweets = api.search(word)

    #print the tweets out
    for tweets in public_tweets :
        print(tweets.text)
        #store sentiment analysis
        analysis = TextBlob(tweets.text)

        # polarity measures how positive or negative the tweet is
        # subjectavity measures how much of an opinion it is vs how factual it is

        if analysis.subjectivity >= 0.8:
            print("Very subjective")
        elif analysis.subjectivity >= 0.5:
            print ("Somewhat subjective")
        elif analysis.subjectivity <= 0.2:
            print("Very objective")
        else:
            print("Somewhat objective")

        if analysis.polarity < 0 :
            print("Negative")
        elif analysis.polarity > 0:
            print("Positive")
        else:
            print("Neutral")

        print(analysis.sentiment, "\n")


    word = input("Enter a word to search (type x to exit): \n")
