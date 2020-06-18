import sys,json,re,shutil,os.path,logging,argparse
from datetime import datetime
import requests
from colorama import init,Fore,Style
import time


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
        message = f"file Successfully saved as {fn}"
        return message




def saveVideo(url, *filename):
    z = DownloadVid(url)
    file = z.save_video(*filename)
    return file
    


# saveVideo("https://twitter.com/nailainayat/status/1272919473792651271")

#https://twitter.com/ishanali101/status/1229445162662846465