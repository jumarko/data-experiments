# https://stackoverflow.com/questions/25501403/storing-the-secrets-passwords-in-a-separate-file
from twitter_config import consumer_key, consumer_secret, access_token, access_token_secret
import tweepy
from textblob import TextBlob

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
