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

    new_search = "iran -filter:retweets"
    tweets = tweepy.Cursor(
        api.search, q=new_search, result_type="recent", include_entities=True, lang="en"
    ).items(50)

    file1 = open("res_data.txt", "w+")

    for tweet in tweets:
        print("new tweet!")
        data = {}
        for key, func in settings.twitter_json_mapping.items():
            data[key] = func(tweet._json)

        file1.write(f'{data["source"]} - {data["name"]} - {data["text"]} \n\n')
    file1.close()