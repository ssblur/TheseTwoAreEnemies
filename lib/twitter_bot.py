import os
import traceback
from twitter import Api
from time import sleep
from .enemies import get_random_enemy
from . import constants
import threading

def post(api):
    while True:
        try:
            character, enemy = get_random_enemy()
            print('Sending the following tweet:')
            print('\t', constants.twitter_message.format(character = character, enemy = enemy))
            print('With the following media:')
            print('\t', character.image)
            print('\t', enemy.image)
            api.PostUpdate(
                constants.twitter_message.format(character = character, enemy = enemy),
                [
                    character.image,
                    enemy.image
                ])
            break
        except Exception as e:
            print('Ran into an error generating that tweet, let\'s try again...')
            traceback.print_exception(e)

def loop(api):
    while True:
        post(api)
        if constants.once:
            break
        sleep(constants.twitter_period)

def run():
    api = Api(
        consumer_key=constants.twitter_key,
        consumer_secret=constants.twitter_secret,
        access_token_key=constants.twitter_token_key,
        access_token_secret=constants.twitter_token_secret
    )
    threading.Thread(target=loop, args=(api,)).start()
    