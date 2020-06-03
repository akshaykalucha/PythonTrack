import tweepy
import time
from secrets import authkey, authPass, Access_token, Access_Token_Secret


auth = tweepy.OAuthHandler(authkey, authPass)

auth.set_access_token(Access_token, Access_Token_Secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()
print(user.screen_name)

# for follower in tweepy.Cursor(api.followers).items():


search = '#100DaysOfCode'

nuTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nuTweets):
    try:
        print("Tweet Liked")
        tweet.favorite()
        time.sleep(1)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
