#importing required stuff
from re import A
from discord import colour
from pymongo import settings
from utils.simplifications import isNotbanned
import discord
from discord.ext import commands
from discord.ext.commands import has_guild_permissions,is_owner
import pymongo
import secrets

#my cog
class botSettings(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    '''
    The next 2 commands are bot wide commands so executing them changes a user's stuff throughout the bot
    '''
    @commands.command(name="botban")
    @commands.is_owner()
    async def botban(self,ctx,target : discord.User):
        cluster = pymongo.MongoClient(secrets.cluster)
        bannedInfo = cluster['banned']['Ids'] 
        userID = target.id
        status = bannedInfo.find_one({"_id" : userID})
        if status is None:
            bannedInfo.insert_one({'_id' : userID})
            await ctx.send(f'User {target.mention} ({target.id}) has been successfully bot banned')
        else:
            await ctx.send('Looks like this user is already banned')


    @commands.command(name='botunban')
    @commands.is_owner()
    async def botunban(self,ctx,target: discord.Member):
        cluster = pymongo.MongoClient(secrets.cluster)
        bannedInfo = cluster['banned']['Ids'] 
        userID = target.id
        status = bannedInfo.find_one({"_id" : userID})
        if status is None:
            await ctx.send('Looks like this user is not banned')
        else:
            bannedInfo.delete_one({'_id' : userID})
            await ctx.send(f'User {target.mention} ({target.id}) has been successfully unbanned')
        
    '''
    The following change bot settings for a particular channel
    '''
    @commands.group(name='autoban',invoke_without_command=True)
    @commands.check_any(commands.is_owner(), commands.has_guild_permissions(administrator=True),commands.has_guild_permissions(manage_guild=True))
    @commands.guild_only()
    async def autoban(self,ctx):
        autobanEmbed = discord.Embed(title='Autoban Scammers feature',description='Make sure to set all subcommands for the best experience',colour=0xabcdef)
        autobanEmbed.add_field(name='alertchan',value='Sets a channel from which ink scans all messages for ban reports',inline=False)
        autobanEmbed.add_field(name='failchan',value='Sets a channel from which ink deletes all scams that it could detect scammers from, leaving you with a list of all reports that ink couldnt find a scammer from',inline=False)
        autobanEmbed.add_field(name='Important: ',value='For best results out of ink, make sure to follow the same alert reporting channels in both the alert channel and fail channel\nAlso remember to make sure no one except ink can type in the alert channel so no foul play can be conducted',inline=False)
        await ctx.send(embed=autobanEmbed)

        
    @autoban.group(name='alertchan')
    @commands.check_any(commands.is_owner(), commands.has_guild_permissions(administrator=True),commands.has_guild_permissions(manage_guild=True))
    @commands.guild_only()
    @commands.check(isNotbanned)
    async def alertchannel(self,ctx,channel : discord.TextChannel):
        cluster = pymongo.MongoClient(secrets.cluster)
        serverSettingsCol = cluster[str(ctx.guild.id)]['serverSettings']
        query = {"_id" : 'alertChan'}
        status = serverSettingsCol.find_one(query)
        channelID = channel.id
        if status is None:
            serverSettingsCol.insert_one({"_id" : "alertChan","channel" : channelID})
            await ctx.send(f'{channel.mention} has been set as the alert channel for {ctx.guild.name}')
        else:
            serverSettingsCol.update_one(query,{"$set":{"channel" : channelID}})
            await ctx.send(f'Alert channel for {ctx.guild.name} has been changed to {channel.mention}')
    
    @autoban.group(name='failchan')
    @commands.check_any(commands.is_owner(),commands.has_guild_permissions(manage_guild=True),commands.has_guild_permissions(administrator=True))
    @commands.guild_only()
    @commands.check(isNotbanned)
    async def failchannel(self,ctx,channel : discord.TextChannel):
        cluster = pymongo.MongoClient(secrets.cluster)
        serverSettingsCol = cluster[str(ctx.guild.id)]['serverSettings']
        query = {"_id" : 'failChan'}
        status = serverSettingsCol.find_one(query)
        channelID = channel.id
        if status is None:
            serverSettingsCol.insert_one({"_id" : "failChan","channel" : channelID})
            await ctx.send(f'{channel.mention} has been set as the fail channel for {ctx.guild.name}')
        else:
            serverSettingsCol.update_one(query,{"$set":{"channel" : channelID}})
            await ctx.send(f'Fail channel for {ctx.guild.name} has been changed to {channel.mention}')
        
#setup
def setup(bot):
    bot.add_cog(botSettings(bot))