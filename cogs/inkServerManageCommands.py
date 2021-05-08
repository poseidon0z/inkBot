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
    #triggers which include: 
    #hi ink trigger
    #ars
    #Scammer Autoban


    @commands.Cog.listener()
    async def on_message(self,message):
        #hi ink response
        if 'hi ink' == message.content.lower():
            if str(message.author.nick) != 'None':
                allowedMentions = discord.AllowedMentions(everyone=False,roles=False,users=False)
                await message.channel.send('Hi ' + str(message.author.nick), allowed_mentions=allowedMentions)
            else:
                allowedMentions = discord.AllowedMentions(everyone=False,roles=False,users=False)
                await message.channel.send('Hi ' + str(message.author.name), allowed_mentions=allowedMentions)

        #adi ar    
        if 'adi' in message.content.lower():
            await message.add_reaction('<:kiki_happy:839524132286365717>')

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
                
        #scammer banning feature
        if 'id' == message.content.lower()[0:2]:
            if message.channel.id in varsToNotCopy.alertChannel_id:
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
            
            elif message.channel.id in varsToNotCopy.failChannel_id:
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



#cog setup
def setup(bot):
    bot.add_cog(inkServerManageCommands(bot))
