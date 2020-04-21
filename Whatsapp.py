from twilio.rest import Client 
 
account_sid = 'AC28aae9205d1514633e8ea129436a9bb6' 
auth_token = '7cb6c719f1b57f49651250da2fc50954' 
client = Client(account_sid, auth_token) 

def send_msg():
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='this is test message',      
                                to='whatsapp:+919873835100' 
                            ) 
    
    print(message.sid)