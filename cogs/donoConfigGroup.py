#importing requirements
from operator import truediv
import discord
from discord.ext import commands
from discord.ext.commands.core import command
import pymongo
import secrets

#specifying few vars
cluster = pymongo.MongoClient(secrets.cluster)
allowedMentions = discord.AllowedMentions(everyone=False,roles=False)

#cog contents
class donoConfigGroup(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.group(name='settings',aliases=['set'],invoke_without_commands=True)
    async def set(self,ctx):
        setEmbed = discord.Embed(title='inkBot guild specific configs')
    
    @set.command(name='giveawaymanager', aliases=['gmanrole', 'gr'])
    @commands.check_any(commands.is_owner(), commands.has_guild_permissions(administrator=True),commands.has_guild_permissions(manage_guild=True))
    async def giveawayManagerRole(self,ctx,role : discord.Role):
        db = cluster['donations' + str(ctx.guild.id)]
        settingsCol = db['serverSettings']
        query = {"_id" : 'giveawayManagerRole'}
        status = settingsCol.find_one(query)
        roleID = role.id
        if status is None:
            settingsCol.insert_one({"_id" : 'giveawayManagerRole','role' : roleID})
            await ctx.send(f'giveaway manager role has been added as {role.mention}',allowed_mentions = allowedMentions)
        else:
            settingsCol.update_one(query,{"$set": {'role' : roleID}})
            await ctx.send(f'giveaway manager role has been updated to {role.mention}',allowed_mentions = allowedMentions)

    @set.command(name='eventmanager', aliases=['emanrole', 'er'])
    @commands.check_any(commands.is_owner(), commands.has_guild_permissions(administrator=True),commands.has_guild_permissions(manage_guild=True))
    async def eventManagerRole(self,ctx,role : discord.Role):
        db = cluster['donations' + str(ctx.guild.id)]
        settingsCol = db['serverSettings']
        query = {"_id" : 'eventManagerRole'}
        status = settingsCol.find_one(query)
        roleID = role.id
        if status is None:
            settingsCol.insert_one({"_id" : 'eventManagerRole','role' : roleID})
            await ctx.send(f'event manager role has been added as {role.mention}',allowed_mentions = allowedMentions)
        else:
            settingsCol.update_one(query,{"$set": {'role' : roleID}})
            await ctx.send(f'event manager role has been updated to {role.mention}',allowed_mentions = allowedMentions)
        
    @set.command(name='moderator', aliases=['mod', 'mr'])
    @commands.check_any(commands.is_owner(), commands.has_guild_permissions(administrator=True),commands.has_guild_permissions(manage_guild=True))
    async def modRole(self,ctx,role : discord.Role):
        db = cluster['donations' + str(ctx.guild.id)]
        settingsCol = db['serverSettings']
        query = {"_id" : 'modRole'}
        status = settingsCol.find_one(query)
        roleID = role.id
        if status is None:
            settingsCol.insert_one({"_id" : 'modRole','role' : roleID})
            await ctx.send(f'Mod role has been added as {role.mention}',allowed_mentions = allowedMentions)
        else:
            settingsCol.update_one(query,{"$set": {'role' : roleID}})
            await ctx.send(f'Mod role has been updated to {role.mention}',allowed_mentions = allowedMentions)

    @set.command(name='administrator', aliases=['admin', 'ar'])
    @commands.check_any(commands.is_owner(), commands.has_guild_permissions(administrator=True),commands.has_guild_permissions(manage_guild=True))
    async def adminRole(self,ctx,role : discord.Role):
        db = cluster['donations' + str(ctx.guild.id)]
        settingsCol = db['serverSettings']
        query = {"_id" : 'adminRole'}
        status = settingsCol.find_one(query)
        roleID = role.id
        if status is None:
            settingsCol.insert_one({"_id" : 'adminRole','role' : roleID})
            await ctx.send(f'Mod role has been added as {role.mention}',allowed_mentions = allowedMentions)
        else:
            settingsCol.update_one(query,{"$set": {'role' : roleID}})
            await ctx.send(f'Mod role has been updated to {role.mention}',allowed_mentions = allowedMentions)



#running the cog
def setup(bot):
    bot.add_cog(donoConfigGroup(bot))