'''
WHAT IS THIS FILE?
This is a file where i define functions that shorten certain functions, reducing the amount of repetition done in the cog itself

WHAT ARE THE FUNCTIONS HERE?
1. make_iq_embed
2. get_description
3. check_dono
4. is_an_alert_channel
5. is_a_fail_channel
6. is_ban_royale_participant
7. is_ban_royale_channel
8. is_message_mania_participant_in_channel

IMPORTS:
1. discord to define vars as discord.something type
2. random to use in finding target's iq in the make_iq_embed func, choosing a description in get_description
3. pymongo to interact with the dashboard
4. load to load my json files
5. path to show the path to my json file
'''
import discord
import random
import pymongo
from json import load
from pathlib import Path
from utils.botwideFunctions import has_role

'''
Variables used:
describe_list is a list of all descriptions among which the bot chooses one as the person's description with ink describe
cluster is the cluster my information is stored on in mongodb
embed_colour is the colour for embeds
'''
describe_list = ['a big nab','a qt','a simp','hot','friendly','an irritating bitch','an ass','a dick','a hoe','dum','tiny','the best','the poggest','sweet','cute','<:bigbrain:838472543705759824>','teeny brain','an alien','a waifu','a dumbass']
with Path("utils/secrets.json").open() as f:
    config = load(f)
cluster = pymongo.MongoClient(config["cluster"])
embed_colour = 0x52476B

'''
The 'make_iq_embed' function:
takes in a target variable and returns an embed with the iq of the invoker and their iq
'''
def make_iq_embed(target : discord.Member):
    if target.id == 652756616185380894:                 #rigging it for myself by making my iq always 160
        personIq = 160
    else:                                               #the actual function
        personIq = random.randint(a= 40, b= 160)
    
    if personIq >= 116:
        personEmoji = '<:bigbrain:838472543705759824>'
    elif personIq >= 84:
        personEmoji = ':brain:'
    elif personIq >= 40:
        personEmoji = '<:dumbfuck:838730636175998976>'
    
    iq_embed = discord.Embed(title=f'{target.name}\'s iq:',description=f'{target.mention} has an iq of {str(personIq)} {personEmoji}',color= 0x1598B7)
    return iq_embed



'''
The 'get_description' function:
Takes in a target variable and returns a description for the target
'''
def get_description(target):
    if target.id == 652756616185380894:                 #rigging it for myself by making description for my id always amazing
        description = 'amazing'
    else:                                               #the actual function
        description = random.choice(describe_list)      
    return description



'''
The 'check_dono' function:
Checks the amount donated by a member and returns an embed with the data arrangedin an embed
'''
def check_dono(target,db):
    donoCol = db['memberDonos']
    personID = target.id
    personDetails = donoCol.find_one({"_id" : personID})
    if personDetails is not None:
        try:
            totalAmount = '{:,.0f}'.format(personDetails["donoAmount"])
        except KeyError:
            totalAmount = 0
        try:
            totalGawDono = '{:,.0f}'.format(personDetails["gawDono"])
        except KeyError:
            totalGawDono = 0
        try:    
            totalEventDono = '{:,.0f}'.format(personDetails["eventDono"])
        except KeyError:
            totalEventDono = 0
        try:    
            totalSpecialDono = '{:,.0f}'.format(personDetails["specialEvents"])
        except KeyError:
            totalSpecialDono = 0
        donoEmbed = discord.Embed(title=f'{target.name}\'s donation summary: ',colour=embed_colour)
        donoEmbed.set_thumbnail(url=target.avatar_url)
        donoEmbed.add_field(name='Total donated:',value=f'> `{totalAmount}`',inline=False)
        donoEmbed.add_field(name='Donated for giveaways:', value=f'> `{totalGawDono}`',inline=False)
        donoEmbed.add_field(name='Donated for events:', value=f'> `{totalEventDono}`',inline=False)
        donoEmbed.add_field(name='Donated for special celebrations:', value=f'> `{totalSpecialDono}`',inline=False)
        return donoEmbed
    else:
        return None

'''
The 'is_an_alert_channel' function:
Checks is the channel the trigger is called is an alert channel
'''
def is_an_alert_channel(message):
    server_settings = cluster[str(message.guild.id)]['serverSettings']
    server_alert_chan_setting = server_settings.find_one({'_id' : 'alertChan'})
    if server_alert_chan_setting is not None:
        return message.channel.id == server_alert_chan_setting['channel']
    else:
        return False


'''
The 'is_a_fail_channel' function:
Checks is the channel the trigger is called is a fail channel
'''
def is_a_fail_channel(message):
    server_settings = cluster[str(message.guild.id)]['serverSettings']
    server_fail_chan_setting = server_settings.find_one({'_id' : 'failChan'})
    if server_fail_chan_setting is not None:
        return message.channel.id == server_fail_chan_setting['channel']
    else:
        return False
    
'''
The 'is_ban_royale_participant' command
Checks if the member calling rhe command has the participant role for the ban royale event
'''
def is_ban_royale_participant(ctx):
    server_settings = cluster[str(ctx.guild.id)]['eventSettings']
    try:
        br_participant_role = server_settings.find_one({'_id' : 'brParticipantRole'})['role']
        return has_role(br_participant_role,ctx.author)
    except:
        return False

'''
The 'is_ban_royale_channel' command
Checks if the command is called in the ban royale channel
'''
def is_ban_royale_channel(ctx):
    server_settings = cluster[str(ctx.guild.id)]['eventSettings']
    try: 
        br_channel = server_settings.find_one({'_id' : 'brChannel'})['channel']
        return ctx.channel.id == br_channel
    except:
        return False

'''
The 'is_message_mania_participant_in_channel' command
Checks if the command is called in the message mania channel
'''
def is_message_mania_participant_in_channel(ctx):
    server_settings = cluster[str(ctx.guild.id)]['eventSettings']
    try:
        mm_channel = server_settings.find_one({'_id' : 'mmChannel'})['channel']
    except:
        return False
    try:
        participantRole = server_settings.find_one({"_id" : 'mmParticipantRole'})["role"]
    except:
        return False
    return has_role(participantRole,ctx.author) and mm_channel == ctx.channel.id
