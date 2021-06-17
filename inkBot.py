'''
INFO:
1. WHAT IS THIS BOT?
This is inkBot, a bot made by Adi#1874 to assist in server featues for which finding a bot is too hard or unnsesary

2. WHAT IS THIS FILE?
This is the main file that is like the hub to all code, here is where the bot prefix is determined, cogs are loaded and bot is run throught the token



IMPORTS:
1. discord cause idk
2. commands module for running bot functions and calling commands
3. load to load my token
4. os to read /cogs/ and automatically load in all cogs 
5. path to show the path to my json
'''
import discord
from discord.ext import commands
from json import load
import os
from pathlib import Path

allowed_mentions = discord.AllowedMentions(everyone=False,roles=False)

intents = discord.Intents.default()
intents.members = True
#defining the bot,removing help command, disabling everyone and role mentions
client = commands.Bot(command_prefix = ['ink ', 'ink', 'Ink ','Ink'], intents = intents,status=discord.Status.do_not_disturb,activity=discord.Game(name="ink help"))
client.allowed_mentions = allowed_mentions
client.remove_command('help')

#
#Loading message
@client.event
async def on_ready():
    print('Bot is online!')

#removing need for underscores in using jsk
os.environ['JISHAKU_NO_UNDERSCORE'] = 'true'


#making a list of all cogs in the cogs folder
myCogs = []
cogsFolderStuff = os.listdir('./cogs/')
for file in cogsFolderStuff:
    if file.endswith('.py'):
        fileName = file.split('.')
        myCogs.append(str('cogs.' + fileName[0]))


#loading my cogs as defined in previous step
if __name__ == '__main__':
    for ext in myCogs:
        client.load_extension(ext)


#loading jishaku seperately cause its weird
client.load_extension('jishaku')


#reading my json file
with Path("utils/secrets.json").open() as f:
    config = load(f)
token = config["token"]


#Running client on token given
client.run(token)