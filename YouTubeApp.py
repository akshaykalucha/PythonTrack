from googleapiclient.discovery import build
import json 

# UCJSzwLMy_0yDvVVtMxWzRcg

def getChInfo(channelID):

    youtube = build('youtube', 'v3',
                    developerKey='AIzaSyC59EjyfGfTapw8F4HHY7zBsiOOcV2M7ho')
    ch_request = youtube.channels().list(
        part='statistics', id=f"{channelID}")

    ch_response = ch_request.execute()
    userDict = {}
    try:
        userDict["totalSubs"] = ch_response['items'][0]['statistics']['subscriberCount']
        userDict["totalVids"] = ch_response['items'][0]['statistics']['videoCount']
        userDict["totalViews"] = ch_response['items'][0]['statistics']['viewCount']
        json_object = json.dumps(userDict, indent = 4) 
        return json_object
    except:
        return "channel not found"

print(getChInfo("UCJSzwLMy_0yDvVVtMxWzRcg"))