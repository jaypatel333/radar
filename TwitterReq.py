import tweepy
import json
from tweepy import OAuthHandler

consumer_key = 'WdeNFdEiamWTrcy0EjB6kYuQj'
consumer_secret = 'b7SB2jJRLVMw1Fwn7qCGbLyBkwsjLvKApyUeAzTPRvoKxEFsBG'
access_token = '1097989063452356608-GAPBfgZFBTl2Qr95sdQA7iUqCny2VV'
access_secret = 'TKgf5eBGjPUlpLuQ6RuZBVZ2pmktlbIJe5rSdj4qIKQHi'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

USA_WOE_ID = 23424977

usa_trends = api.trends_place(USA_WOE_ID)

trends = json.loads(json.dumps(usa_trends, indent=1))

hashtags = [trend['name'] for trend in trends[0]['trends'] if trend['name'].startswith('#')]

for hashtag in hashtags:
    print(hashtag.lstrip("#"))

from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import re