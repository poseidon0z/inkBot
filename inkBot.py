#importing the discord package
import discord
from discord.ext import commands
import random
import inkFunCommands
import time
import inkServerManageCommands
import varsToNotCopy
from discord.ext.commands import MemberNotFound

# Client (my bot)
client = commands.Bot(command_prefix = ['ink ', 'ink', 'Ink'])
client.remove_command('help')


#doing stuff

#vars for the bot
botVars_describeList = inkFunCommands.describeList
botVars_pickupLines = inkFunCommands.pickupLines

#message sent in bot status when bot comes on
@client.event
async def on_ready():
    item_channel = client.get_channel(838425596421079060)
    await item_channel.send('bot is up! <:yayy:838430088738504725>')

#message sent in bot status when bot goes down
@client.event
async def on_disconnect():
    item_channel = client.get_channel(838425596421079060)
    await item_channel.send('bot is now down <:sad:838430133537734737>')

#help command
@client.group(name="help",invoke_without_command=True)
async def help_cmd(context):
    helpEmbed = discord.Embed(Title="inkBot help",description='Say `ink help <command>` for more info about a particular command',colour=0x9933ff)
    helpEmbed.add_field(name='Fun',value='`say`,`describe`,`hi`,`help`,`iq`,`besmooth`,`ping`,`8ball`',inline=False)
    helpEmbed.add_field(name='Server Utils',value='`whois`,`info`',inline=False)
    helpEmbed.add_field(name='Server Config',value='`autobanScammers`',inline=False)
    helpEmbed.set_footer(text='bot by Adi#1874')
    await context.message.channel.send(embed=helpEmbed)

@help_cmd.command()
async def say(context):
    helpEmbed = discord.Embed(title='Say command',colour=0x9933ff)
    helpEmbed.add_field(name='Feature', value='Makes the bot repeat something for you',inline=False)
    helpEmbed.add_field(name='Syntax',value='`ink say <your_text>`',inline=False)
    await context.message.channel.send(embed=helpEmbed)

@help_cmd.command()
async def describe(context):
    helpEmbed = discord.Embed(title='Describe command',colour=0x9933ff)
    helpEmbed.add_field(name='Feature', value='Makes the bot describe the person you ping',inline=False)
    helpEmbed.add_field(name='Syntax',value='`ink describe <target>`',inline=False)
    helpEmbed.add_field(name='Xtra Feature:', value='type `ink describe list` to see list of possible descriptions',inline=False)
    await context.message.channel.send(embed=helpEmbed)

@help_cmd.command()
async def hi(context):
    helpEmbed = discord.Embed(title='hi ink command',colour=0x9933ff)
    helpEmbed.add_field(name='Feature', value='Makes the bot reply with a hi',inline=False)
    helpEmbed.add_field(name='Syntax',value='`hi ink`',inline=False)
    await context.message.channel.send(embed=helpEmbed)

@help_cmd.command()
async def help(context):
    helpEmbed = discord.Embed(title='Help command',colour=0x9933ff)
    helpEmbed.add_field(name='Feature', value='Opens the `ink help` embed to see all ink features and find out how to use them',inline=False)
    helpEmbed.add_field(name='Syntax',value='`ink help`',inline=False)
    await context.message.channel.send(embed=helpEmbed)

@help_cmd.command()
async def iq(context):
    helpEmbed = discord.Embed(title='Iq command',colour=0x9933ff)
    helpEmbed.add_field(name='Feature', value='Generates a random value to be the iq for the user mentioned',inline=False)
    helpEmbed.add_field(name='Syntax',value='`ink iq <target>`',inline=False)
    await context.message.channel.send(embed=helpEmbed)

@help_cmd.command()
async def besmooth(context):
    helpEmbed = discord.Embed(title='besmooth command',colour=0x9933ff)
    helpEmbed.add_field(name='Feature', value='Generates a random pickup line',inline=False)
    helpEmbed.add_field(name='Syntax',value='`ink besmooth`',inline=False)
    await context.message.channel.send(embed=helpEmbed)

@help_cmd.command()
async def ping(context):
    helpEmbed = discord.Embed(title='Ping command',colour=0x9933ff)
    helpEmbed.add_field(name='Feature', value='Gives a message telling you the ping you\'re getting at that time',inline=False)
    helpEmbed.add_field(name='Syntax',value='`ink ping`',inline=False)
    await context.message.channel.send(embed=helpEmbed)

