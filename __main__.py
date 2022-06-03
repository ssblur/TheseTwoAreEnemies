#!/bin/env python
"""
These Two Are Enemies
A set of bots which tell you about some enemies on wikis of your choice.
"""
import sys
from lib import constants, discord_bot, twitter_bot
from dotenv import load_dotenv
import argparse

load_dotenv()

parser = argparse.ArgumentParser(description='Run the These Two are Enemies Bot')
parser.add_argument('--once', action='store_true', help='If the Mode supports it, run this once and exit')
parser.add_argument('--wiki-url', action='store', help='Set the wiki URL to poll from. Overrides values specified in env')

parser.add_argument('--discord', action='store_true', help='Run this bot in Discord Mode')
parser.add_argument('--discord-token', action='store', help='Set the Discord token to use. Overrides values specified in env')
parser.add_argument('--discord-message', action='store', help='Set the format of the message to send to Discord. Overrides values specified in env')

parser.add_argument('--twitter', action='store_true', help='Run this bot in Twitter Mode')
parser.add_argument('--twitter-key', action='store', help='Set the Twitter key to use. Overrides values specified in env')
parser.add_argument('--twitter-secret', action='store', help='Set the Twitter secret to use. Overrides values specified in env')
parser.add_argument('--twitter-token-key', action='store', help='Set the Twitter token key to use. Overrides values specified in env')
parser.add_argument('--twitter-token-secret', action='store', help='Set the Twitter token secret to use. Overrides values specified in env')
parser.add_argument('--twitter-message', action='store', help='Set the format of the message to send to Twitter. Overrides values specified in env')
parser.add_argument('--twitter-period', action='store', help='Set the period of time to wait between posts. Does not apply if --once is enabled. Overrides values specified in env')

args = parser.parse_args()
constants.initialize_env()
constants.initialize_args(args)

if __name__=='__main__':
    tasks = []
    # Was originally going to aggregate with asyncio, but I don't want to try to make that compatible with discord.js.
    if constants.twitter:
        twitter_bot.run()
    if constants.discord:
        discord_bot.run()