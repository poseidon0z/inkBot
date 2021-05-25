'''
1.WHAT IS THIS FILE?
This is a cog containing all commands for ink donation management commands

2.WHAT ARE THE COMMANDS HERE?
The Cog consists of
I Donation group, with commands:-
    (a) giveaway
    (b) event
    (c) special
    (d) check
    (e) mine
    (f) checkeman
    (g) checkgman
    (h) donorlb
    (i) emanlb
        (i) number
       (ii) amount
    (j) gmanlb
        (i) number
       (ii) amount

IMPORTS:
1. discord module to describe many of the used elements
2. commands to run the cog and its functions
3. pymongo to interact with my db
4. load to load my json
5. path to define the path to my json
6. stuff from botwide functions to add restrictions to my commands
7. check dono from commandShortenings cause its a long function
'''
import discord
from discord import colour
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from discord.ext.commands.core import command, is_owner
from discord.ext.commands.errors import BadArgument, CheckAnyFailure, ConversionError, MemberNotFound, MissingRequiredArgument
import pymongo
from json import load
from pathlib import Path
from utils.botwideFunctions import is_admin, is_gman, is_mod, is_not_bot_banned,is_eman
from utils.commandShortenings import check_dono
import asyncio

'''
VARIABLES USED:
1. embed_colour - colour of embeds used in the cog
2. allowed_mentions - mention perms allowed for messages sent for the bot
3. cluster - the cluster where the data is stored
'''
embed_colour = 0x52476B
allowed_mentions = discord.AllowedMentions(everyone=False,roles=False)

with Path("utils/secrets.json").open() as f:
    config = load(f)
cluster = pymongo.MongoClient(config["cluster"])


class inkDonationCommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    '''
    The 'donation' group
    Running this command gives information about all the subcommands here
    '''
    @commands.group(name='donation',aliases=['dono','d'],invoke_without_command=True)
    @is_not_bot_banned()
    @commands.guild_only()
    async def donation(self,ctx):
        donation_embed = discord.Embed(title='inkBot donation commands', description='Commands falling under the donation group and their functions',colour=embed_colour)
        donation_embed.add_field(name='**giveaway**:',value='Adds a certain amout to the total donation of a user (used for giveaway donations)',inline=False)
        donation_embed.add_field(name='**event**:',value='Adds a certain amout to the total donation of a user (used for event donations)',inline=False)
        donation_embed.add_field(name='**special**:',value='Adds a certain amout to the total donation of a user (used for special celebration donations)',inline=False)
        donation_embed.add_field(name='**check**:',value='Shows the donations for a member',inline=False)
        donation_embed.add_field(name='**mine**:',value='Shows your own donations',inline=False)
        donation_embed.add_field(name='**checkeman**:',value='Checks the stats for donations taken for an event manager',inline=False)
        donation_embed.add_field(name='**checkgman**:',value='Checks the stats for donations taken for a giveaway manager',inline=False)
        donation_embed.add_field(name='**emanlb**:',value='Group with 2 ways of representing most active event managers',inline=False)
        donation_embed.add_field(name='**gmanlb**:',value='Group with 2 ways of representing most active giveaway managers',inline=False)
        donation_embed.add_field(name='**clearemanlb**:',value='Clears the eman leaderboard',inline=False)
        donation_embed.add_field(name='**cleargmanlb**:',value='Clears the gman leaderboard',inline=False)
        await ctx.send(embed=donation_embed)


    '''
    The 'giveaway' command
    Running this command registers a donation from a member as a donation towards a gaw
    '''
    @donation.command(name='giveaway',aliases=['gaw'])
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.check_any(commands.is_owner(),is_admin(),is_mod(),is_gman())
    async def giveaway(self,ctx,target : discord.Member,amount : float):
        db = cluster[str(ctx.guild.id)]
        dono_collection = db['memberDonos']
        gman_collection = db['gmanagerStats']
        dono_query = {'_id' : target.id}
        gman_query = {'_id' : ctx.author.id}
        first_dono_checker = dono_collection.find_one(dono_query)
        dono_collection.update_one(dono_query,{"$inc":{"donoAmount" : amount, "gawDono" : amount}},upsert=True)
        gman_collection.update_one(gman_query,{"$inc":{"donosTaken" : 1,"amountTaken" : amount}},upsert=True)
        if first_dono_checker is None:
            await ctx.send(f'Donation has been added! tysm {target.mention} for your first donation to the server!!',allowed_mentions = allowed_mentions)
        else:
            await ctx.send(f'Donation for {target.name} has been updated!',allowed_mentions = allowed_mentions)
    
    @giveaway.error
    async def giveaway_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        elif isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink donation giveaway <member> <amount>\n\n{error.param} is not specified```')
        elif isinstance(error,MemberNotFound):
            await ctx.send(f'Couldn\'t find the member "{error.argument}" <:lotsofpain:839371861346222112>',allowed_mentions=allowed_mentions)
        elif isinstance(error,BadArgument):
            await ctx.send(f'Couldn\'t find a amount from the given argument')
        else:
            print(error)
    
    '''
    The 'event' command
    Running this command registers a donation form a member as a donation towards an event
    '''
    @donation.command(name='event')
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.check_any(commands.is_owner(),is_admin(),is_mod(),is_eman())
    async def event(self,ctx,target : discord.Member,amount : float):
        db = cluster[str(ctx.guild.id)]
        dono_collection = db['memberDonos']
        eman_collection = db['emanagerStats']
        dono_query = {'_id' : target.id}
        eman_query = {'_id' : ctx.author.id}
        first_dono_checker = dono_collection.find_one(dono_query)
        dono_collection.update_one(dono_query,{"$inc":{"donoAmount" : amount, "eventDono" : amount}},upsert=True)
        eman_collection.update_one(eman_query,{"$inc":{"donosTaken" : 1,"amountTaken" : amount}},upsert=True)
        if first_dono_checker is None:
            await ctx.send(f'Donation has been added! tysm {target.mention} for your first donation to the server!!',allowed_mentions = allowed_mentions)
        else:
            await ctx.send(f'Donation for {target.name} has been updated!',allowed_mentions = allowed_mentions)
    

    @event.error
    async def event_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        elif isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink donation event <member> <amount>\n\n{error.param} is not specified```')
        elif isinstance(error,MemberNotFound):
            await ctx.send(f'Couldn\'t find the member "{error.argument}" <:lotsofpain:839371861346222112>',allowed_mentions=allowed_mentions)
        elif isinstance(error,BadArgument):
            await ctx.send(f'Couldn\'t find a amount from the given argument')
        else:
            print(error)

    '''
    The 'special' command
    Running this command registers a donation form a member as a donation towards a special celebrations
    '''
    @donation.command(name='special')
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.check_any(commands.is_owner(),is_admin(),is_mod(),is_eman(),is_gman())
    async def special(self,ctx,target : discord.Member,amount : float):
        db = cluster[str(ctx.guild.id)]
        dono_collection = db['memberDonos']
        dono_query = {'_id' : target.id}
        first_dono_checker = dono_collection.find_one(dono_query)
        dono_collection.update_one(dono_query,{"$inc":{"donoAmount" : amount, "specialEvents" : amount}},upsert=True)
        if first_dono_checker is None:
            await ctx.send(f'Donation has been added! tysm {target.mention} for your first donation to the server!!',allowed_mentions = allowed_mentions)
        else:
            await ctx.send(f'Donation for {target.name} has been updated!',allowed_mentions = allowed_mentions)

    @special.error
    async def special_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        elif isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink donation special <member> <amount>\n\n{error.param} is not specified```')
        elif isinstance(error,MemberNotFound):
            await ctx.send(f'Couldn\'t find the member "{error.argument}" <:lotsofpain:839371861346222112>',allowed_mentions=allowed_mentions)
        elif isinstance(error,BadArgument):
            await ctx.send(f'Couldn\'t find a amount from the given argument')
        else:
            print(error)
    
    '''
    The 'check' command
    Running this command checks the donation of a user
    '''
    @donation.command(name='check')
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.check_any(commands.is_owner(),is_admin(),is_mod(),is_eman(),is_gman())
    async def check(self,ctx,target : discord.User):
        db = cluster[str(ctx.guild.id)]
        donovalue = check_dono(target,db)
        if donovalue is not None:
            await ctx.send(embed=donovalue)
        else:
            await ctx.send('Coundnt find any logged donations for this member ;-;',allowed_mentions = allowed_mentions)

    @check.error
    async def check_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        elif isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink donation check <member>\n\n{error.param} is not specified```')
        elif isinstance(error,MemberNotFound):
            await ctx.send(f'Couldn\'t find the member "{error.argument}" <:lotsofpain:839371861346222112>',allowed_mentions=allowed_mentions)
        else:
            print(error)
    '''
    The 'mine' command
    Used to check own donation
    '''
    @donation.command(name='mine')
    @is_not_bot_banned()
    @commands.guild_only()
    async def mine(self,ctx):
        db = cluster[str(ctx.guild.id)]
        dono_embed = check_dono(ctx.author,db)
        if dono_embed is not None:
            await ctx.send(embed=dono_embed)
        else:
            await ctx.send('Coundnt find any logged donations for this member ;-;',allowed_mentions = allowed_mentions)

    '''
    The 'checkeman' command:
    Checks the stats for donations taken for an event manager
    '''
    @commands.command(name='checkeman')
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.check_any(commands.is_owner(),is_admin())
    async def check_eman(self,ctx,eman : discord.Member):
        eman_stats = cluster[str(ctx.guild.id)]['emanagerStats']
        targetDetails = eman_stats.find_one({'_id' : eman.id})
        if targetDetails is not None:
            eman_stats_embed = discord.Embed(title=f'Event manager stats for {eman.name}',colour=embed_colour)
            eman_stats_embed.add_field(name='Events donos taken:',value=targetDetails['donosTaken'],inline=False)
            eman_stats_embed.add_field(name='Amount collected:',value=targetDetails['amountTaken'],inline=False)
        else:
            await ctx.message.reply('Couldnt find any events held by this member ;-;')
    
    @check_eman.error
    async def check_eman_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        elif isinstance(error,MemberNotFound):
            await ctx.send(f'Couldn\'t find the member "{error.argument}" <:lotsofpain:839371861346222112>',allowed_mentions=allowed_mentions)
        elif isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink donation checkeman <member>\n\n{error.param} is not specified```',allowed_mentions=allowed_mentions)
        else:
            print(error)

    
    '''
    The 'checkgman' command:
    Checks the stats for donations taken for a giveaway manager
    '''
    @commands.command(name='checkgman')
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.check_any(commands.is_owner(),is_admin())
    async def check_gman(self,ctx,gman : discord.Member):
        gman_stats = cluster[str(ctx.guild.id)]['gmanagerStats']
        targetDetails = gman_stats.find_one({'_id' : gman.id})
        if targetDetails is not None:
            gman_stats_embed = discord.Embed(title=f'Giveaway manager stats for {gman.name}',colour=embed_colour)
            gman_stats_embed.add_field(name='Giveaways held:',value=targetDetails['donosTaken'],inline=False)
            gman_stats_embed.add_field(name='Amount collected:',value=targetDetails['amountTaken'],inline=False)
        else:
            await ctx.message.reply('Couldnt find any giveaways held by this member ;-;')
    
    @check_gman.error
    async def check_gman_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        elif isinstance(error,MemberNotFound):
            await ctx.send(f'Couldn\'t find the member "{error.argument}" <:lotsofpain:839371861346222112>',allowed_mentions=allowed_mentions)
        elif isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink donation checkgman <member>\n\n{error.param} is not specified```',allowed_mentions=allowed_mentions)
        else:
            print(error)
        



    '''
    The 'donorlb' command
    Gives a leaderboard consisting of the top 10 donors
    '''
    @donation.command(name='donorlb',aliases=['donolb'])
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.cooldown(1,30,BucketType.user)
    async def donorlb(self,ctx):
        db = cluster[str(ctx.guild.id)]
        donor_collection = db['memberDonos']
        raw_lb = donor_collection.find().limit(10).sort('donoAmount',-1)
        lb_embed = discord.Embed(title=f'{ctx.guild.name} top donors!',colour=embed_colour)
        i = 1
        for donor_data in raw_lb:
            if donor_data is not None:
                donor_id = int(donor_data["_id"])
                donor = await ctx.guild.fetch_member(donor_id)
                amount_donated = '{:,.0f}'.format(donor_data['donoAmount'])
                lb_embed.add_field(name=f'**#{i}**', value=f'> Donor name: {donor.name} `({donor.id})`\n> Amount donated: `{amount_donated}`',inline=False)



    '''
    The 'emanlb' group
    Gives a leaderboard ranking event managers
    '''
    @donation.group(name='emanlb',invoke_without_command=True)
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.check_any(is_owner(),is_admin())
    async def emanlb(self,ctx):
        emanlb_embed = discord.Embed(title='emanlb types',colour=embed_colour)
        emanlb_embed.add_field(name='number',value='Gives a leaderboad ranking the event managers according to number of donations taken',inline=False)
        emanlb_embed.add_field(name='amount',value='Gives a leaderboard ranking the event managers according to amount in donations collected',inline=False)
        await ctx.send(embed=emanlb_embed)

    @emanlb.error
    async def emanlb_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        else:
            print(error)

    '''
    The 'number' command
    Gives a leaderboad ranking the event managers according to number of donations taken
    '''
    @emanlb.command(name='number',aliases=['num'])
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.check_any(is_owner(),is_admin())
    async def emanlb_by_number(self,ctx):
        db = cluster[str(ctx.guild.id)]
        eman_collection = db['emanagerStats']
        raw_lb = eman_collection.find().sort('donosTaken',-1)
        lb_embed = discord.Embed(title=f'{ctx.guild.name}\'s top event managers!',colour=embed_colour)
        i = 1
        for eman_data in raw_lb:
            if eman_data is not None:
                eman_id = int(eman_data["_id"])
                eman = await ctx.guild.fetch_member(eman_id)
                donos_taken = '{:,.0f}'.format(eman_data['donosTaken'])
                lb_embed.add_field(name=f'**#{i}**', value=f'> Manager name: {eman.name} `({eman.id})`\n> Donations taken: `{donos_taken}`',inline=False)
        await ctx.send(embed=lb_embed)

    @emanlb_by_number.error
    async def emanlb_by_number_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        else:
            print(error)

    '''
    The 'amount' command
    Gives a leaderboard ranking the event managers according to amount in donations collected
    '''
    @emanlb.command(name='amount',aliases=['amt'])
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.check_any(is_owner(),is_admin())
    async def emanlb_by_amount(self,ctx):
        db = cluster[str(ctx.guild.id)]
        eman_collection = db['emanagerStats']
        raw_lb = eman_collection.find().sort('amountTaken',-1)
        lb_embed = discord.Embed(title=f'{ctx.guild.name}\'s top event managers!',colour=embed_colour)
        i = 1
        for eman_data in raw_lb:
            if eman_data is not None:
                eman_id = int(eman_data["_id"])
                eman = await ctx.guild.fetch_member(eman_id)
                amount_collected = '{:,.0f}'.format(eman_data['amountTaken'])
                lb_embed.add_field(name=f'**#{i}**', value=f'> Manager name: {eman.name} `({eman.id})`\n> Donation amount collected: `{amount_collected}`',inline=False)
        await ctx.send(embed=lb_embed)
    
    @emanlb_by_amount.error
    async def emanlb_by_amount_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        else:
            print(error)

    '''
    The 'gmanlb' group
    Gives a leaderboard ranking giveaway managers
    '''
    @donation.group(name='gmanlb',invoke_without_command=True)
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.check_any(is_owner(),is_admin())
    async def gmanlb(self,ctx):
        gmanlb_embed = discord.Embed(title='gmanlb types',colour=embed_colour)
        gmanlb_embed.add_field(name='number',value='Gives a leaderboad ranking the giveaway managers according to number of gaws held',inline=False)
        gmanlb_embed.add_field(name='amount',value='Gives a leaderboard ranking the giveaway managers according to amount in donations collected',inline=False)
        await ctx.send(embed=gmanlb_embed)

    @gmanlb.error
    async def gmanlb_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        else:
            print(error)

    '''
    The 'number' command
    Gives a leaderboad ranking the giveaway managers according to number of donations taken
    '''
    @gmanlb.command(name='number',aliases=['num'])
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.check_any(is_owner(),is_admin())
    async def gmanlb_by_number(self,ctx):
        db = cluster[str(ctx.guild.id)]
        gman_collection = db['gmanagerStats']
        raw_lb = gman_collection.find().sort('donosTaken',-1)
        lb_embed = discord.Embed(title=f'{ctx.guild.name}\'s top giveaway managers!',colour=embed_colour)
        i = 1
        for gman_data in raw_lb:
            if gman_data is not None:
                gman_id = int(gman_data["_id"])
                gman = await ctx.guild.fetch_member(gman_id)
                donos_taken = '{:,.0f}'.format(gman_data['donosTaken'])
                lb_embed.add_field(name=f'**#{i}**', value=f'> Manager name: {gman.name} `({gman.id})`\n> Donations taken: `{donos_taken}`',inline=False)
        await ctx.send(embed=lb_embed)

    @gmanlb_by_number.error
    async def gmanlb_by_number_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        else:
            print(error)

    '''
    The 'amount' command
    Gives a leaderboard ranking the giveaway managers according to amount in donations collected
    '''
    @gmanlb.command(name='amount',aliases=['amt'])
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.check_any(is_owner(),is_admin())
    async def gmanlb_by_amount(self,ctx):
        db = cluster[str(ctx.guild.id)]
        gman_collection = db['gmanagerStats']
        raw_lb = gman_collection.find().sort('amountTaken',-1)
        lb_embed = discord.Embed(title=f'{ctx.guild.name}\'s top giveaway managers!',colour=embed_colour)
        i = 1
        for gman_data in raw_lb:
            if gman_data is not None:
                gman_id = int(gman_data["_id"])
                gman = await ctx.guild.fetch_member(gman_id)
                amount_collected = '{:,.0f}'.format(gman_data['amountTaken'])
                lb_embed.add_field(name=f'**#{i}**', value=f'> Manager name: {gman.name} `({gman.id})`\n> Donation amount collected: `{amount_collected}`',inline=False)
        await ctx.send(embed=lb_embed)    

    @gmanlb_by_amount.error
    async def gmanlb_by_amount_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        else:
            print(error)

    '''
    The 'clearemanlb' command:
    Clears the event manager leaderboard (helpful to check weekly activity etc.)
    '''
    @donation.command(name='clearemanlb',aliases=['cleareman'])
    @is_not_bot_banned()
    @commands.check_any(is_owner(),is_admin())
    async def clear_eman_lb(self,ctx):
        confirmation_message  = await ctx.send(f'This will clear the event manager leaderboard for {ctx.guild.name}! are you sure you wanna do this? React with <a:check:845936436297728030> to confirm or <:cancel:845945583835283487> to cancel!',allowed_mentions=allowed_mentions)
        await confirmation_message.add_reaction('<a:check:845936436297728030>')
        await confirmation_message.add_reaction('<:cancel:845945583835283487>')
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ['<a:check:845936436297728030>','<:cancel:845945583835283487>']
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=10.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('Cancelling....')
        else:
            if str(reaction.emoji) == '<a:check:845936436297728030>':
                await ctx.send('Clearing stats...')
                db = cluster[str(ctx.guild.id)]
                eman_collection = db['emanagerStats']
                eman_collection.drop()
                await ctx.send('Cleared!')
            if str(reaction.emoji) == '<:cancel:845945583835283487>':
                await ctx.send('Cancelling....')

    @clear_eman_lb.error
    async def clear_eman_lb_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        else:
            print(error)

    '''
    The 'cleargmanlb' command:
    Clears the giveaway manager leaderboard (helpful to check weekly activity etc.)
    '''
    @donation.command(name='cleargmanlb',aliases=['cleargman'])
    @is_not_bot_banned()
    @commands.check_any(is_owner(),is_admin())
    async def clear_gman_lb(self,ctx):
        confirmation_message  = await ctx.send(f'This will clear the giveawway manager leaderboard for {ctx.guild.name}! are you sure you wanna do this? React with <a:check:845936436297728030> to confirm or <:cancel:845945583835283487> to cancel!!',allowed_mentions=allowed_mentions)
        await confirmation_message.add_reaction('<a:check:845936436297728030>')
        await confirmation_message.add_reaction('<:cancel:845945583835283487>')
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ['<a:check:845936436297728030>','<:cancel:845945583835283487>']
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=10.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('Cancelling....')
        else:
            if str(reaction.emoji) == '<a:check:845936436297728030>':
                await ctx.send('Clearing stats...')
                db = cluster[str(ctx.guild.id)]
                gman_collection = db['gmanagerStats']
                gman_collection.drop()
                await ctx.send('Cleared!')
            if str(reaction.emoji) == '<:cancel:845945583835283487>':
                await ctx.send('Cancelling....')

    @clear_gman_lb.error
    async def clear_gman_lb_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        else:
            print(error)

    

def setup(bot):
    bot.add_cog(inkDonationCommands(bot))
    print("""Cog inkDonationCommands has loaded successfully
--------------------""")