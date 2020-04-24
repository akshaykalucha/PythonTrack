from twilio.rest import Client 
# from Tracker import converted_price
 
account_sid = [YOUR_TWILIO_SID] 
auth_token = [YOUR_TWILIO_AUTH_TOKEN]
client = Client(account_sid, auth_token) 

def send_msg(price):

    message = client.messages.create( 
                                from_='whatsapp:[AUTH_NUMBER],  
                                body=price,      
                                to='whatsapp:+[RECIEVERS_NUMBER]
                            ) 
    
    print(message.sid)
