'''
WHAT IS THIS FILE?
This is the cog that handles the autoban command for inkBot

IMPORTS:
1. discord cause discord
2. commands from discord.ext - basically runs the cog
3. is_a commands to check for alert and fail channel
4. is_not_bot_banned stops bot-banned members from accessing the command
'''
from utils.botwideFunctions import is_not_bot_banned
import discord
from discord.ext import commands
from utils.commandShortenings import is_a_fail_channel,is_an_alert_channel

class inkAutoban(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    '''
    The 'autoban' function:
    Bans scammers reported into alert channels and leaves only fails behind in the fail channel
    '''
    @commands.Cog.listener("on_message")
    @is_not_bot_banned()
    async def autoban(self,message):
        if message.author.id not in [838390757449662496,839052539395440710]:            #making sure bots dont trigger each other
            if "id" in str(message.content.lower()):
                if is_an_alert_channel(message) is True:
                    first_line = message.content.split('\n')[0]
                    numbers_in_line = []
                    if 'id' in str(first_line.lower()):
                        for letter in list(first_line):
                            try:
                                scammer_id_character = int(letter)
                                numbers_in_line.append(str(scammer_id_character))
                            except:
                                pass
                        probable_scammer_id = ''.join(numbers_in_line)
                        if len(probable_scammer_id) == 18:
                            userToBan = await self.bot.fetch_user(int(probable_scammer_id))
                            await message.channel.send(f"""Banning user:{userToBan.name}(#{userToBan.discriminator}) with id:{userToBan.id} for scam reported in the message {message.jump_url}""")
                            await message.guild.ban(user= userToBan,reason= 'Ink autoban for being reported by another server. [Link to alert](' + message.jump_url + ')')

                if is_a_fail_channel(message) is True:
                    first_line = message.content.split('\n')[0]
                    numbers_in_line = []
                    if 'id' in str(first_line.lower()):
                        for letter in list(first_line):
                            try:
                                scammer_id_character = int(letter)
                                numbers_in_line.append(str(scammer_id_character))
                            except:
                                pass
                        probable_scammer_id = ''.join(numbers_in_line)
                        if len(probable_scammer_id) == 18:
                            userToBan = await self.bot.fetch_user(int(probable_scammer_id))
                            await message.delete()

def setup(bot):
    bot.add_cog(inkAutoban(bot))
    print("""Cog inkAutoban has loaded successfully
--------------------""")