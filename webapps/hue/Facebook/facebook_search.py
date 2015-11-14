import json
import urllib2
import requests


one = 'http://graph.facebook.com/search?'
two = 'q=coffee&type=place'
three = '&access_token=1715504075335935|55e9ecd3535429e6e69557607c93769bq'
ulink = one+two + three

print ulink

data = json.load(urllib2.urlopen(ulink))



print data


#"http://graph.facebook.com/search?q=coffee&type=place"

#https://graph.facebook.com/v1.0/search?q=search_query&type=post&access_token={access_token}