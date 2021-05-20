import discord
from discord.ext import commands
import varsToNotCopy
from utils import simplifications
class onMessageCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #triggers which include: 
    #hi ink trigger
    #ars
    #Scammer Autoban


    @commands.Cog.listener()
    @commands.check(simplifications.isNotbanned)
    @commands.guild_only()
    async def on_message(self,message):
        #hi ink response
        if 'hi ink' == message.content.lower():
            if message.guild.id != 719180744311701505:
                if str(message.author.nick) != 'None':
                    allowedMentions = discord.AllowedMentions(everyone=False,roles=False,users=False)
                    await message.channel.send('Hi ' + str(message.author.nick), allowed_mentions=allowedMentions)
                else:
                    allowedMentions = discord.AllowedMentions(everyone=False,roles=False,users=False)
                    await message.channel.send('Hi ' + str(message.author.name), allowed_mentions=allowedMentions)


        if str(message.content) == f'''<@!{varsToNotCopy.bot_id}>''' or str(message.content) == f'''<@{varsToNotCopy.bot_id}>''':
                await message.channel.send('Hi! My prefix is `ink `, run `ink help` for more details!!')

        #ping autoreacts
        if len(message.mentions) > 0:
            for okSomeonesPing in message.mentions:
                #adi's ar
                if okSomeonesPing.id == 652756616185380894:
                    await message.add_reaction('<:kiki_happy:839524132286365717>')
                #ceee's ar <3
                elif okSomeonesPing.id == 696754560429064263:
                    await message.add_reaction('<:an_urcute:776896089760333844>')

               
def setup(bot):
    bot.add_cog(onMessageCommands(bot))