import os
import re

from dateutil.parser import parse

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")


def clean_text(tweet: str):
    tweet = tweet.lower()
    tweet = re.sub(r"^https://t.co/[a-zA-Z0-9]*\s", " ", tweet)
    tweet = re.sub(r"\s+https://t.co/[a-zA-Z0-9]*\s", " ", tweet)
    tweet = re.sub(r"\s+https://t.co/[a-zA-Z0-9]*$", " ", tweet)
    tweet = re.sub(r"http\S+|www\S+|https\S+", "", tweet, flags=re.MULTILINE)
    tweet = " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet).split())
    tweet = re.sub(r"\@\w+|\#", "", tweet)
    tweet = re.sub(r"\W", " ", tweet)
    tweet = re.sub(r"\d", " ", tweet)
    tweet = re.sub(r"\s+[a-z]\s+", " ", tweet)
    tweet = re.sub(r"\s+[a-z]$", " ", tweet)
    tweet = re.sub(r"^[a-z]\s+", " ", tweet)
    tweet = re.sub(r"\s+", " ", tweet)

    return tweet


twitter_json_mapping = {
    "tweet_id": lambda x: int(x["id"]),
    "created_at": lambda x: parse(str(x["created_at"])),
    "text": lambda x: x["text"].lower(),
    "hashtags": lambda x: ",".join([i["text"] for i in x["entities"]["hashtags"]]),
    "url": lambda x: ",".join([i["url"] for i in x["entities"]["urls"]]),
    "expanded_url": lambda x: ",".join(
        [i["expanded_url"] for i in x["entities"]["urls"]]
    ),
    "display_url": lambda x: ",".join(
        [i["display_url"] for i in x["entities"]["urls"]]
    ),
    "source": lambda x: re.findall('">(.*)</a>', x["source"])[0]
    if x["source"]
    else "null",
    "user_id": lambda x: int(x["user"]["id"]),
    "name": lambda x: x["user"]["name"],
    "screen_name": lambda x: x["user"]["screen_name"],
    "location": lambda x: x["user"]["location"] if x["user"]["location"] else "null",
    "description": lambda x: x["user"]["description"],
    "followers_count": lambda x: int(x["user"]["followers_count"]),
    "friends_count": lambda x: int(x["user"]["friends_count"]),
    "listed_count": lambda x: int(x["user"]["listed_count"]),
    "favourites_count": lambda x: int(x["user"]["favourites_count"]),
    "statuses_count": lambda x: int(x["user"]["statuses_count"]),
    "geo": lambda x: x["geo"],
    "coordinates": lambda x: x["coordinates"],
    "contributors": lambda x: x["contributors"],
    "retweet_count": lambda x: x["retweet_count"],
    "favorite_count": lambda x: x["favorite_count"],
    "lang": lambda x: x["lang"],
    "text": lambda x: clean_text(x["text"]),
}
