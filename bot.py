#!/usr/bin/env python2
import sys
import time
import random
from datetime import datetime, timedelta
from twython import Twython, TwythonError
from mulder import generate_clean_sentence

class TwythonKnownError(TwythonError):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

class bot:
    def __init__(self, c_key, c_secret, a_token, a_token_secret):
        self.api = Twython(c_key, c_secret, a_token, a_token_secret)
        self.api.verify_credentials()

    def tweet_generated_msg(self):
        sentence = generate_clean_sentence(True) # True means Twitter
        print sentence
        try: # Split into generic/specific TwythonError. No real err handling.
            self.api.update_status(status = sentence)
        except TwythonError as err:
            e = str(err)
            if 'Read timed out' in e or 'reset by peer' or 'retries exceeded' in e:
                # here's a new one:
                # twython.exceptions.TwythonError:
                # EOF occurred in violation of protocol (_ssl.c:590)
                #
                # twython.exceptions.TwythonError:
                # HTTPSConnectionPool(host='api.twitter.com',
                # port=443): Max retries exceeded with url:
                # /1.1/statuses/update.json (Caused by <class
                # 'socket.error'>: [Errno 110] Connection timed out)
                raise TwythonKnownError(e)
            else:
                raise TwythonError(e)

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

    n_tries = 0
    max_tries = 2
    while True:
        avg_hours = 1.0
        sleep_sec = random.expovariate(1.0 / avg_hours) * 60 * 60
        while sleep_sec <= 50:
            sleep_sec = random.expovariate(1.0 / avg_hours) * 60 * 60
        assert sleep_sec > 50 # safety valve
        print "tweeting..."
        try:
            n_tries += 1
            twitter.tweet_generated_msg()
        except TwythonKnownError as err:
            print "Try {} of {} failed.\n    [{}]".format(n_tries, max_tries,
                                                          str(err))
            if n_tries < max_tries:
                sleep_sec = 10
            else:
                raise TwythonKnownError(str(err))
        else:
            print "Done.",
            n_tries = 0
        print ("Next tweet approx " +
               str(datetime.now() + timedelta(seconds=sleep_sec)) + "\n")
        time.sleep(sleep_sec)
