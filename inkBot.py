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

@client.command(name="botban")
@commands.is_owner()
async def botban(ctx,target : discord.User):
    cluster = pymongo.MongoClient(secrets.cluster)
    bannedInfo = cluster['banned']['Ids'] 
    userID = target.id
    status = bannedInfo.find_one({"_id" : userID})
    if status is None:
        bannedInfo.insert_one({'_id' : userID})
        await ctx.send(f'User {target.mention} ({target.id}) has been successfully bot banned')
    else:
        await ctx.send('Looks like this user is already banned')

@client.command(name='botunban')
@commands.is_owner()
async def botban(ctx,target : discord.User):
    cluster = pymongo.MongoClient(secrets.cluster)
    bannedInfo = cluster['banned']['Ids'] 
    userID = target.id
    status = bannedInfo.find_one({"_id" : userID})
    if status is None:
        await ctx.send('Looks like this user is not banned')
    else:
        bannedInfo.delete_one({'_id' : userID})
        await ctx.send(f'User {target.mention} ({target.id}) has been successfully unbanned')

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