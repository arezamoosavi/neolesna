# Twitter API authentication

import tweepy
import json
import settings

# authorize the API Key
authentication = tweepy.OAuthHandler(settings.api_key, settings.api_secret)

# authorization to user's access token and access token secret
authentication.set_access_token(settings.access_token, settings.access_token_secret)

# call the api
api = tweepy.API(
    authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True
)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

public_tweet = api.home_timeline(count=300)

for tweet in public_tweet:
    # print(tweet._json)
    print(tweet.source, "\n")