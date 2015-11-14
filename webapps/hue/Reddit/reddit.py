import praw
import json
import time
import urllib2

# use GET /api/subreddits_by_topic


def reddit_query(q,num):
    comments_red = {'comments' : []}
    try:
    	r = praw.Reddit(user_agent='web:com.example.myredditapp:v1.0.0 (by /u/sharangc)')
    	subreddits = r.get_subreddit(q).get_hot(limit=num)
    	comm = []
    	for sbr in subreddits:
    		comm = comm + sbr.comments

    	for c in comm:
    		com_obj = {'text':str(c)}
    		comments_red['comments'].append(com_obj)

    	print len(comments_red['comments'])
    	return comments_red
    except:
    	print "Error in Reddit Query"

   	return None



#print "Input some string: "
start = time.time()

data = urllib2.urlopen('http://someurl/path/to/json')

#comments = reddit_query('Paris',5)


#with open('reddit_data.json', 'w') as outfile:
#    json.dump(comments, outfile)

end = time.time()
print end - start

