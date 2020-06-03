from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from Tracker import check_price
import json
from MakeTweet import execTweet
# from scheduler import start_sending

app = Flask(__name__)

# price = check_price()
# if price>1:
#     price = [str(price)]
#     print('yes')
#     start_sending()

@app.route("/")
def hello():
    return "Hello, World!"

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
        print(len(z))
        body = z["body"]
        if z["type"]["kind"] == "simple":
            print("it is a simple tweet")
            print(f"body is: {body}")
            try:
                execTweet(body)
                resp.message(f"Lmao you made the following tweet: {body}")
            except:
                resp.message("Lmao there was a error please try again")
        elif z["type"]["kind"] == "reply":
            print("it is a reply tweet")
            try:
                replyId = z["type"]["replyID"]
            except:
                print("No tweet id given")
                return
            print(f"replying to {replyId}")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)