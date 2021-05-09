#importing the discord package
import discord
from discord.ext import commands
import random
import time
import varsToNotCopy
from discord.ext.commands import MemberNotFound
import os

# Client (my bot)
client = commands.Bot(command_prefix = ['ink ', 'ink', 'Ink ','Ink'])
client.remove_command('help')


#message sent in bot status when bot comes on
@client.event
async def on_ready():
    print('bot is online')

#message sent in bot status when bot goes down
@client.event
async def on_disconnect():
    print('bot is now going offline')

#defining my cogs
myCogs = []
cogsFolderStuff = os.listdir('./cogs/')
for file in cogsFolderStuff:
    if file.endswith('.py'):
        fileName = file.split('.')
        myCogs.append(str('cogs.' + fileName[0]))
#loading my cogs
if __name__ == '__main__':
    for ext in myCogs:
        client.load_extension(ext)
        
os.environ['JISHAKU_NO_UNDERSCORE'] = 'true'
client.load_extension("jishaku")


#Running client on server
client.run(varsToNotCopy.token)