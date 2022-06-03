import os

once = False
wiki_url = None

discord = False
discord_token = None
discord_message = "{character.name} ( {character.link} ) and {enemy.name} ( {enemy.link} ) are enemies."

twitter = False
twitter_key = None
twitter_secret = None
twitter_token_key = None
twitter_token_secret = None
twitter_message = "{character.name} and {enemy.name} are enemies. (Source: {character.link} and {enemy.link})"
twitter_period = 86400

def initialize_env():
    global wiki_url
    global discord_token, discord_command, discord_message
    global twitter_key, twitter_secret, twitter_token_key, twitter_token_secret, twitter_message, twitter_period
    wiki_url = os.environ['WIKI_URL'] if 'WIKI_URL' in os.environ else wiki_url

    discord_token = os.environ['DISCORD_TOKEN'] if 'DISCORD_TOKEN' in os.environ else discord_token
    discord_command = os.environ['DISCORD_COMMAND'] if 'DISCORD_COMMAND' in os.environ else discord_command
    discord_message = os.environ['DISCORD_MESSAGE'] if 'DISCORD_MESSAGE' in os.environ else discord_message

    twitter_key = os.environ['TWITTER_KEY'] if 'TWITTER_KEY' in os.environ else twitter_key
    twitter_secret = os.environ['TWITTER_SECRET'] if 'TWITTER_SECRET' in os.environ else twitter_secret
    twitter_token_key = os.environ['TWITTER_TOKEN_KEY'] if 'TWITTER_TOKEN_KEY' in os.environ else twitter_token_key
    twitter_token_secret = os.environ['TWITTER_TOKEN_SECRET'] if 'TWITTER_TOKEN_SECRET' in os.environ else twitter_token_secret
    twitter_message = os.environ['TWITTER_MESSAGE'] if 'TWITTER_MESSAGE' in os.environ else twitter_message
    twitter_period = float(os.environ['TWITTER_PERIOD']) if 'TWITTER_PERIOD' in os.environ else twitter_period

def initialize_args(args):
    global once, wiki_url
    global discord, discord_token, discord_command, discord_message
    global twitter, twitter_key, twitter_secret, twitter_token_key, twitter_token_secret, twitter_message, twitter_period
    once = args.once
    wiki_url = args.wiki_url or wiki_url

    discord = args.discord
    discord_token = args.discord_token or discord_token
    discord_message = args.discord_message or discord_message
    
    twitter = args.twitter
    twitter_key = args.twitter_key or twitter_key
    twitter_secret = args.twitter_secret or twitter_secret
    twitter_token_key = args.twitter_token_key or twitter_token_key
    twitter_token_secret = args.twitter_token_secret or twitter_token_secret
    twitter_message = args.twitter_message or twitter_message
    twitter_period = args.twitter_period or twitter_period
    