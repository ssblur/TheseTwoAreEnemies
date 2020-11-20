import twitter, os
from time import sleep
from enemies import get_random_enemy

def post(api):
    while True:
        try:
            character, enemy = get_random_enemy()
            print('Sending the following tweet:')
            print('\t', os.environ['TWITTER_MESSAGE'].format(character = character, enemy = enemy))
            print('With the following media:')
            print('\t', character.image)
            print('\t', enemy.image)
            api.PostUpdate(
                os.environ['TWITTER_MESSAGE'].format(character = character, enemy = enemy),
                [
                    character.image,
                    enemy.image
                ])
            break
        except Exception:
            print('Ran into an error generating that tweet, let\'s try again...')

def run():
    api = twitter.Api(consumer_key=os.environ['TWITTER_KEY'],
        consumer_secret=os.environ['TWITTER_SECRET'],
        access_token_key=os.environ['TWITTER_TOKEN_KEY'],
        access_token_secret=os.environ['TWITTER_TOKEN_SECRET'])
    while True:
        post(api)
        sleep(int(os.environ['TWITTER_PERIOD']))