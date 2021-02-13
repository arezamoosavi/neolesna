import os
import re

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")


twitter_json_mapping = {
    "tweet_id": lambda x: x["id"],
    "created_at": lambda x: x["created_at"],
    "text": lambda x: x["text"],
    "hashtags": lambda x: ",".join([i["text"] for i in x["entities"]["hashtags"]]),
    "url": lambda x: ",".join([i["url"] for i in x["entities"]["urls"]]),
    "expanded_url": lambda x: ",".join(
        [i["expanded_url"] for i in x["entities"]["urls"]]
    ),
    "display_url": lambda x: ",".join(
        [i["display_url"] for i in x["entities"]["urls"]]
    ),
    "source": lambda x: re.findall('">(.*)</a>', x["source"])[0] if x["source"] else "",
    "user_id": lambda x: str(x["user"]["id"]),
    "name": lambda x: x["user"]["name"],
    "screen_name": lambda x: x["user"]["screen_name"],
    "location": lambda x: x["user"]["location"] if x["user"]["location"] else "null",
    "description": lambda x: x["user"]["description"],
    "followers_count": lambda x: x["user"]["followers_count"],
    "friends_count": lambda x: x["user"]["friends_count"],
    "listed_count": lambda x: x["user"]["listed_count"],
    "favourites_count": lambda x: x["user"]["favourites_count"],
    "statuses_count": lambda x: x["user"]["statuses_count"],
    "geo": lambda x: x["geo"],
    "coordinates": lambda x: x["coordinates"],
    "contributors": lambda x: x["contributors"],
    "retweet_count": lambda x: x["retweet_count"],
    "favorite_count": lambda x: x["favorite_count"],
    "lang": lambda x: x["lang"],
}
