'''
1. WHAT IS THIS FILE?
This is the file that manages global errors for the bot

2. WHAT ARE THE ERROR HANDLERS CURRENTLY PRESENT?

'''
import discord
import traceback
import sys
from discord.ext import commands
from discord.ext.commands.errors import ChannelNotFound, CommandOnCooldown, RoleNotFound

'''
VARIABLES:

'''

class commandErrorHandler(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    '''
    This is called whenever an error is raised
    '''
    @commands.Cog.listener('on_command_error')
    async def global_error_handler(self,ctx,error):
        cog = ctx.cog
        error = getattr(error,'original' , error)
        
        if isinstance(error,commands.CommandNotFound):
            print(f'{ctx.author.id} tried using a command: {ctx.command}')
        
        if isinstance(error,commands.MemberNotFound):
            try:
                await ctx.reply(f'Couldn\'t find the member "{error.argument}" <:lotsofpain:839371861346222112>')
            except:
                await ctx.send(f'Couldn\'t find the member "{error.argument}" <:lotsofpain:839371861346222112>')

        if isinstance(error,ChannelNotFound):
            try:
                await ctx.reply(f'Couldn\'t find the channel "{error.argument}" <:lotsofpain:839371861346222112>')
            except:
                await ctx.send(f'Couldn\'t find the channel "{error.argument}" <:lotsofpain:839371861346222112>')

        if isinstance(error,RoleNotFound):
            try:
                await ctx.reply(f'Couldn\'t find the role "{error.argument}" <:lotsofpain:839371861346222112>')
            except:
                await ctx.send(f'Couldn\'t find the role "{error.argument}" <:lotsofpain:839371861346222112>')

        if isinstance(error,CommandOnCooldown):
            try:
                await ctx.reply(f'You\'re on cooldown from using the {ctx.command} command for {error.retry_after:.2f} more seconds!')
            except:
                await ctx.send(f'{ctx.author.mention}! You\'re on cooldown from using the {ctx.command} command for {error.retry_after:.2f} more seconds!')
        
        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)



def setup(bot):
    bot.add_cog(commandErrorHandler(bot))