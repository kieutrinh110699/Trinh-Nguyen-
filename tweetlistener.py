# tweetlistener.py
"""tweepy.StreamListener subclass that processes tweets as they arrive."""
import tweepy
from tweepy import Stream
from textblob import TextBlob

class TweetListener(tweepy.Stream):
    """Handles incoming Tweet stream."""
    
    def __init__(self, consumer_key, consumer_secret, access_token,access_token_secret, limit=10):
        """Create instance variables for tracking number of tweets."""
        self.tweet_count = 0
        self.TWEET_LIMIT = limit
        super().__init__(consumer_key, consumer_secret, access_token, access_token_secret)  # call superclass's init
    
    def on_connect(self):
        """Called when your connection attempt is successful, enabling 
        you to perform appropriate application tasks at that point."""
        print('Connection successful\n')
    
    def on_status(self, status):
        """Called when Twitter pushes a new tweet to you."""
        # get the tweet text
        try:  
            tweet_text = status.extended_tweet.full_text
        except: 
            tweet_text = status.text
        print(self.tweet_count)
        print(f'Screen name: {status.user.screen_name}:')
        print(f'   Language: {status.lang}')
        print(f'     Status: {tweet_text}')
    
        #if status.lang != 'en':
        #    print(f' Translated: {TextBlob(tweet_text).translate()}')

        print()
        self.tweet_count += 1  # track number of tweets processed

        # if TWEET_LIMIT is reached, return False to terminate streaming
        if self.tweet_count >= self.TWEET_LIMIT:
            self.disconnect()