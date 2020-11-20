#!/bin/env python
"""
Discord Bot
A shell for Disney Enemies
"""
import discord, os
from enemies import get_random_enemy

class EnemyClient(discord.Client):
    async def on_message(self, message):
        if message.content.startswith(os.environ['DISCORD_COMMAND']):
            character, enemy = get_random_enemy(' '.join(message.content.split(' ')[1:]).strip())
            print("Sending the following message:")
            print('\t', os.environ['DISCORD_MESSAGE'].format(character = character, enemy = enemy))
            await message.channel.send(os.environ['DISCORD_MESSAGE'].format(character = character, enemy = enemy))

def run():
    client = EnemyClient()
    client.run(os.environ['DISCORD_TOKEN'])

if __name__ == "__main__":
    run()