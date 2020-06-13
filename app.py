from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from Tracker import check_price
from flask_restful import Resource, Api
from timeout import startThread, t, cancelThread, startTweetTracker, stopTweetTracker
import json
from MakeTweet import execTweet
# from scheduler import start_sending

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        dic = {
        "Type": "Success",
        "Message": "Response sbmitted",
        "Data": None
        }
        return dic, 201

api.add_resource(HelloWorld, '/')

# @app.route("/")
# def hello():
    # dic = {
    #     "Type": "Success",
    #     "Message": "Response sbmitted",
    #     "Data": None
    # }
#     return Response(data=dic, status=status.HTTP_200_OK)

@app.route("/sms", methods=['POST'])
def sms_reply():

    resp = MessagingResponse()
    resp.message("My whatsapp bot working...")

    """Respond to incoming calls with a simple text message."""


    # Fetch the message
    msg = request.form.get('Body')
    # print(msg)
    if msg == "prices":
        # Create reply
        GCPrice = check_price()
        New_Price = str(GCPrice)
        resp.message("Prize of graphic card is {}".format(New_Price))
    elif msg == 'send direct':
        from scheduler import start_sending
        start_sending()
    elif msg == "tweet":
        print(type(msg))
    else:
        z = json.loads(msg)
        print(type(z), 'main type....')
        print(len(z))
        body = z["body"]
        if z["type"]["kind"] == "simple":
            print("it is a simple tweet")
            print(f"body is: {body}")
            try:
                execTweet(body, "simple")
                resp.message(f"Lmao you made the following tweet: {body}")
            except:
                resp.message("Lmao there was a error please try again")


        elif z["type"]["kind"] == "reply":
            print("it is a reply tweet")
            try:
                replyId = z["type"]["replyID"]
                execTweet(body, "reply", replyId)
                resp.message(f"Lmao you made the following REPLY: {body} to {replyId}")
            except:
                print("No tweet id given")
                return
            print(f"replying to {replyId}")


        elif z["type"]["kind"] == "start":
            startThread()

        elif z["type"]["kind"] == "stop":
            print('cancelling the process.....')
            print(t)
            cancelThread()
            print(t)

        elif z["type"]["kind"] == "track-like":
            try:
                userName = z['type']['userName']
                userTweet = z['type']['sinceTweet']
                tweets = startTweetTracker(userName, userTweet)
                print("liking tweet.......")
                resp.message("tweet liked")
            except:
                resp.message("Sory an error occured please try again with corrected values..")
        elif z["type"]["kind"] == "stop-track-like":
            print("cancelling liking process.....")
            stopTweetTracker()
            resp.message("stopped liking process")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)