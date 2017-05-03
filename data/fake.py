#!/usr/bin/env python

from __future__ import print_function

import time

import twitter
import json

config = json.loads(open('config.json').read())

api = twitter.Api(consumer_key=config['TWITTER_CONSUMER_KEY'],
        consumer_secret=config['TWITTER_CONSUMER_SECRET'],
        access_token_key=config['TWITTER_ACCESS_TOKEN_KEY'],
        access_token_secret=config['TWITTER_ACCESS_TOKEN_SECRET']
        )


fpath = 'fake.txt'
max_id = None
with open(fpath, 'a+') as f:
        for i in range(200):
                tweets = api.GetSearch('#fake', count=200, max_id=max_id)

                if len(tweets) < 1:
                        break

                for status in tweets:
                        try:
                                text = '\n\n\n' + status.text

                                print(text, file=f)
                                print(text)
                        except:
                                continue
                        
                        if not max_id:
                                max_id = status.id - 1
                        elif status.id < max_id:
                                max_id = status.id - 1

                time.sleep(1)
