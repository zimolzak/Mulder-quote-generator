#!/usr/bin/env python2
# A Twitter Bot for the Raspberry Pi that retweets any content from
import sys
import time
from datetime import datetime 
from twython import Twython

class bot:
    def __init__(self, c_key, c_secret, a_token, a_token_secret):
        # Create a Twython API instance
        self.api = Twython(c_key, c_secret, a_token, a_token_secret)
        # Make sure we are authenticated correctly
        try: 
            self.api.verify_credentials()
        except:
            sys.exit("Authentication Failed")
        self.last_ran = datetime.now() 

    @staticmethod
    def timestr_to_datetime(timestr):
        # Convert a string like Sat Nov 09 09:29:55 +0000
        # 2013 to a datetime object. Get rid of the timezone 
        # and make the year the current one
        timestr = "{0} {1}".format(timestr[:19], datetime.now().year)
        # We now have Sat Nov 09 09:29:55 2013
        return datetime.strptime(timestr, '%a %b %d %H:%M:%S %Y')

    def retweet_task(self, screen_name):
        # Retweets any tweets we've not seen 
        # from a user
        print "Checking for new tweets from @{0}".format(screen_name)
        # Get a list of the users latest tweets
        timeline = self.api.get_user_timeline (screen_name = screen_name)
        # Loop through each tweet and check if it was 
        # posted since we were last called
        for t in timeline:
            tweet_time = bot.timestr_to_datetime (t['created_at'])
            if tweet_time > self.last_ran:
                print "Retweeting {0}".format(t['id']) 
                # self.api.retweet(id = t['id']) # FIXME uncomment later

    def tweet_hardcode_msg(self):
        self.api.update_status(status='Our darkest secret will come full circle to all that they have to hide. #thexfiles')

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
