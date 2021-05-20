#importing the discord package
import discord
from discord.ext import commands
import os
import secrets
import pymongo

# Client (my bot)
client = commands.Bot(command_prefix = ['ink ', 'ink', 'Ink ','Ink'])
client.remove_command('help')


#message sent in bot status when bot comes on
@client.event
async def on_ready():
    print('bot is online')



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

client.load_extension('jishaku')

#Running client on server
client.run(secrets.token)