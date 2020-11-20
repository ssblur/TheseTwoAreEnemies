import twitter, os

def run():
    api = twitter.Api(consumer_key=os.environ['TWITTER_KEY'],
        consumer_secret=os.environ['TWITTER_SECRET'],
        access_token_key=os.environ['TWITTER_TOKEN_KEY'],
        access_token_secret=os.environ['TWITTER_TOKEN_SECRET'])