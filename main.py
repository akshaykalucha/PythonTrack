import tweepy
import time
import json
from keys import authkey, authPass, Access_token, Access_Token_Secret

#auth
auth = tweepy.OAuthHandler(authkey, authPass)

auth.set_access_token(Access_token, Access_Token_Secret)

#accessing my profile after auth
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#my twitter name
user = api.me()
print(user.screen_name)


#get user and print mutual followers
'''
user2 = api.get_user('Chiragbarjatyaa')
print(user2.screen_name)
print(user2.followers_count)
for friend in user2.friends():
    print(friend.screen_name)
    '''

    #getting page of a person
'''
for page in tweepy.Cursor(api.user_timeline, id="Chiragbarjatyaa").pages():
    # page is a list of statuses
    process_page(page)
    '''

#printing my followers tweets
'''
for follower in tweepy.Cursor(api.followers).items():
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)
        '''


#Searching specific hashtag and liking everytweet

'''
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
    '''

# retweets the tweet with given id
'''print(api.retweet(1267756223220203521).text)'''

#returns tweets on my page from what to where
'''print(api.home_timeline(1267756223220203521, 1267804296483086337, 1))'''

#returns status of tweet
'''print(api.get_status(1267756223220203521).text)'''

#update status/ tweeting / Replying
#tweet ID
'''
tweetid = 1267856481258520577
print(api.update_status("+1💫", in_reply_to_status_id=tweetid, auto_populate_reply_metadata=True))
'''


'''print(api.update_with_media('./mylogo.png', "another targeted tweet", 1267369665828777984, source="https://miro.medium.com/max/1000/1*cXlPOwhc6A3Skp9GQ1gVFQ.png"))'''

#Tweets on my timeline
'''
timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")
    '''


#Simple search in twitter
'''
for tweet in api.search(q="lifeofakshy", lang="en", rpp=10):
    print(f"{tweet.user.name}:{tweet.text}")
    '''


### CREATIG A STREAM

class MySTreamListner(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.txt}")

    def on_error(self,status):
        print('Error Detected')


tweets_listner = MySTreamListner(api)

stream = tweepy.Stream(api.auth, tweets_listner)
print(stream.filter(track=["lifeofakshy"], languages=["en"]))