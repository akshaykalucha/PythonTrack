from aiohttp import request
from flask import Flask
from flask import request
from InstaApp import getInfo
from YouTubeApp import getChInfo

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/getInstaInfo', methods=['GET'])
def sendData():
    args = request.args
    uname = args.get("uname")
    data = getInfo(uname)
    return data

@app.route('/getYTInfo', methods=['GET'])
def sendYTData():
    args = request.args
    cname = args.get("cid")
    data = getChInfo(cname)
    return data


if __name__ == "__main__":
    app.run()