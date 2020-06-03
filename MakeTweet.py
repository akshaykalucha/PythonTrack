import tweepy
import logging
from config import main_api
import json

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()

class MakeTweet:
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def make_tweet(self, tweetBody):
        logger.info(f"Processing tweet {tweetBody}")
        try:
            tweet = self.api.update_status(status=tweetBody)
            print(f"successfully tweeted following: {tweetBody}")
        except Exception as e:
            logger.error("Error on tweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)


def execTweet(keywords):
    api = main_api()
    tweet_maker = MakeTweet(api)
    try:
        tweet__done = tweet_maker.make_tweet(keywords)
        return tweet__done
    except:
        return tweet_maker.on_error()

if __name__ == "__main__":
    print("this is test tweet from akshay")