import json
import urllib2
import requests


one = 'http://graph.facebook.com/search?'
two = 'q=coffee&type=event'
three = '&access_token=1715504075335935'
ulink = one+two

print ulink

#data = json.load(urllib2.urlopen(ulink))

response = requests.get(ulink)


print response


#"http://graph.facebook.com/search?q=coffee&type=place"

#https://graph.facebook.com/v1.0/search?q=search_query&type=post&access_token={access_token}


GET https://graph.facebook.com/v2.3/oauth/access_token?
    client_id={app-id}
   &redirect_uri={redirect-uri}
   &client_secret={app-secret}
   &code={code-parameter}