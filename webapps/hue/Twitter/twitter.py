import json
from twitter import *

CONSUMER_KEY = "eelzYoinnhURGfDZwyljlBsCQ"
CONSUMER_SECRET = "QfdVvKkX4ud3BpCQez6F5fmp3foRzQJrcZ03oWIwyMfdfUorP5"

ACCESS_TOKEN = "4183683136-fniPCNshPdfCVMGDLpD2SkuSuzwfuJrrj9SxXev"
ACCESS_TOKEN_SECRET = "9xR7od8njdqQm5vNKVaZ3haVtXOwDVj15qhSuAnk7KBL4"

MAX_TWEETS = 500

def twitter_query(q):
    tweets = {'comments' : []}

    try:
        tso = TwitterSearchOrder()
        tso.set_keywords(q.split(" "))
        ts = TwitterSearch(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, verify=True)
        
        for tweet in ts.search_tweets_iterable(tso):
            if (tweet['lang'] == 'en'):
                tweet_obj = {'user' : tweet['user']['screen_name'],
                             'text' : tweet['text'],
                             'favorites' : tweet['favorite_count'],
                             'retweets' : tweet['retweet_count']}
                tweets['tweets'].append(tweet_obj)
                if (len(tweets['tweets']) >= MAX_TWEETS):
                    break;

    except TwitterSearchException as e:
        print(e)

    return tweets


print "Input some string: "
tweets = twitter_query(raw_input())

with open('data.json', 'w') as outfile:
    json.dump(tweets, outfile)
