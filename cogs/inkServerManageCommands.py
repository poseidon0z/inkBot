#imports required to ru this code
import discord
from discord.ext import commands
import varsToNotCopy
from discord.ext.commands import MissingRequiredArgument
from discord.ext.commands import MemberNotFound
from discord.ext.commands import ChannelNotFound

class inkServerManageCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #addchan command
    @commands.command(name='addchannel',aliases=['ac', 'addchan','achan'])
    async def addchannel(self,ctx,channel : discord.TextChannel,target : discord.Member):
        if ctx.author.guild_permissions.manage_channels == True:
            await channel.set_permissions(target, view_channel=True,send_messages=True)
            await ctx.channel.send(f'{target.mention} has been added to {channel.mention}')
        else:
            await ctx.channel.send(f'Oi {ctx.author.mention}! You dont have perms <a:angry:840470937325273098>')
        
    @addchannel.error
    async def addchannel_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.channel.send(f'Missing arguemnts, make sure you follow the syntax:\n```ink addchannel <channel> <member>```')
        elif isinstance(error, MemberNotFound):
            await ctx.channel.send(f'Couldnt find the member you were trying to add')
        elif isinstance(error, ChannelNotFound):
            await ctx.channel.send(f'Couldnt find the channel you were trying to add to')
            
    #removechan command
    @commands.command(name='removechannel',aliases=['rc', 'removechan','rchan'])
    async def removechannel(self,ctx,channel : discord.TextChannel,target : discord.Member):
        if ctx.author.guild_permissions.manage_channels == True:
            await channel.set_permissions(target, overwrite=None)
            await ctx.channel.send(f'{target.mention} has been removed from {channel.mention}')
        else:
            await ctx.channel.send(f'Oi {ctx.author.mention}! You dont have perms <a:angry:840470937325273098>')

    @removechannel.error
    async def removechannel_error(self, ctx, error):
        if isinstance(error,MissingRequiredArgument):
            await ctx.channel.send(f'Missing arguemnts, make sure you follow the syntax:\n```ink removechannel <channel> <member>```')
        elif isinstance(error, MemberNotFound):
            await ctx.channel.send(f'Couldnt find the member you were trying to add')
        elif isinstance(error, ChannelNotFound):
            await ctx.channel.send(f'Couldnt find the channel you were trying to add to')

#cog setup
def setup(bot):
    bot.add_cog(inkServerManageCommands(bot))
