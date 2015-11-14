import requests
import requests.auth
import json


client_id = 'EfEAJfojHDJAKg';
client_secret = 'TRT2IR7lRJ1b4rm2H596fzcbzo0';
client_auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
post_data = {"grant_type": "password", "username": "sharangc", "password": "manutd"}
headers = {"User-Agent": 'web:com.example.myredditapp:v1.0.0 (by /u/sharangc)'}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
resp = response.json()

acc_tok = resp['access_token']

auth_bear =  "bearer " + (str(acc_tok))

headers = {"Authorization": auth_bear, "User-Agent": 'web:com.example.myredditapp:v1.0.0 (by /u/sharangc)'}


#response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)



response = requests.get("https://oauth.reddit.com/search?q=Paris&limit=2&sort=top", headers=headers)

data = response.json()
# print data
for i in xrange(0, len(data["data"]["children"])):
    id = data["data"]["children"][i]["data"]["id"]
    children = requests.get("https://oauth.reddit.com/comments/" + id + "/?sort=top&limit=1&depth=1", headers=headers).json()
    print children