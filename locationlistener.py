# locationlistener.py
"""Receives tweets matching a search string and stores a list of
dictionaries containing each tweet's screen_name/text/location."""
import tweepy
from tweetutilities import get_tweet_content

class LocationListener(tweepy.Stream):
    """Handles incoming Tweet stream to get location data."""

    def __init__(self, consumer_key, consumer_secret, access_token,access_token_secret, limit=10):
        """Configure the LocationListener."""
        self.tweet_count = 0
        self.tweets_list = []
        self.counts_dict = counts = {'total_tweets': 0, 'locations': 0}
        self.TWEET_LIMIT = limit
        super().__init__(consumer_key, consumer_secret, access_token,access_token_secret)  # call superclass's init

    def on_status(self, status):
        """Called when Twitter pushes a new tweet to you."""
        # get each tweet's screen_name, text and location
        tweet_data = get_tweet_content(status, location=True)  

        self.counts_dict['total_tweets'] += 1  # original tweet

        # ignore tweets with no location 
        if not status.user.location:  
            return

        self.counts_dict['locations'] += 1  # tweet with location
        self.tweets_list.append(tweet_data)  # store the tweet
        print(f'{status.user.screen_name}: {tweet_data["text"]}\n')

        # if TWEET_LIMIT is reached, return False to terminate streaming
        self.tweet_count += 1
        if self.tweet_count >= self.TWEET_LIMIT:
            self.disconnect()



##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
