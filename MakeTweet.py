import tweepy
import logging
from config import main_api
import json
from SaveVid import saveVideo


recentId = None

mentionedId = None

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()

mention_chache = {}
id_cache = {}


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



    def make_reply(self,  tweetBody, replyId):
        logger.info(f"Replying tweet {tweetBody} to {replyId}")
        try:
            tweet = self.api.update_status(status=tweetBody, in_reply_to_status_id=replyId, auto_populate_reply_metadata=True)
            print(f"Successfully replied given tweet {tweetBody} to {replyId}")
        except Exception as e:
            logger.error("Error on tweet", exc_info=True)


    def trackUser(self, user_id, since_id):
        global recentId
        print(since_id, "this is Normal id")
        Oldtweets = self.api.user_timeline(id=user_id, since_id=since_id, count=5)
        recentId = Oldtweets[0]._json["id"]
        if "recentID" in id_cache:
            print('recent id found')
            since_id = id_cache["recentID"]
        tweets = self.api.user_timeline(id=user_id, since_id=since_id, count=5)
        print(since_id, "this is most recent updated id")
        # changeTweetId(recentId)
        tweetLiked = []
        for tweet in tweets:
            tweet_data = tweet._json
            if tweet_data["retweeted"] == True:
                pass
                # print(f"you reetweeted this: {tweet_data['text']}")
            try:
                isQuoted = tweet_data['quoted_status']
            except:
                isQuoted = None
            if tweet_data['in_reply_to_status_id'] == None \
                and isQuoted == None \
                and tweet_data['retweeted'] == False:
                if not tweet.favorited:
                    tweet.favorite()
                    id_cache["recentID"] = recentId
                    tweetLiked.append(tweet_data['text'])
        return tweetLiked
            # if tweet_data["id"] > since_id:
            # print(tweet_data['id'], 'this is liked id')


    def mention_reply(self, since_id=None):
        global mentionedId
        if "mentions_id" in mention_chache:
            since_id = mention_chache["mentions_id"]
            print(since_id)
            print("recent Id foud")
        mentioned_tweets = self.api.mentions_timeline(count=1, since_id=since_id)
        mentionedId = mentioned_tweets[0]._json['id']
        print(since_id, "this is gone to api")
        for mentions in mentioned_tweets:
            tweetData = mentions._json
            # print(tweetData['user']['screen_name'])
            myHandle = tweetData['user']['screen_name']
            if myHandle == "lifeofakshy2" or myHandle=="lifeofakshy":
                tweetText = tweetData['text'].split(' ')
                # print(tweetText)
                for text in tweetText:
                    if text=="sendStatus":
                        print("yes word exists")
                        tweet_status_id = tweetData["in_reply_to_status_id"]
                        main_tweet_id = tweetData["id"]
                        print(main_tweet_id)
                        # print(tweet_status_id)
                        original_tweet = self.api.get_status(tweet_status_id)
                        tweetedBy = original_tweet._json['user']['screen_name']
                        tweet_url = original_tweet._json['id_str']
                        # print(tweet_url, "this is tweetId")
                        constructed_url = f"https://twitter.com/{tweetedBy}/status/{tweet_url}"
                        print(constructed_url)
                        videoSaved = saveVideo(f"{constructed_url}")
                        mention_chache["mentions_id"] = mentionedId
                        # print(mention_chache, "this is recent id")
                        self.api.update_status(status="StatusSent", in_reply_to_status_id=main_tweet_id)
                        return videoSaved
            print("sorry this was not save video mention")

    def on_error(self, status):
        logger.error(status)



def startSavingReplying():
    api = main_api()
    tweet_maker = MakeTweet(api)
    videoMessage = tweet_maker.mention_reply()
    return videoMessage

def execTweet(keywords, type, *replyId):
    api = main_api()
    tweet_maker = MakeTweet(api)
    try:
        if type == "simple":
            tweet__done = tweet_maker.make_tweet(keywords)
            return tweet__done
        if type == "reply":
            print("executing reply tweet....")
            tweet__done = tweet_maker.make_reply(keywords, *replyId)
            return tweet__done
    except:
        return tweet_maker.on_error()




def trackTweet(userId, sinceTweet):
    api = main_api()
    tweet_tracker = MakeTweet(api)
    try:
        tweetByUser = tweet_tracker.trackUser(userId, sinceTweet)
        return tweetByUser
    except:
        return tweet_tracker.on_error()



class LikeTweet(tweepy.StreamListener):

    def __init__(self, api):
        self.api = api
        self.me = api.me()


    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet}")
        print(f"{tweet.user.name}:{tweet}")
        if tweet.in_reply_to_status_id is not None or tweet.user.id == self.me.id:
            return
        if not tweet.favorited:
            try:
                print("tweet liked")
            except Exception as e:
                logger.error("Error on fav", exc_info=True)

    def on_error(self, status):
        print("Error detected")




# def tweetListner():
#     api = main_api()
#     tweets_listener = LikeTweet(api)
#     stream = tweepy.Stream(api.auth, tweets_listener)
#     stream.filter(track=["squintneon"])


# tweetListner()



# api = main_api()

# z=api.get_status(1229445162662846465)
# print(z)






if __name__ == "__main__":
    print("this is test tweet from akshay")