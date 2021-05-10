#importing all required stuff
import discord
from discord.ext import commands
import varsToNotCopy
from discord.ext.commands import MissingRequiredArgument
from discord.ext.commands import MemberNotFound
from discord.ext.commands import ChannelNotFound

#creating the class, which is the cog
class inkServerManageCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #addchan command to add a member to a channel
    @commands.command(name='addchannel',aliases=['ac', 'addchan','achan'])
    @commands.has_permissions(manage_channels=True)
    async def addchannel(self,ctx,target : discord.Member):    
        await ctx.channel.set_permissions(target, view_channel=True,send_messages=True)             #giving the member perms to view the channel and send messages
        await ctx.channel.send(f'{target.mention} has been added to {ctx.channel.mention}')

        
    @addchannel.error
    async def addchannel_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.channel.send(f'Missing arguemnts, make sure you follow the syntax:\n```ink addchannel <member>```')
        elif isinstance(error, MemberNotFound):
            await ctx.channel.send(f'Couldnt find the member you were trying to add to')
        else:
            pass

    #removechan command
    @commands.command(name='removechannel',aliases=['rc', 'removechan','rchan'])
    @commands.has_permissions(manage_channels=True)
    async def removechannel(self,ctx,target : discord.Member):    
        await ctx.channel.set_permissions(target, overwrite=None)                                               #removing the overwrites the member has
        await ctx.channel.send(f'{target.mention} has been removed from {ctx.channel.mention}')

    @removechannel.error
    async def removechannel_error(self, ctx, error):
        if isinstance(error,MissingRequiredArgument):
            await ctx.channel.send(f'Missing arguemnts, make sure you follow the syntax:\n```ink removechannel <member>```')
        elif isinstance(error, MemberNotFound):
            await ctx.channel.send(f'Couldnt find the member you were trying to take perms for')
        else:
            pass

    #channelmanager
    @commands.command(name='addchannelmanager',aliases=['acm','addchanman'])
    @commands.has_guild_permissions(manage_channels=True)
    async def addchannelmanager(self,ctx,channel : discord.TextChannel,target : discord.Member): 
        await channel.set_permissions(target,manage_channels=True)                                                                  #giving the member manage channel perms for that channel
        await ctx.channel.send(f'{target.mention} has been made channel manager for {channel.mention}')
         

    @addchannelmanager.error
    async def addchannelmanager_error(self,ctx,error):
        if isinstance(error,MissingRequiredArgument):
            await ctx.channel.send(f'Missing arguemnts, make sure you follow the syntax:\n```ink addchannelmanager <channel> <member>```')
        elif isinstance(error, MemberNotFound):
            await ctx.channel.send(f'Couldnt find the member you were give to take perms to')
        elif isinstance(error, ChannelNotFound):
            await ctx.channel.send(f'Couldnt find the channel')
        else:
            pass

    @commands.command(name='removechannelmanager',aliases=['rcm','remchanman'])
    @commands.has_guild_permissions(manage_channels=True)
    async def removechannelmanager(self,ctx,channel : discord.TextChannel,target : discord.Member):     
        await channel.set_permissions(target, manage_channels=None)                                                     #removing the manage channel perms for that channel from the member
        await ctx.channel.send(f'{target.mention} has been removed as channel manager for {channel.mention}')
    

    @removechannelmanager.error
    async def removechannelmanager_error(self,ctx,error):
        if isinstance(error,MissingRequiredArgument):
            await ctx.channel.send(f'Missing arguemnts, make sure you follow the syntax:\n```ink removechannelmanager <channel> <member>```')
        elif isinstance(error, MemberNotFound):
            await ctx.channel.send(f'Couldnt find the member you were trying to take perms for')
        elif isinstance(error, ChannelNotFound):
            await ctx.channel.send(f'Couldnt find the channel')
        else:
            pass

#cog setup
def setup(bot):
    bot.add_cog(inkServerManageCommands(bot))
