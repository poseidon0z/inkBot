'''
1. WHAT IS THIS FILE?
This is the file that manages global errors for the bot

2. WHAT ARE THE ERROR HANDLERS CURRENTLY PRESENT?

'''
import discord
import traceback
import sys
from discord.ext import commands
from discord.ext.commands.errors import BotMissingPermissions, ChannelNotFound, CommandOnCooldown, NotOwner, RoleNotFound

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
        error = getattr(error,'original' , error)

        if hasattr(ctx.command, 'on_error'):
            run_the_error = await ctx.command.on_error(self,ctx,error,rerun=True)
            if run_the_error == None:
                return
            elif run_the_error == False:
                pass

        if isinstance(error,commands.CommandNotFound):
            print(f'{ctx.author.id} tried using a command: {ctx.command}')
        
        elif isinstance(error,commands.MemberNotFound):
            try:
                await ctx.reply(f'Couldn\'t find the member "{error.argument}" <:lotsofpain:839371861346222112>')
            except:
                await ctx.send(f'Couldn\'t find the member "{error.argument}" <:lotsofpain:839371861346222112>')

        elif isinstance(error,ChannelNotFound):
            try:
                await ctx.reply(f'Couldn\'t find the channel "{error.argument}" <:lotsofpain:839371861346222112>')
            except:
                await ctx.send(f'Couldn\'t find the channel "{error.argument}" <:lotsofpain:839371861346222112>')

        elif isinstance(error,RoleNotFound):
            try:
                await ctx.reply(f'Couldn\'t find the role "{error.argument}" <:lotsofpain:839371861346222112>')
            except:
                await ctx.send(f'Couldn\'t find the role "{error.argument}" <:lotsofpain:839371861346222112>')

        elif isinstance(error,CommandOnCooldown):
            try:
                await ctx.reply(f'You\'re on cooldown from using the {ctx.command} command for {error.retry_after:.2f} more seconds!')
            except:
                await ctx.send(f'{ctx.author.mention}! You\'re on cooldown from using the {ctx.command} command for {error.retry_after:.2f} more seconds!')
        
        elif isinstance(error,NotOwner):
            print(f'{ctx.author.id} tried running a owner only command: {ctx.command}')
            
        elif isinstance(error,discord.errors.Forbidden):
            try:
                await ctx.reply(f'I don\'t have the permissions nessasary to run this')
            except:
                await ctx.send(f'I don\'t have the permissions nessasary to run this')

        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)



def setup(bot):
    bot.add_cog(commandErrorHandler(bot))