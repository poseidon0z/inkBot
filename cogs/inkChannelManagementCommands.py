'''
WHAT IS THIS FILE?
This is the cog with all channel management commands

WHAT ARE THE COMMANDS IN THIS FILE?
(a) addchannel
(b) removechannel
(c) addchannelmanager
(d) removechannelmanager

IMPORTS
1. discord - cause discord
2. commands from discord.ext - basically what the cog runs based off of
3. Error handlers
4. is_not_bot_banned - stops bot banned users from running commands
'''
import discord
from discord.ext import commands
from discord.ext.commands.errors import BotMissingPermissions, ChannelNotFound, MemberNotFound,MissingRequiredArgument
from utils.botwideFunctions import is_not_bot_banned

'''
Variables
1. allowed_mentions - used to restrict bot mentions so it can only mention users, not roles or everyone 
'''
allowed_mentions = discord.AllowedMentions(everyone=False,roles=False)


class inkChannelManagementCommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    '''
    The 'addchannel' command
    Adds a member to a channel by giving them view_channel and send_message overrides
    '''
    @commands.command(name='addchannel',aliases=['ac','addchan'])
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    async def add_channel(self,ctx,target : discord.Member):    
        await ctx.channel.set_permissions(target, view_channel=True,send_messages=True)
        await ctx.channel.send(f'{target.mention} has been added to {ctx.channel.mention}',allowed_mentions=allowed_mentions)
    
    @add_channel.error
    async def add_channel_error(self,ctx,error):
        if isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink addchannel <member>\n\n{error.param} is not specified```')
        elif isinstance(error,BotMissingPermissions):
            await ctx.send(f'I need the {error.missing_perms} perm to run this command, which i dont have!')
        else:
            print(error)

    '''
    The 'removechannel' command
    Removes a member from a channel by clearing their overrides for that channel
    '''
    @commands.command(name='removechannel',aliases=['rc','remchan'])
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    async def remove_channel(self,ctx,target : discord.Member):    
        await ctx.channel.set_permissions(target, overwrite=None)
        await ctx.channel.send(f'{target.mention} has been removed from {ctx.channel.mention}')
    
    @remove_channel.error
    async def remove_channel_error(self,ctx,error):
        if isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink removechannel <member>\n\n{error.param} is not specified```')
        elif isinstance(error,BotMissingPermissions):
            await ctx.send(f'I need the {error.missing_perms} perm to run this command, which i dont have!')
        else:
            print(error)


    '''
    The 'addchannelmanager' command
    Adds a member as a "channel manager" for that channel, giving them manage_channel perms
    '''    
    @commands.command(name='addchannelmanager',aliases=['acm'])
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    async def add_channel_manager(self,ctx,channel : discord.TextChannel,target : discord.Member): 
        await channel.set_permissions(target,manage_channels=True)                                                                  #giving the member manage channel perms for that channel
        await ctx.channel.send(f'{target.mention} has been made channel manager for {channel.mention}')
    
    @add_channel_manager.error
    async def add_channel_manager_error(self,ctx,error):
        if isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink addchannelmanager <channel> <member>\n\n{error.param} is not specified```')
        elif isinstance(error,BotMissingPermissions):
            await ctx.send(f'I need the {error.missing_perms} perm to run this command, which i dont have!')
        else:
            print(error)

    '''
    The 'removechannelmanager' command
    Removes a member as channel manager for the channel
    '''    
    @commands.command(name='removechannelmanager',aliases=['rcm'])
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    async def remove_channel_manager(self,ctx,channel : discord.TextChannel,target : discord.Member):     
        await channel.set_permissions(target, manage_channels=None)                                                     #removing the manage channel perms for that channel from the member
        await ctx.channel.send(f'{target.mention} has been removed as channel manager for {channel.mention}')
    
    @remove_channel_manager.error
    async def remove_channel_manager_error(self,ctx,error):
        if isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink removechannelmanager <channel> <member>\n\n{error.param} is not specified```')
        elif isinstance(error,BotMissingPermissions):
            await ctx.send(f'I need the {error.missing_perms} perm to run this command, which i dont have!')
        else:
            print(error)


def setup(bot):
    bot.add_cog(inkChannelManagementCommands(bot))
    print("""Cog inkChannelManagementCommands loaded successfully
--------------------""")