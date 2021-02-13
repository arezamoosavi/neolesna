# Twitter API authentication

import tweepy
import json
import settings


def get_twitter_api(settings):
    # authorize the API Key
    authentication = tweepy.OAuthHandler(settings.api_key, settings.api_secret)

    # authorization to user's access token and access token secret
    authentication.set_access_token(settings.access_token, settings.access_token_secret)

    # call the api
    api = tweepy.API(
        authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True
    )

    if api.verify_credentials():
        return api
    else:
        return None


api = get_twitter_api(settings)

if api:
    new_search = "#wildfires" + " -filter:retweets"
    tweets = tweepy.Cursor(api.search, q=new_search, lang="en").items(5)

    for tweet in tweets:

        data = {}
        for key, f in settings.twitter_json_mapping.items():
            data[key] = f(tweet._json)
        print(data["source"], "\n\n\n", data["text"], "\n\n")