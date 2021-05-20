import builtins
import discord
from discord.ext import commands
from utils import simplifications

class autoBan(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    @commands.check(simplifications.isNotbanned)
    @commands.guild_only()
    async def on_message(self,message):
        if simplifications.isProbablyAnAlert(message) is True:
            if simplifications.isAnAlertChannel(message) is True:
                idMaker = []
                splitMessage = list(message.content.split('\n'))
                for word in list(splitMessage[0]):
                    try:
                        number = int(word)
                        idMaker.append(str(number))
                    except ValueError:
                        pass
                personId = "".join(idMaker)
                if len(str(personId)) == 18:
                    userToBan = await self.bot.fetch_user(int(personId))
                    await message.channel.send(f"""Banning user:{userToBan.name}(#{userToBan.discriminator}) with id:{userToBan.id} for scam reported in the message {message.jump_url}""")
                    await message.guild.ban(user= userToBan,reason= 'Ink autoban for being reported by another server. [Link to alert](' + message.jump_url + ')')

            elif simplifications.isAFailChannel(message):            
                idMaker = []
                splitMessage = list(message.content.split('\n'))
                for word in list(splitMessage[0]):
                    try:
                        number = int(word)
                        idMaker.append(str(number))
                    except ValueError:
                        pass
                personId = "".join(idMaker)
                if len(str(personId)) == 18:
                    userToBan = await self.bot.fetch_user(int(personId))
                    await message.delete()
def setup(bot):
    bot.add_cog(autoBan(bot))