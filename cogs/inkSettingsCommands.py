'''
1. WHAT IS THIS FILE?
This file consists of settings commands for inkBot

2. WHAT ARE THE COMMANDS HERE?
(a) settings
    (1) Giveaway Manager
    (2) Event Manager
    (3) Moderator
    (4) Admin
    (5) alertchannel
    (6) failchannel


IMPORTS:
1. discord - ................ cause discord
2. commands from discord.ext - what the cog runs on
3. load to load my json
4. path to define the path to my json
5. pymongo to interact with the db
6. is_not_bot_banned to stop bot banned members from using bot commands
7. error handlers
'''
import discord
from discord.ext import commands
from json import load
from pathlib import Path
from discord.ext.commands.errors import RoleNotFound
import pymongo
from utils.botwideFunctions import is_not_bot_banned
from discord.ext.commands import MemberNotFound,CheckAnyFailure,MissingRequiredArgument,ChannelNotFound

'''
VARIABLES:
1. allowed_mentions - mention perms allowed for messages sent for the bot
2. cluster - the cluster where the data is stored
3. embed_colour - colour for embeds used
'''
allowed_mentions = discord.AllowedMentions(everyone=False,roles=False)
with Path("utils/secrets.json").open() as f:
    config = load(f)
cluster = pymongo.MongoClient(config["cluster"])
embed_colour = 0x52476B

class inkSettingsCommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.group(name='settings',aliases=['set'],invoke_without_command=True)
    @is_not_bot_banned()
    @commands.guild_only()
    async def settings(self,ctx):
        settings_embed = discord.Embed(title='**Settings Group Commands**', description='Alias for this command is `set`\nYou need admin or manage server perms to run commands in this category!',colour=embed_colour)
        settings_embed.add_field(name='Giveaway manager',value='Sets a role as a giveaway manager role\nMembers with this role have perms to set giveaway donos, special donos and check a member\'s donos',inline=False)
        settings_embed.add_field(name='Event manager',value='Sets a role as a event manager role\nMembers with this role have perms to set event donos, special donos and check a member\'s donos',inline=False)
        settings_embed.add_field(name='Moderator',value='Sets a role as a mod role\nMembers with this role have perms to set event donos, giveaway donos, special donos and check a member\'s donos',inline=False)
        settings_embed.add_field(name='Administrator',value='Sets a role as the administrator role\nMembers with this role have perms to run all commands under the donation group!',inline=False)
        settings_embed.add_field(name='alertchannel',value='Sets a channel as the alert channel, that is used for the autoban feature',inline=False)
        settings_embed.add_field(name='failchannel',value='Sets a channel as the fail channel, that is used for the autoban feature',inline=False)
        await ctx.send(embed=settings_embed)
    
    '''
    The 'giveawaymanager' command:
    Sets a role as the gman role, which can run all cmds that gmans will need like "d gaw" or "d special" or "d check"
    '''
    @settings.command(name='giveawaymanager',aliases=['gman'])
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.check_any(commands.is_owner(), commands.has_guild_permissions(administrator=True),commands.has_guild_permissions(manage_guild=True))
    async def giveawaymanager(self,ctx,role : discord.Role):
        server_settings = cluster[str(ctx.guild.id)]['serverSettings']
        query = {"_id" : 'giveawayManagerRole'}
        server_settings.update_one(query,{"$set": {'role' : role.id}},upsert=True)
        await ctx.send(role.id)
        print(role)
        await ctx.send(f'Giveaway manager role has been set as {role.mention}',allowed_mentions=allowed_mentions)

    @giveawaymanager.error
    async def giveawaymanager_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        elif isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink settings giveawaymanager <role>\n\n{error.param} is not specified```')
        elif isinstance(error,RoleNotFound):
            await ctx.send(f'Couldn\'t find the role "{error.argument}" <:lotsofpain:839371861346222112>',allowed_mentions=allowed_mentions)
        else:
            print(error)

    '''
    The 'eventmanager' command:
    Sets a role as the eman role, which can run all cmds that emans will need like "d event" or "d special" or "d check"
    '''
    @settings.command(name='eventmanager',aliases=['eman'])
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.check_any(commands.is_owner(), commands.has_guild_permissions(administrator=True),commands.has_guild_permissions(manage_guild=True))
    async def eventmanager(self,ctx,role : discord.Role):
        server_settings = cluster[str(ctx.guild.id)]['serverSettings']
        query = {"_id" : 'eventManagerRole'}
        server_settings.update_one(query,{"$set": {'role' : role.id}},upsert=True)
        await ctx.send(f'Event manager role has been set as {role.mention}',allowed_mentions=allowed_mentions)
    
    @eventmanager.error
    async def eventmanager_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        elif isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink settings eventmanager <role>\n\n{error.param} is not specified```')
        elif isinstance(error,RoleNotFound):
            await ctx.send(f'Couldn\'t find the role "{error.argument}" <:lotsofpain:839371861346222112>',allowed_mentions=allowed_mentions)
        else:
            print(error)

    '''
    The 'moderator' command:
    Sets a role as the mod role, which can run all cmds that mods can support managers with like "d event", "d gaw" or "d special" or "d check"
    '''
    @settings.command(name='moderator',aliases=['mod'])
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.check_any(commands.is_owner(), commands.has_guild_permissions(administrator=True),commands.has_guild_permissions(manage_guild=True))
    async def moderator(self,ctx,role : discord.Role):
        server_settings = cluster[str(ctx.guild.id)]['serverSettings']
        query = {"_id" : 'modRole'}
        server_settings.update_one(query,{"$set": {'role' : role.id}},upsert=True)
        await ctx.send(f'Mod role has been set as {role.mention}',allowed_mentions=allowed_mentions)
    
    @moderator.error
    async def moderator_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        elif isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink settings moderator <role>\n\n{error.param} is not specified```')
        elif isinstance(error,RoleNotFound):
            await ctx.send(f'Couldn\'t find the role "{error.argument}" <:lotsofpain:839371861346222112>',allowed_mentions=allowed_mentions)
        else:
            print(error)

    '''
    The 'admin' command:
    Sets a role as the admin role that can run all donation commands
    '''
    @settings.command(name='administrator',aliases=['admin'])
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.check_any(commands.is_owner(), commands.has_guild_permissions(administrator=True),commands.has_guild_permissions(manage_guild=True))
    async def administrator(self,ctx,role : discord.Role):
        server_settings = cluster[str(ctx.guild.id)]['serverSettings']
        query = {"_id" : 'adminRole'}
        server_settings.update_one(query,{"$set": {'role' : role.id}},upsert=True)
        await ctx.send(f'Admin role has been set as {role.mention}',allowed_mentions=allowed_mentions)
    
    @administrator.error
    async def administrator_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        elif isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink settings administrator <role>\n\n{error.param} is not specified```')
        elif isinstance(error,RoleNotFound):
            await ctx.send(f'Couldn\'t find the role "{error.argument}" <:lotsofpain:839371861346222112>',allowed_mentions=allowed_mentions)
        else:
            print(error)
    

    '''
    The 'alertchan' command:
    Sets a channel as the alert channel
    '''
    @settings.command(name='alertchannel',aliases=['alertchan'])
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.check_any(commands.is_owner(), commands.has_guild_permissions(administrator=True),commands.has_guild_permissions(manage_guild=True))
    async def alertchannel(self,ctx,channel : discord.TextChannel):
        server_settings = cluster[str(ctx.guild.id)]['serverSettings']
        query = {"_id" : 'alertChan'}
        server_settings.update_one(query,{"$set": {'role' : channel.id}},upsert=True)
        await ctx.send(f'Alert channel has been set as {channel.mention}',allowed_mentions=allowed_mentions)
    
    @alertchannel.error
    async def alertchannel_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        elif isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink settings alertchannel <channel>\n\n{error.param} is not specified```')
        elif isinstance(error,ChannelNotFound):
            await ctx.send(f'Couldn\'t find the channel "{error.argument}" <:lotsofpain:839371861346222112>',allowed_mentions=allowed_mentions)
        else:
            print(error)
    
    '''
    The 'failchan' command:
    Sets a channel as the fail channel
    '''
    @settings.command(name='failchannel',aliases=['failchan'])
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.check_any(commands.is_owner(), commands.has_guild_permissions(administrator=True),commands.has_guild_permissions(manage_guild=True))
    async def failchannel(self,ctx,channel : discord.TextChannel):
        server_settings = cluster[str(ctx.guild.id)]['serverSettings']
        query = {"_id" : 'failChan'}
        server_settings.update_one(query,{"$set": {'role' : channel.id}},upsert=True)
        await ctx.send(f'Fail channel has been set as {channel.mention}',allowed_mentions=allowed_mentions)

    @failchannel.error
    async def failchannel_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        elif isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink settings failchannel <channel>\n\n{error.param} is not specified```')
        elif isinstance(error,ChannelNotFound):
            await ctx.send(f'Couldn\'t find the channel "{error.argument}" <:lotsofpain:839371861346222112>',allowed_mentions=allowed_mentions)
        else:
            print(error)

def setup(bot):
    bot.add_cog(inkSettingsCommands(bot))
    print("""Cog inkDonationSettingCommands has loaded successfully
--------------------""")