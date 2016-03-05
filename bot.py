#!/usr/bin/env python2
import sys
import time
from datetime import datetime 
from twython import Twython

class bot:
    def __init__(self, c_key, c_secret, a_token, a_token_secret):
        self.api = Twython(c_key, c_secret, a_token, a_token_secret)
        try: 
            self.api.verify_credentials()
        except:
            sys.exit("Authentication Failed")
        self.last_ran = datetime.now() 

    def tweet_hardcode_msg(self):
        self.api.update_status(status='A lie will be confronted by someone who reveals the truth. #thexfiles')

if __name__ == "__main__":

    keys_tokens = open('keys_tokens.txt', 'r').read().splitlines()
    # Consumer key & secret, access token & secret,
    # usually found at https://dev.twitter.com/apps
    c_key = keys_tokens[0]
    c_secret = keys_tokens[1]
    a_token = keys_tokens[2]
    a_token_secret = keys_tokens[3]

    print "login..."
    twitter = bot(c_key, c_secret, a_token, a_token_secret)
    print "done"

    while True:
        print "tweeting..."
        twitter.tweet_hardcode_msg()
        print "done"
        twitter.last_ran = datetime.now()
        time.sleep(5 * 60)
