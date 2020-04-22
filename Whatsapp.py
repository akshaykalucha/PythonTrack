from twilio.rest import Client 
# from Tracker import converted_price
 
account_sid = 'AC28aae9205d1514633e8ea129436a9bb6' 
auth_token = '7cb6c719f1b57f49651250da2fc50954' 
client = Client(account_sid, auth_token) 

def send_msg(price):

    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body=price,      
                                to='whatsapp:+919873835100'
                            ) 
    
    print(message.sid)