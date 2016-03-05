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
        print "first t is", timeline[0] # delete
        print "len timeline", len(timeline) #del
        for t in timeline:
            tweet_time = bot.timestr_to_datetime (t['created_at'])
            if tweet_time > self.last_ran:
                print "Retweeting {0}".format(t['id']) 
                # self.api.retweet(id = t['id']) # FIXME uncomment later
            else: #del
                print "none found" #del

if __name__ == "__main__":

    keys_tokens = open('keys_tokens.txt', 'r').read().splitlines()
    
    # The consumer keys can be found on your application's Details
    # page located at https://dev.twitter.com/apps (under "OAuth
    # settings")
    c_key = keys_tokens[0]
    c_secret = keys_tokens[1]

    # The access tokens can be found on your applications's Details
    # page located at https://dev.twitter.com/apps (located under
    # "Your access token")
    a_token = keys_tokens[2]
    a_token_secret = keys_tokens[3]

    # Create an instance of the bot class
    print "verifying..." #del
    twitter = bot(c_key, c_secret, a_token, a_token_secret)
    print "success" #del

    # Retweet anything new by @LinuxUserMag every 5 minutes
    while True:
        # Update the time after each retweet_task so we're 
        # only retweeting new stuff 
        twitter.retweet_task("LinuxUserMag")
        print "returned successfully" #del
        twitter.last_ran = datetime.now()
        time.sleep(5 * 60)
