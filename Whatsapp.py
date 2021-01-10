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

def deco(fun):
    def foo(num):
        return fun(num ** 2)
    return foo
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


# @deco
# def square(num):
#     return num**2

# n = square(2)
# print(n)