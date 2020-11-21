#!/bin/env python
"""
Discord Bot
A shell for Disney Enemies
"""
import discord, os
from .enemies import get_random_enemy

class EnemyClient(discord.Client):
    async def on_message(self, message):
        if message.content.startswith(os.environ['DISCORD_COMMAND']):
            query = ' '.join(message.content.split(' ')[1:]).strip();
            character, enemy = get_random_enemy(query)
            if character:
                print("Sending the following message:")
                print('\t', os.environ['DISCORD_MESSAGE'].format(character = character, enemy = enemy))
                await message.channel.send(os.environ['DISCORD_MESSAGE'].format(character = character, enemy = enemy))
            else:
                out = f"Could not find a {query} with any enemies."
                print(out)
                await message.channel.send(out)

def run():
    client = EnemyClient()
    client.run(os.environ['DISCORD_TOKEN'])

if __name__ == "__main__":
    run()