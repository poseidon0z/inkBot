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
                try:
                    userToBan = int(message.content[4:22])
                    userToBan = str(userToBan)
                    if len(userToBan) == 18:
                        userToBan = await self.bot.fetch_user(userToBan)
                        await message.channel.send(f"""Banning user:{userToBan.name}(#{userToBan.discriminator}) with id:{userToBan.id} for scam reported in the message {message.jump_url}""")
                        await message.guild.ban(user= userToBan,reason= 'Ink autoban for being reported by another server. [Link to alert](' + message.jump_url + ')')
                    else:
                        userToBan = int(message.content[3:21])
                        userToBan = str(userToBan)
                        if len(userToBan) == 18:
                            userToBan = await self.bot.fetch_user(userToBan)
                            await message.channel.send(f"""Banning user:{userToBan.name}(#{userToBan.discriminator}) with id:{userToBan.id} for scam reported in the message {message.jump_url}""")
                            await message.guild.ban(user= userToBan,reason= 'Ink autoban for being reported by another server. [Link to alert](' + message.jump_url + ')')
                        else:
                            await message.channel.send('Couldnt find ID, ping adi if this happens too often and he\'ll prolly think of a fix <a:MaidThumbsUp:839411010460975165>')
                except ValueError:
                    await message.channel.send('I detected something.... but its not an id....')
                except:
                    await message.channel.send('Couldnt find ID, ping adi if this happens too often and he\'ll prolly think of a fix <a:MaidThumbsUp:839411010460975165>')
            
            elif simplifications.isAFailChannel(message):            
                try:
                    userToBan = int(message.content[4:22])
                    userToBan = str(userToBan)
                    if len(userToBan) == 18:
                        await message.delete()
                    else:
                        userToBan = int(message.content[3:21])
                        userToBan = str(userToBan)
                        if len(userToBan) == 18:
                            await message.delete()
                        else:
                            await message.channel.send('Couldnt find ID, ping adi if this happens too often and he\'ll prolly think of a fix <a:MaidThumbsUp:839411010460975165>')
                except ValueError:
                    await message.channel.send('I detected something.... but its not an id....')
                except:
                    await message.channel.send('Couldnt find ID, ping adi if this happens too often and he\'ll prolly think of a fix <a:MaidThumbsUp:839411010460975165>')


def setup(bot):
    bot.add_cog(autoBan(bot))