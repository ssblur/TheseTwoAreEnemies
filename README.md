# These Two Are Enemies
**A Multi-Platform Bot**

Have you ever wanted to know two random wiki characters that may consider each other enemies? Well, you can anyways.


## Getting Started
To start, you will need to copy .env.example to .env to begin configuration. You can also change WIKI_URL to any valid Fandom / Wikia URL to determine where to pull enemies from, though this bot will only work on those where enemies is a valid/present data-source (like the default, the Disney fandom wiki).

## Discord

### Installation
In your .env set DISCORD_TOKEN to a Discord bot token. [Instructions on how to do so.](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token)

You can also use the opportunity to change your command or the content of the message if you'd like.

### Usage
You can launch the Discord bot by launching the module with the 'discord' option (e.g. `python . --discord`)

Once this is done, create a bot invite like, invite the bot to your server, and use the '!enemies' command (or whatever you have set your command to) in any channel the bot can see and send messages to.

## Twitter

### Installation
In your .env you will need to set the TWITTER_KEY and TWITTER_SECRET to your app's key and secret, then generate and set your token key and secret with TWITTER_TOKEN_KEY and TWITTER_TOKEN_SECRET. 

You can also take this time to change the message to tweet and the amount of seconds between tweets.

### Usage
You can launch the Twitter bot by launching the module with the 'twitter' option (e.g. `python . --twitter`)

The Twitter section supports the --once argument. If provided, it will post a Tweet and then end.

This bot will automatically tweet once every TWITTER_PERIOD seconds (+processing time) with a random pair of enemies to the account the token key and secret are associated with. It has no prevention against sending the same enemies more than once, so it may repeat occasionally.

## Arguments
You can get more info on arguments with the 'help' option (e.g. `python . --help`)

Providing the lowercase kebab-case version of any Environment Variable will overwrite that variable. This can be used to set keys or such in the command line.

Some modes support the 'once' option (e.g. `python . --twitter --once`) to execute once instead of waiting. Currently only the Twitter mode supports 'once'.