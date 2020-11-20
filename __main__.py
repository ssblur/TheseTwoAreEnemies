#!/bin/env python
"""
These Two Are Enemies
A set of bots which tell you about some enemies on wikis of your choice.
"""
import sys, discord_bot, twitter_bot
from dotenv import load_dotenv
load_dotenv()

if __name__=='__main__':
    tasks = []
    # Was originally going to aggregate with asyncio, but I don't want to try to make that compatible with discord.js.
    if 'discord' in sys.argv:
        discord_bot.run()
    elif 'twitter' in sys.argv:
        twitter_bot.run()