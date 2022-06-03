#!/bin/env python
"""
Discord Bot
A shell for Disney Enemies
"""
import discord, os
from .enemies import get_random_enemy
from . import constants

class EnemyClient(discord.Client):
    async def on_message(self, message):
        if message.content.startswith(constants.discord_command):
            query = ' '.join(message.content.split(' ')[1:]).strip();
            character, enemy = get_random_enemy(query)
            if character:
                print("Sending the following message:")
                print('\t', constants.discord_message.format(character = character, enemy = enemy))
                await message.channel.send(constants.discord_message.format(character = character, enemy = enemy))
            else:
                out = f"Could not find a {query} with any enemies."
                print(out)
                await message.channel.send(out)

def run():
    client = EnemyClient()
    client.run(constants.discord_token)