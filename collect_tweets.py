import json
import pymongo
import tweepy

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

keywords = [
    '#wind', 
    #'#gas',
    '#hydro',
    '#coal',
    '#nuclear',
    '#arstemcoal',
    '#arstemwind',
    #'#arstemgas',
    '#arstemhydro',
    '#arstemnuclear',
    '#artem']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()

        self.db = pymongo.MongoClient().arstem

    def on_data(self, tweet):
        self.db.tweets.insert(json.loads(tweet))

    def on_error(self, status_code):
        return True # Don't kill the stream

    def on_timeout(self):
        return True # Don't kill the stream


sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))
sapi.filter(track=keywords)
