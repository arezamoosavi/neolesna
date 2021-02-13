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

    print("connected Ok!")
    data = api.trends_place(1, "#")
    trends = data[0]["trends"]
    trend_names = "\n".join(trend["name"] for trend in trends)

    print(trend_names)