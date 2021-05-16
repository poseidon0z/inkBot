#importing reqs
import discord
from discord.ext import commands
from discord.ext.commands.errors import MemberNotFound
from discord.mentions import AllowedMentions
import pymongo
from pymongo.common import validate
from discord.ext.commands import MissingRequiredArgument
import secrets
from utils import simplifications

allowedMentions = discord.AllowedMentions(everyone=False,roles=False)
cluster = pymongo.MongoClient(secrets.cluster)


#cog contents
"""
Contents of this cog are:
1. Donation group, with:
    (i) gaw --> adds a specifc amount to the person's donations(used if gaw donation)
    (ii)event --> adds a specifc amount to the person's donations(used if event donation)
    (iii)special --> adds a specific amount to the person's donations(used if special celeb dono)
    (iv)check --> checks how much a member has donated
    (v)gmanlb --> to find a leaderboard of most active giveaway managers
    (vi)emanlb --> to find a leaderboard of most active event managers
    (vii)lb --> to get a leaderboard of top donators
    (viii)mine --> to find amount donated by you
    (ix)eventsheld --> to find number of events held by an event manager
    (x)giveawaysheld --> to find number of giveaways held by a gaw manager
"""
class eventStuff(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    '''
    Main group
    
    Running just the donation command gives you info on all the commands in the group
    '''
    @commands.group(name='donation', aliases=['d','dono'], invoke_without_command=True)
    @commands.check(simplifications.isNotbanned)
    @commands.guild_only()    
    async def donation(self,ctx):
        donationEmbed = discord.Embed(title='inkBot donation commands', description='',colour=0x4040bf)
        donationEmbed.add_field(name='**gaw:**', value='adds a specifc amount to the person\'s donations(used if gaw donation)',inline=False)
        donationEmbed.add_field(name='**event**:', value='adds a specifc amount to the person\'s donations(used if event donation)',inline=False)
        donationEmbed.add_field(name='**special**:', value='adds a specific amount to the person\'s donations (used if the donation was for a special celeb)',inline=False)
        donationEmbed.add_field(name='**check**:', value='checks how much a member has donated',inline=False)
        donationEmbed.add_field(name='**gmanlb**:', value='to find a leaderboard of most active giveaway managers',inline=False)
        donationEmbed.add_field(name='**emanlb**:', value='to find a leaderboard of most active event managers',inline=False)
        donationEmbed.add_field(name='**lb**:', value='to get a leaderboard of top donators',inline=False)
        donationEmbed.add_field(name='**mine**:', value='to find amount donated by you',inline=False)
        donationEmbed.add_field(name='**eventsheld**:', value='to find number of events held by an event manager',inline=False)
        donationEmbed.add_field(name='**giveawaysheld**:', value='to find number of giveaways held by a gaw manager',inline=False)
        await ctx.send(embed=donationEmbed)
    
    #Used if the donor has donated towards making a gaw
    @donation.command(name='giveaway',aliases=['gaw'])
    @commands.check(simplifications.isNotbanned)
    @commands.guild_only()    
    async def gaw_dono_add(self,ctx,target : discord.Member,amount):
        amount = float(amount)
        db = cluster['donations' + str(ctx.guild.id)]
        gman = db['serverSettings'].find_one({"_id" : 'giveawayManagerRole'})
        mod = db['serverSettings'].find_one({"_id" : 'modRole'})
        admin = db['serverSettings'].find_one({"_id" : 'adminRole'})
        allowedRoles = []
        if gman is not None:
            allowedRoles.append(gman["role"])
        if mod is not None:
            allowedRoles.append(mod["role"])
        if admin is not None:
            allowedRoles.append(admin["role"])
        hasRole = simplifications.hasAnyRole(allowedRoles,ctx.author)
        if hasRole is True:
            await simplifications.upsert(ctx,target,amount,db,'gaw')
        else:
            await ctx.send('You dont have perms!')

    @gaw_dono_add.error
    async def dono_add_error(self,ctx,error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send('Make sure to enter all required arguments by following the syntax:\n```ink dono gaw <member> <amount>```',allowed_mentions = allowedMentions)
        elif isinstance(error, MemberNotFound):
            await ctx.send('Couldnt find the member, make sure you\'re following the syntax:\n```ink dono gaw <member> <amount>```',allowed_mentions = allowedMentions)
        else:
            pass



    #Used if the donor has donated towards an event
    @donation.command(name='event')
    @commands.check(simplifications.isNotbanned)
    @commands.guild_only()    
    async def event_dono_add(self,ctx,target : discord.Member,amount):
        amount = float(amount)
        db = cluster['donations' + str(ctx.guild.id)]
        eman = db['serverSettings'].find_one({"_id" : 'eventManagerRole'})
        mod = db['serverSettings'].find_one({"_id" : 'modRole'})
        admin = db['serverSettings'].find_one({"_id" : 'adminRole'})
        allowedRoles = []
        if eman is not None:
            allowedRoles.append(eman["role"])
        if mod is not None:
            allowedRoles.append(mod["role"])
        if admin is not None:
            allowedRoles.append(admin["role"])
        hasRole = simplifications.hasAnyRole(allowedRoles,ctx.author)
        if hasRole is True:
            await simplifications.upsert(ctx,target,amount,db,'event')
        else:
            await ctx.message.reply('You dont have perms!')
    
    @event_dono_add.error
    async def event_dono_add_error(self,ctx,error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send('Make sure to enter all required arguments by following the syntax:\n```ink dono event <member> <amount>```',allowed_mentions = allowedMentions)
        elif isinstance(error, MemberNotFound):
            await ctx.send('Couldnt find the member, make sure you\'re following the syntax:\n```ink dono event <member> <amount>```',allowed_mentions = allowedMentions)
        else:
            pass



    #Used if the donor has donated towards a special celeb
    @donation.command(name='special')
    @commands.check(simplifications.isNotbanned)
    @commands.guild_only()    
    async def special_dono_add(self,ctx,target : discord.Member,amount):
        amount = float(amount)
        db = cluster['donations' + str(ctx.guild.id)]
        eman = db['serverSettings'].find_one({"_id" : 'eventManagerRole'})
        mod = db['serverSettings'].find_one({"_id" : 'modRole'})
        gman = db['serverSettings'].find_one({"_id" : 'eventManagerRole'})
        admin = db['serverSettings'].find_one({"_id" : 'adminRole'})
        allowedRoles = []
        if eman is not None:
            allowedRoles.append(eman["role"])
        if mod is not None:
            allowedRoles.append(mod["role"])
        if gman is not None:
            allowedRoles.append(gman["role"])
        if admin is not None:
            allowedRoles.append(admin["role"])
        hasRole = simplifications.hasAnyRole(allowedRoles,ctx.author)
        if hasRole is True:
            await simplifications.upsert(ctx,target,amount,db,'special')
        else:
            await ctx.message.reply('You dont have perms!')
    
    
    @special_dono_add.error
    async def special_dono_add_error(self,ctx,error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send('Make sure to enter all required arguments by following the syntax:\n```ink dono event <member> <amount>```',allowed_mentions = allowedMentions)
        elif isinstance(error, MemberNotFound):
            await ctx.send('Couldnt find the member, make sure you\'re following the syntax:\n```ink dono event <member> <amount>```',allowed_mentions = allowedMentions)
        else:
            pass
    
    #Used to check the donation by a certain member
    @donation.command(name='check')
    @commands.check(simplifications.isNotbanned)
    @commands.guild_only()    
    async def dono_check(self,ctx,target: discord.Member):
        db = cluster['donations' + str(ctx.guild.id)]
        eman = db['serverSettings'].find_one({"_id" : 'eventManagerRole'})
        mod = db['serverSettings'].find_one({"_id" : 'modRole'})
        gman = db['serverSettings'].find_one({"_id" : 'eventManagerRole'})
        admin = db['serverSettings'].find_one({"_id" : 'adminRole'})
        allowedRoles = []
        if eman is not None:
            allowedRoles.append(eman["role"])
        if mod is not None:
            allowedRoles.append(mod["role"])
        if gman is not None:
            allowedRoles.append(gman["role"])
        if admin is not None:
            allowedRoles.append(admin["role"])
        hasRole = simplifications.hasAnyRole(allowedRoles,ctx.author)
        if hasRole is True:
            await simplifications.check(ctx,target,db)
        else:
            await ctx.message.reply('You dont have perms!')
        

    #ranks giveaway managers based on activity
    @donation.command(name='giveawaymanagerleaderboard',aliases=['gmanlb', 'glb'])
    @commands.check(simplifications.isNotbanned)
    @commands.guild_only()    
    async def dono_gmanlb(self,ctx):
        db = cluster['donations' + str(ctx.guild.id)]
        admin = db['serverSettings'].find_one({"_id" : 'adminRole'})
        allowedRoles = []
        if admin is not None:
            allowedRoles.append(admin["role"])
        hasrole = simplifications.hasAnyRole(allowedRoles,ctx.author)
        if hasrole is True:
            lbEmbed = discord.Embed(title="Dank Trades Top Giveaway Managers",colour=0x4040bf)
            lbType = 'gman'
            await simplifications.lbmaker(ctx,db,lbEmbed,lbType)
            await ctx.send(embed=lbEmbed)
        else:
            await ctx.message.reply("you dont have perms")

    #ranks event managers based on activity
    @donation.command(name='eventmanagerleaderboard',aliases=['emanlb','elb'])
    @commands.check(simplifications.isNotbanned)
    @commands.guild_only()    
    async def dono_emanlb(self,ctx):
        db = cluster['donations' + str(ctx.guild.id)]
        admin = db['serverSettings'].find_one({"_id" : 'adminRole'})
        allowedRoles = []
        if admin is not None:
            allowedRoles.append(admin["role"])
        hasrole = simplifications.hasAnyRole(allowedRoles,ctx.author)
        if hasrole is True:
            lbEmbed = discord.Embed(title="Dank Trades Top Event Managers",colour=0x4040bf)
            lbType = 'eman'
            await simplifications.lbmaker(ctx,db,lbEmbed,lbType)
            await ctx.send(embed=lbEmbed)
        else:
            await ctx.message.reply("you dont have perms")
        

    #used to find the top 10 donors
    @donation.command(name='donationleaderboard',aliases=['dlb','donolb'])
    @commands.check(simplifications.isNotbanned)
    @commands.guild_only()    
    async def dono_lb(self,ctx):
        db = cluster['donations' + str(ctx.guild.id)]
        lbEmbed = discord.Embed(title="Dank Trades Top Donators",colour=0x4040bf)
        lbType = 'donations'
        await simplifications.lbmaker(ctx,db,lbEmbed,lbType)
        await ctx.send(embed=lbEmbed)

    
    #find the amound donated by you
    @donation.command(name='mine')
    @commands.check(simplifications.isNotbanned)
    @commands.guild_only()    
    async def mydono(self,ctx):
        target = ctx.author
        db = cluster['donations' + str(ctx.guild.id)]
        await simplifications.check(ctx,target,db)

    #find the number of events held by a certain event manager
    @donation.command(name='eventsheld',aliases=['eh','eheld'])
    @commands.check(simplifications.isNotbanned)
    @commands.guild_only()    
    async def eventsHeld(self,ctx,target : discord.Member):
        db = cluster['donations' + str(ctx.guild.id)]
        admin = db['serverSettings'].find_one({"_id" : 'adminRole'})
        allowedRoles = []
        if admin is not None:
            allowedRoles.append(admin["role"])
        hasrole = simplifications.hasAnyRole(allowedRoles,ctx.author)
        if hasrole is True:
            emanCol = cluster['donations' + str(ctx.guild.id)]['emanagerStats']
            targetID = target.id
            targetDetails = emanCol.find_one({'_id' : targetID})
            if targetDetails is not None:
                await ctx.message.reply(f'{target.name} has held {targetDetails["donosTaken"]} events',allowed_mentions = allowedMentions)
            else:
                await ctx.message.reply('Couldnt find any events held by this member ;-;',allowed_mentions = allowedMentions)

        else:
            await ctx.message.reply("you dont have perms")
            
    @eventsHeld.error
    async def eventsHeld_error(self,ctx,error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send(f'Make sure to enter all required arguments by following the syntax:\n```ink eventsheld <member>```',allowed_mentions = allowedMentions)
        elif isinstance(error, MemberNotFound):
            await ctx.send('Couldnt find the member, make sure you\'re following the syntax:\n```ink eventsheld <member>```',allowed_mentions = allowedMentions)


    #find the number of giveaways hosted by a certain gaw manager
    @donation.command(name='giveawaysheld',aliases=['gh', 'gawsheld'])
    @commands.check(simplifications.isNotbanned)
    @commands.guild_only()    
    async def giveawaysHeld(self,ctx,target : discord.Member):
        db = cluster['donations' + str(ctx.guild.id)]
        admin = db['serverSettings'].find_one({"_id" : 'adminRole'})
        allowedRoles = []
        if admin is not None:
            allowedRoles.append(admin["role"])
        hasrole = simplifications.hasAnyRole(allowedRoles,ctx.author)
        if hasrole is True:
            gmanCol = cluster['donations' + str(ctx.guild.id)]['gmanagerStats']
            targetID = target.id
            targetDetails = gmanCol.find_one({'_id' : targetID})
            if targetDetails is not None:
                await ctx.message.reply(f'{target.name} has hosted {targetDetails["donosTaken"]} giveaways',allowed_mentions = allowedMentions)
            else:
                await ctx.message.reply('Couldnt find any gaws held by this member ;-;',allowed_mentions = allowedMentions)


        else:
            await ctx.message.reply("you dont have perms")
            
    @giveawaysHeld.error
    async def giveawaysHeld_error(self,ctx,error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.message.reply(f'Make sure to enter all required arguments by following the syntax:\n```ink giveawaysheld <member>```',allowed_mentions = allowedMentions)
        elif isinstance(error, MemberNotFound):
            await ctx.message.reply('Couldnt find the member, make sure you\'re following the syntax:\n```ink giveawaysheld <member>```',allowed_mentions = allowedMentions)

    #reset weekly lb
    @donation.command(name='reseteventmanagers', aliases=['resetemans'])
    @commands.check(simplifications.isNotbanned)
    @commands.guild_only()
    async def resetEventManagers(self,ctx):
        db = cluster['donations' + str(ctx.guild.id)]
        admin = db['serverSettings'].find_one({"_id" : 'adminRole'})
        allowedRoles = []
        if admin is not None:
            allowedRoles.append(admin["role"])
        hasrole = simplifications.hasAnyRole(allowedRoles,ctx.author)
        if hasrole is True:
            await ctx.send('Sending backup: ')
            lbEmbed = discord.Embed(title="Dank Trades Top Event Managers",colour=0x4040bf)
            lbType = 'eman'
            await simplifications.lbmaker(ctx,db,lbEmbed,lbType)
            await ctx.send(embed=lbEmbed)
            db['emanagerStats'].drop()
            await ctx.send('Event manager leaderboard reset successfully')
        else:
            await ctx.message.reply("You dont have perms!")

    #reset weekly lb
    @donation.command(name='resetgiveawaymanagers', aliases=['resetgmans'])
    @commands.check(simplifications.isNotbanned)
    @commands.guild_only()
    async def resetGiveawayManagers(self,ctx):
        db = cluster['donations' + str(ctx.guild.id)]
        admin = db['serverSettings'].find_one({"_id" : 'adminRole'})
        allowedRoles = []
        if admin is not None:
            allowedRoles.append(admin["role"])
        hasrole = simplifications.hasAnyRole(allowedRoles,ctx.author)
        if hasrole is True:
            await ctx.send('Sending backup: ')
            lbEmbed = discord.Embed(title="Dank Trades Top Giveaway Managers",colour=0x4040bf)
            lbType = 'gman'
            await simplifications.lbmaker(ctx,db,lbEmbed,lbType)
            await ctx.send(embed=lbEmbed)
            db['gmanagerStats'].drop()
            await ctx.send('Giveaway manager leaderboard reset successfully')
        else:
            await ctx.message.reply("You dont have perms!")


#loading the cog
def setup(bot):
    bot.add_cog(eventStuff(bot))