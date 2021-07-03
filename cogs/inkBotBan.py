'''
WHAT IS THIS FILE?
This is a cog to hold my botban and unban command!

IMPORTS:
discord cause idk
commands from discord.ext cause thats what the bot runs on
pymongo to interact with my database
'''
import discord
from discord.ext import commands
import pymongo
from json import load
from pathlib import Path

'''
VARIABLES:
1. allowed_mentions - mention perms allowed for messages sent for the bot
2. cluster - the cluster my db is on
'''
allowed_mentions = discord.AllowedMentions(everyone=False,roles=False)
with Path("utils/secrets.json").open() as f:
    config = load(f)
cluster = pymongo.MongoClient(config["cluster"])

class inkBotBan(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name='botban')
    @commands.is_owner()
    async def botban(self,ctx,target : discord.User):
        banned_info = cluster['banned']['Ids']
        query = {"_id" : target.id}
        already_banned = banned_info.find_one(query)
        if already_banned is None:
            banned_info.insert_one(query)
            await ctx.send(f'User {target.mention}`({target.id})` has been successfully bot banned',allowed_mentions=allowed_mentions)
        else:
            await ctx.send(f'This user is already bot banned!')
        
    @commands.command(name='botunban')
    @commands.is_owner()
    async def botunban(self,ctx,target : discord.User):
        banned_info = cluster['banned']['Ids']
        query = {"_id" : target.id}
        already_banned = banned_info.find_one(query)
        if already_banned is not None:
            banned_info.delete_one(query)
            await ctx.send(f'User {target.mention}`({target.id})` has been successfully unbanned',allowed_mentions=allowed_mentions)
        else:
            await ctx.send(f'This user is not bot banned!')
        
    @commands.command(name='checkforban',aliases=['cfb'])
    @commands.is_owner()
    async def checkforban(self,ctx,target : discord.User):
        banned_info = cluster['banned']['Ids']
        query = {"_id" : target.id}
        already_banned = banned_info.find_one(query)
        if already_banned is not None:
            await ctx.send(f'User {target.mention}`({target.id})` is bot banned',allowed_mentions=allowed_mentions)
        else:
            await ctx.send(f'User {target.mention}`({target.id})` is not bot banned')

def setup(bot):
    bot.add_cog(inkBotBan(bot))
    print("""Cog inkBotBan loaded successfully
--------------------""")