@help_cmd.command(name = '8ball')
async def eightball(context):
    helpEmbed = discord.Embed(title='8ball command',colour=0x9933ff)
    helpEmbed.add_field(name='Feature', value='Predict the future <a:winks:839524896270319707>',inline=False)
    helpEmbed.add_field(name='Syntax',value='`ink 8ball <what you want predicted>`',inline=False)
    await context.message.channel.send(embed=helpEmbed)

@help_cmd.command()
async def whois(context):
    helpEmbed = discord.Embed(title='Whois command',colour=0x9933ff)
    helpEmbed.add_field(name='Feature', value='Gives info on a user regardless of wether they are in the server(Use `ink info` for more detailed info on a user in the server)',inline=False)
    helpEmbed.add_field(name='Syntax',value='`ink whois <user>`',inline=False)
    await context.message.channel.send(embed=helpEmbed)

@help_cmd.command()
async def info(context):
    helpEmbed = discord.Embed(title='Info command',colour=0x9933ff)
    helpEmbed.add_field(name='Feature', value='Gives detailed info on a user in the server(Use `ink whois` for info on a user regardless of wether they are in the server )',inline=False)
    helpEmbed.add_field(name='Syntax',value='`ink info <user>`',inline=False)
    await context.message.channel.send(embed=helpEmbed)

@help_cmd.command()
async def autobanScammers(context):
    helpEmbed = discord.Embed(title='Autoban scammers',colour=0x9933ff)
    helpEmbed.add_field(name='Feature', value='Automatically bans members that are reported in the alert channels of various servers',inline=False)
    helpEmbed.add_field(name='Setup',value='You have to dm Adi for this till he learns to set up global vars',inline=False)
    await context.message.channel.send(embed=helpEmbed)



#command to echo
@client.command(name = 'say')
async def say(context, *, whatToSay):
    await inkFunCommands.say(context,whatToSay)

#gives a description of the person mentioned
@client.command(name = 'describe')
async def describe(context, target : discord.Member):
    await inkFunCommands.describe(context,target)

@describe.error
async def describe_error(cxt, error):
    if isinstance(error, MemberNotFound):
        await cxt.channel.send('Oi gimme an actual member to describe <a:PI_Angry:838736380674572328>')

#iq command
@client.command(name = 'iq')
async def iq(context,target : discord.Member):
    await inkFunCommands.iq(context, target)


@iq.error
async def iq_error(cxt, error):
    if isinstance(error, MemberNotFound):
        await cxt.channel.send('Oi gimme an actual member to find iq of <a:PI_Angry:838736380674572328>')

#flirt command
@client.command(name = 'besmooth')
async def besmooth(context):
    await inkFunCommands.besmooth(context)

#whois feature
@client.command(name = 'whois')
async def whois(context, target : discord.User):
    await inkServerManageCommands.whois(context,target)

#info feature
@client.command(name = 'info')
async def info(context, target : discord.Member):
    print('info command called')
    await inkServerManageCommands.info(context,target)

#ping command
@client.command(name = 'ping')
async def ping(content):
    await content.channel.send(f"""Ping is {round(client.latency * 1000)}ms""")

#8ball cmd
@client.command(name = '8ball')
async def eightball(cxt, *,toPredict):
    await inkFunCommands.eightball(cxt, toPredict)

@eightball.error
async def eightball_error(cxt, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await cxt.channel.send('Give me something to predict <:facepalm:838671083481333781>')

    
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
        
    elif 'adi' in message.content.lower():
        await message.add_reaction('<:kiki_happy:839524132286365717>')

    elif str(message.content) == f'''<@!{varsToNotCopy.bot_id}>''':
        await message.channel.send('Hi! My prefix is `ink `, run `ink help` for more details!!')

    elif len(message.mentions) > 0:
        for okSomeonesPing in message.mentions:
            #adi's ar
            if okSomeonesPing.id == 652756616185380894:
                await message.add_reaction('<:kiki_happy:839524132286365717>')
            #ceee's ar <3
            elif okSomeonesPing.id == 696754560429064263:
                await message.add_reaction('<:an_urcute:776896089760333844>')
            

    elif 'id' == message.content.lower()[0:2]:
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

#Running client on server
client.run(varsToNotCopy.token)