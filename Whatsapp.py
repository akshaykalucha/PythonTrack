from twilio.rest import Client 
# from Tracker import converted_price
import os
account_sid = os.environ['account_sid_key']
auth_token = os.environ['auth_token_key'] 
client = Client(account_sid, auth_token) 

def send_msg(price):

    message = client.messages.create( 
                                from_='whatsapp: twilio number',  
                                body=price,      
                                to='whatsapp: recievers number'
                            ) 
    
    print(message.sid)