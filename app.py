from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from Tracker import check_price
from scheduler import start_sending

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
    resp.message("Hi this is your own python bot to check the rate of gaming pc graphics card")

    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    print(msg)
    if msg == "prices":
        # Create reply
        GCPrice = check_price()
        New_Price = str(GCPrice)
        resp.message("Prize of graphic card is {}".format(New_Price))
    else:
        resp.message("please send the keyword 'prices' to get price of graphics card")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)