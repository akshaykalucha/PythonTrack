import smtplib
import os
from email.message import EmailMessage
import filetype
# from secrets import EMAIL_PASSWORD, EMAIL_ADDRESS


EMAIL_ADDRESS = os.environ['EMAIL_ADDRESS']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']
# Access_token = os.environ['Access_token']
# Access_Token_Secret = os.environ['Access_Token_Secret']


def send_video_mail(fn):

    msg = EmailMessage()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)


    msg['Subject'] = 'Here is the Twitter video you requested for'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'akshaykalucha@gmail.com'
    msg.set_content("Find the video attached")

    ddir = './videos/'
    op_dir = os.path.join(ddir, fn)
    with open(op_dir, 'rb') as f:
        file_data = f.read()
        file_type = filetype.guess_extension(op_dir)
    
    msg.add_attachment(file_data, maintype='video', subtype=file_type, filename=fn)

    server.send_message(msg)
    print('Hey email sent')
    server.quit

    