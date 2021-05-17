#imports
import discord
from discord.ext.commands import bot
import pymongo
import secrets
from discord.ext import commands

allowedMentions = discord.AllowedMentions(everyone=False,roles=False)

def isNotTrades(ctx):
    return ctx.message.guild.id != 719180744311701505

def isNotbanned(ctx):
    cluster = pymongo.MongoClient(secrets.cluster)
    bannedInfo = cluster['banned']['Ids']
    x = bannedInfo.find()
    bannedList = []
    for item in x:
        if item is not None:
            bannedMember = item['_id']
            bannedList.append(bannedMember)
    return ctx.author.id not in bannedList

def isAnAlertChannel(message):
    cluster = pymongo.MongoClient(secrets.cluster)
    serverSettingsCol = cluster[str(message.guild.id)]['serverSettings']
    x = serverSettingsCol.find_one({"_id" : 'alertChan'})
    if x is not None:
        alertChannel = x["channel"]
    else:
        alertChannel = 'abcd'
    if message.channel.id == alertChannel:
        return True
    else:
        return False

def isAFailChannel(message):
    cluster = pymongo.MongoClient(secrets.cluster)
    serverSettingsCol = cluster[str(message.guild.id)]['serverSettings']
    x = serverSettingsCol.find_one({"_id" : 'failChan'})
    if x is not None:
        failChannel = x["channel"]
    else:
        failChannel = 'abcd'
    if message.channel.id == failChannel:
        return True
    else:
        return False

def isProbablyAnAlert(message):
    firstTwoLetter = message.content.lower()[0:2]
    return 'id' == firstTwoLetter

def addToEman(id,db):
    emanCol = db['emanagerStats']
    manID = id
    query ={"_id" : manID}
    status = emanCol.find_one(query)
    if status is None:
        emanCol.insert_one({"_id" : manID, "donosTaken" : 1})
    else:
        newDonosTaken = status['donosTaken'] + 1
        emanCol.update_one(query,{"$set":{"donosTaken" : newDonosTaken}})

def addToGman(id,db):
    gmanCol = db['gmanagerStats']
    manID = id
    query ={"_id" : manID}
    status = gmanCol.find_one(query)
    if status is None:
        gmanCol.insert_one({"_id" : manID, "donosTaken" : 1})
    else:
        newDonosTaken = status['donosTaken'] + 1
        gmanCol.update_one(query,{"$set":{"donosTaken" : newDonosTaken}})

async def upsert(ctx,target,amount,db,type):
    donoCol = db['memberDonos']
    targetID = target.id
    query = {'_id' : targetID}
    status = donoCol.find_one(query)
    if status is None:
        if type == 'gaw':
            donoCol.insert_one({"_id" : targetID, "donoAmount" : amount, "gawDono" : amount, 'eventDono' : 0, 'specialEvents' : 0})
            addToGman(ctx.author.id,db)
        elif type == 'event':
            donoCol.insert_one({"_id" : targetID, "donoAmount" : amount, 'gawDono' : 0,"eventDono" : amount, 'speacialEvents' : 0})
            addToEman(ctx.author.id,db)
        elif type == 'special':
            donoCol.insert_one({"_id" : targetID, "donoAmount" : amount, 'gawDono' : 0,"eventDono" : 0, 'speacialEvents' : amount})
        await ctx.message.reply(f"Donation has been added! tysm {target.mention} for your first donation to the server!!",allowed_mentions = allowedMentions)
    else:
        if type == 'gaw':
            newamount = status["donoAmount"] + amount
            newgawDono = int(status['gawDono']) + amount
            donoCol.update_one(status,{"$set":{"donoAmount" : newamount,"gawDono" : newgawDono}})
            addToGman(ctx.author.id,db)
        elif type == 'event':
            newamount = status["donoAmount"] + amount
            neweventDono = int(status['eventDono']) + amount
            donoCol.update_one(status,{"$set":{"donoAmount" : newamount,"eventDono" : neweventDono}})
            addToEman(ctx.author.id,db)
        elif type == 'special':
            newamount = status["donoAmount"] + amount
            newspecialDono = int(status['specialEvents']) + amount
            donoCol.update_one(status,{"$set":{"donoAmount" : newamount,"specialEvents" : newspecialDono}})
        await ctx.message.reply(f"Donation for {target.name} has been updated",allowed_mentions = allowedMentions)

async def check(ctx,target,db):
    donoCol = db['memberDonos']
    personID = target.id
    personDetails = donoCol.find_one({"_id" : personID})
    if personDetails is not None:
        try:
            totalAmount = '{:,.2f}'.format(personDetails["donoAmount"])
        except KeyError:
            totalAmount = 0
        try:
            totalGawDono = '{:,.2f}'.format(personDetails["gawDono"])
        except KeyError:
            totalGawDono = 0
        try:    
            totalEventDono = '{:,.2f}'.format(personDetails["eventDono"])
        except KeyError:
            totalEventDono = 0
        try:    
            totalSpecialDono = '{:,.2f}'.format(personDetails["specialEvents"])
        except KeyError:
            totalEventDono = 0
        donoEmbed = discord.Embed(title=f'{target.name}\'s donation summary: ',colour=0x00bfff)
        donoEmbed.set_thumbnail(url=target.avatar_url)
        donoEmbed.add_field(name='Total donated:',value=f'> `{totalAmount}`',inline=False)
        donoEmbed.add_field(name='Donated for giveaways:', value=f'> `{totalGawDono}`',inline=False)
        donoEmbed.add_field(name='Donated for events:', value=f'> `{totalEventDono}`',inline=False)
        donoEmbed.add_field(name='Donated for special celebrations:', value=f'> `{totalSpecialDono}`',inline=False)
        await ctx.send(embed=donoEmbed)
    else:
        await ctx.send(f'Coundnt find any logged donations for this member ;-;',allowed_mentions = allowedMentions)

async def lbmaker(ctx,db,lbEmbed,type):
    gmanCol = db['gmanagerStats']
    emanCol = db['emanagerStats']
    donoCol = db['memberDonos']
    if type == "gman":
        nameField = 'Giveaway Manager'
        numField = 'Number of giveaways hosted'
        lbRaw = gmanCol.find().sort("donosTaken", -1)
        requiredData = 'donosTaken'
    elif type == "eman":
        nameField = 'Event Manager'
        numField = 'Number of event donations taken'
        lbRaw = emanCol.find().sort("donosTaken", -1)
        requiredData = 'donosTaken'
    elif type == 'donations':
        nameField = 'Donor'
        numField = 'Amount donated'
        lbRaw = donoCol.find().limit(10).sort("donoAmount", -1)
        requiredData = 'donoAmount'
    i = 1
    for manData in lbRaw:
            if manData is not None:
                manID = int(manData["_id"])
                man = await ctx.guild.fetch_member(manID)
                manName = man.name
                manValue = manData[requiredData]
                manvalue = '{:,.0f}'.format(manValue)
                lbEmbed.add_field(name=f'**#{i}**', value=f'> {nameField} : {manName} `({manID})`\n> {numField} : `{manvalue}`',inline=False)
                i += 1

def hasAnyRole(allowedList,author : discord.Member):
    authorRoles = [] 
    for role in author.roles:
        authorRoles.append(role.id)
    if len(set(allowedList).intersection(authorRoles)) >= 1:
        return True
    elif author.id == 652756616185380894:
        return True
    else:
        return False