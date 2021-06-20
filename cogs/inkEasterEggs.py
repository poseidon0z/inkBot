'''
1. WHAT IS THIS FILE?
This is where i store all my easter eggs, and if ink code ever becomes public, this will be gitignored

2. WHAT ARE THE EASTER EGGS IN THE BOT?
(a) greet

IMPORTS:
1. discord - cause discord
2. commands from discord.ext - cause its basically what the cog runs on
'''
import discord
from discord.ext import commands


class inkEasterEggs(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    '''
    The 'greet' autoresponse
    The first command to ever be used on inkBot, the currently added script is the same one i created ages ago (thats why its so weirdly written)
    Saved into easter eggs as a memory of the start of a great learning experience
    '''
    @commands.Cog.listener("on_message")
    async def greet(self,message):
        #hi ink response
        if 'hi ink' == message.content.lower():
            if message.author.bot == False:
                if str(message.author.nick) != 'None':
                    allowedMentions = discord.AllowedMentions(everyone=False,roles=False,users=False)
                    await message.channel.send('Hi ' + str(message.author.nick), allowed_mentions=allowedMentions)
                else:
                    allowedMentions = discord.AllowedMentions(everyone=False,roles=False,users=False)
                    await message.channel.send('Hi ' + str(message.author.name), allowed_mentions=allowedMentions)


def setup(bot):
    bot.add_cog(inkEasterEggs(bot))