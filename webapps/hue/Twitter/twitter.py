import json,os
from twit import *

CONSUMER_KEY = "eelzYoinnhURGfDZwyljlBsCQ"
CONSUMER_SECRET = "QfdVvKkX4ud3BpCQez6F5fmp3foRzQJrcZ03oWIwyMfdfUorP5"

ACCESS_TOKEN = "4183683136-fniPCNshPdfCVMGDLpD2SkuSuzwfuJrrj9SxXev"
ACCESS_TOKEN_SECRET = "9xR7od8njdqQm5vNKVaZ3haVtXOwDVj15qhSuAnk7KBL4"

MAX_TWEETS = 500

def twitter_query(q):
    tweets = {'comments' : []}
    path = os.path.dirname(os.path.realpath(__file__))
    count = 0
    try:
        tso = TwitterSearchOrder()
        tso.set_keywords(q.split(" "))
        ts = TwitterSearch(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, verify=True)
        
        for tweet in ts.search_tweets_iterable(tso):
            if tweet['coordinates'] != None:
                count = count + 1 
            if (tweet['lang'] == 'en'):
                tweet_obj = {'user' : tweet['user']['screen_name'],
                             'text' : tweet['text'],
                             'favorites' : tweet['favorite_count'],
                             'retweets' : tweet['retweet_count']}
                tweets['comments'].append(tweet_obj)
                if (len(tweets['comments']) >= MAX_TWEETS):
                    break;   

    except TwitterSearchException as e:
        print(e)

    print count
    with open(path+'/data.json', 'w') as outfile:
        json.dump(tweets, outfile)


twitter_query('manutd')
