#importing the discord package
import discord
from discord.ext import commands
import random
import time
import inkServerManageCommands
import varsToNotCopy
from discord.ext.commands import MemberNotFound
import os

# Client (my bot)
client = commands.Bot(command_prefix = ['ink ', 'ink', 'Ink'])
client.remove_command('help')


#doing stuff


#message sent in bot status when bot comes on
@client.event
async def on_ready():
    print('bot is online')

#message sent in bot status when bot goes down
@client.event
async def on_disconnect():
    print('bot is now going offline')


#triggers which include: 
#1. hi ink trigger
#adi ar
#Scammer Autoban
@client.event
async def on_message(message):
    if 'hi ink' == message.content.lower():
        if str(message.author.nick) != 'None':
            allowedMentions = discord.AllowedMentions(everyone=False,roles=False,users=False)
            await message.channel.send('Hi ' + str(message.author.nick), allowed_mentions=allowedMentions)
        else:
            allowedMentions = discord.AllowedMentions(everyone=False,roles=False,users=False)
            await message.channel.send('Hi ' + str(message.author.name), allowed_mentions=allowedMentions)
        
    if 'adi' in message.content.lower():
        await message.add_reaction('<:kiki_happy:839524132286365717>')

    if str(message.content) == f'''<@!{varsToNotCopy.bot_id}>''' or str(message.content) == f'''<@{varsToNotCopy.bot_id}>''':
        await message.channel.send('Hi! My prefix is `ink `, run `ink help` for more details!!')

    if len(message.mentions) > 0:
        for okSomeonesPing in message.mentions:
            #adi's ar
            if okSomeonesPing.id == 652756616185380894:
                await message.add_reaction('<:kiki_happy:839524132286365717>')
            #ceee's ar <3
            elif okSomeonesPing.id == 696754560429064263:
                await message.add_reaction('<:an_urcute:776896089760333844>')
            

    if 'id' == message.content.lower()[0:2]:
        if message.channel.id in varsToNotCopy.alertChannel_id:
            try:
                userToBan = int(message.content[4:22])
                userToBan = str(userToBan)
                if len(userToBan) == 18:
                    userToBan = await client.fetch_user(userToBan)
                    await message.channel.send(f"""Banning user:{userToBan.name}(#{userToBan.discriminator}) with id:{userToBan.id} for scam reported in the message {message.jump_url}""")
                    await message.guild.ban(user= userToBan,reason= 'Ink autoban for being reported by another server. [Link to alert](' + message.jump_url + ')')
                else:
                    userToBan = int(message.content[3:21])
                    userToBan = str(userToBan)
                    if len(userToBan) == 18:
                        userToBan = await client.fetch_user(userToBan)
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



    await client.process_commands(message)

myCogs = []
cogsFolderStuff = os.listdir('./cogs/')
for file in cogsFolderStuff:
    if file.endswith('.py'):
        fileName = file.split('.')
        myCogs.append(str('cogs.' + fileName[0]))

if __name__ == '__main__':
    for ext in myCogs:
        client.load_extension(ext)

#Running client on server
client.run(varsToNotCopy.token)