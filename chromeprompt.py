from selenium import webdriver
from random import choice
from webdriver_manager.chrome import ChromeDriverManager
import zipfile,os
from selenium import webdriver
from time import sleep
from selenium import webdriver
import os
from bs4 import BeautifulSoup
import requests
from random import choice
from webdriver_manager.chrome import ChromeDriverManager
import praw
import pprint
import random
import requests
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import json
from proxydriver import get_chromedriver
from fake_useragent import UserAgent
 
ua = UserAgent()
userAgent = ua.random

src = 'https://stackoverflow.com/questions/55582136/how-to-set-proxy-with-authentication-in-selenium-chromedriver-python'


manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
        singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
        },
        bypassList: ["localhost"]
        }
    };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)

def get_chromedriver(use_proxy=False, user_agent=None):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    if use_proxy:
        pluginfile = 'proxy_auth_plugin.zip'
        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json",  manifest_json)
            zp.writestr("background.js", background_js)
        chrome_options.add_extension(pluginfile)
    if user_agent:
            chrome_options.add_argument('--user-agent=%s' % user_agent)
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
    return driver