import requests
import requests.auth
import json

class RedditParser(object):
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

    def send_request(self, query, article_limit, comment_limit):
        self.comments_obj = {}
        self.comments_obj["comments"] = []

        response = requests.get("https://oauth.reddit.com/search?q=" + query  +"&limit=" + str(article_limit) + "&sort=top", headers=self.headers)
        data = response.json()
        # print data
        for i in xrange(0, len(data["data"]["children"])):
            id = data["data"]["children"][i]["data"]["id"]
            children = requests.get("https://oauth.reddit.com/comments/" + id + "/.json?limit=" + str(comment_limit) + "&depth=1", headers=self.headers).json()
            for j in xrange(0, len(children[1]["data"]["children"])-1):
                # print children[1]["data"]["children"][j]["data"]["body"]
                c_obj = {}
                c_obj["text"] = children[1]["data"]["children"][j]["data"]["body"]
                self.comments_obj["comments"].append(c_obj)

        return self.comments_obj

r = RedditParser();
print r.send_request('paris',1,6)


