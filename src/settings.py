import os
import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


stop_words = set(stopwords.words("english"))

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
    # tweet =  " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet).split())
    tweet = re.sub(r"\@\w+|\#", "", tweet)
    tweet = re.sub(r"that's", "that is", tweet)
    tweet = re.sub(r"there's", "there is", tweet)
    tweet = re.sub(r"what's", "what is", tweet)
    tweet = re.sub(r"where's", "where is", tweet)
    tweet = re.sub(r"it's", "it is", tweet)
    tweet = re.sub(r"who's", "who is", tweet)
    tweet = re.sub(r"i'm", "i am", tweet)
    tweet = re.sub(r"she's", "she is", tweet)
    tweet = re.sub(r"he's", "he is", tweet)
    tweet = re.sub(r"they're", "they are", tweet)
    tweet = re.sub(r"who're", "who are", tweet)
    tweet = re.sub(r"ain't", "am not", tweet)
    tweet = re.sub(r"wouldn't", "would not", tweet)
    tweet = re.sub(r"shouldn't", "should not", tweet)
    tweet = re.sub(r"can't", "can not", tweet)
    tweet = re.sub(r"couldn't", "could not", tweet)
    tweet = re.sub(r"won't", "will not", tweet)
    tweet = re.sub(r"\W", " ", tweet)
    tweet = re.sub(r"\d", " ", tweet)
    tweet = re.sub(r"\s+[a-z]\s+", " ", tweet)
    tweet = re.sub(r"\s+[a-z]$", " ", tweet)
    tweet = re.sub(r"^[a-z]\s+", " ", tweet)
    tweet = re.sub(r"\s+", " ", tweet)

    tweet_tokens = word_tokenize(tweet)
    filtered_words = [w for w in tweet_tokens if not w in stop_words]

    return " ".join(filtered_words)


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
    "source": lambda x: re.findall('">(.*)</a>', x["source"])[0]
    if x["source"]
    else "null",
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
    "text": lambda x: clean_text(x["text"]),
}