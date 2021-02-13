import json
import settings

import tweepy
from tweepy.streaming import StreamListener


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


class MyStreamListener(StreamListener):
    def on_data(self, tweet):
        file1 = open("res_data.txt", "a+")

        tweet = json.loads(tweet)
        if tweet.get("id", None) is None:
            return None

        data = {}
        for key, func in settings.twitter_json_mapping.items():
            data[key] = func(tweet)
        file1.write(f'\n\n {data["source"]} -\n {data["name"]} -\n {data["text"]}\n\n')
        file1.close()

        return True

    def on_error(self, status):
        if status == 420:
            print(
                "Enhance Your Calm; The App Is Being Rate Limited For Making Too Many Requests"
            )
            return True
        else:
            print("Error {}".format(status))
            return True


if api:

    print("connected Ok!")

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(
        auth=api.auth, listener=myStreamListener, tweet_mode="extended"
    )
    myStream.filter(languages=["en"], track=["trump", "biden"], is_async=True)
