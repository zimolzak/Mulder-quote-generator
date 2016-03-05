#!/usr/bin/env python2
import sys
import time
import random
from datetime import datetime, timedelta
from twython import Twython
from mulder import generate_clean_sentence

class bot:
    def __init__(self, c_key, c_secret, a_token, a_token_secret):
        self.api = Twython(c_key, c_secret, a_token, a_token_secret)
        try: 
            self.api.verify_credentials()
        except:
            sys.exit("Authentication Failed")

    def tweet_generated_msg(self):
        sentence = generate_clean_sentence(True) # True means Twitter
        print sentence
        self.api.update_status(status = sentence)

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
        twitter.tweet_generated_msg()
        avg_hours = 0.5
        sleep_sec = random.expovariate(1.0 / avg_hours) * 60 * 60
        print "Done. Next tweet approx", datetime.now() + timedelta(seconds=sleep_sec)
        time.sleep(sleep_sec)
