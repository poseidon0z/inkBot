'''
WHAT IS THIS FILE?
This is the file with all commands needed for the ban roulette event with inkbot

WHAT ARE THE COMMANDS HERE?
1. ban_roulette_ban
2. banlb
3. clearlb
'''
import asyncio
from discord.ext.commands.core import has_guild_permissions, is_owner
from discord.ext.commands.errors import CheckAnyFailure, CheckFailure, MissingRequiredArgument
from utils.botwideFunctions import has_role, is_manager, is_not_bot_banned
from utils.commandShortenings import is_ban_royale_channel, is_ban_royale_participant
import discord
from discord.ext import commands
from json import load
import pymongo
from pathlib import Path
from timeit import default_timer as timer

with Path("utils/secrets.json").open() as f:
    config = load(f)

'''
VARIABLES:
config (defined above) the json file storing bot data
embed_colour = the embed colour used in all embeds in this cog
cluster = the cluster in which db stuff is saved
'''
embed_colour = 0xabcdef
cluster = pymongo.MongoClient(config["cluster"])

class banRoulette(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name='brb')
    @commands.guild_only()
    @commands.check(is_ban_royale_channel)
    @commands.check(is_ban_royale_participant)
    @is_not_bot_banned()
    async def brb(self, ctx, target : discord.Member):
        settings_db = cluster[str(ctx.guild.id)]
        settings_col = settings_db['eventSettings']
        play_role = settings_col.find_one({'_id' : 'brParticipantRole'})['role']
        staff_role = settings_col.find_one({'_id' : 'brStaffRole'})['role']
        bancount = settings_db['banCount']
        if has_role(staff_role,target) == False:
            if has_role(play_role,target) == True:
                role = ctx.guild.get_role(play_role)
                await target.remove_roles(role)
                await ctx.channel.send(f'{ctx.author.mention} banned {target.mention}!')
                authorID = ctx.author.id
                status = bancount.find_one({'_id' : authorID})
                if status is None:
                    person = {'_id' : authorID , "numberOfBans": 1}
                    bancount.insert_one(person)
                else:
                    myquery = {'_id' : authorID}
                    newBanNumber = status['numberOfBans'] + 1
                    bancount.update_one(myquery,{"$set":{"numberOfBans": newBanNumber}})
            else:
                await ctx.reply(f'Don\'t try banning someone who can\'t participate <a:slowkek:838803911686750209>')
        else:
            await ctx.reply(f'You can\'t ban staff BAHAHAHAHA')

    @brb.error
    async def brb_error(self,ctx,error,rerun=False):
        if rerun == True:
            if isinstance(error, CheckFailure):
                await ctx.reply('You don\'t have the roles required to run this command or are using it in the wrong channel')
            if isinstance(error,MissingRequiredArgument):
                await ctx.reply(f'Make sure to use the correct format and provide all required args: ```ink brb <target>\n\n{error}```')
            else:
                return False
        elif rerun == False:
            pass

    @commands.command(name='banlb')
    @commands.guild_only()
    @commands.check_any(has_guild_permissions(administrator=True),is_owner(),is_manager())
    @is_not_bot_banned()
    async def banlb(self,ctx):
        bancollection = cluster[str(ctx.guild.id)]['banCount']
        lbRaw = bancollection.find().limit(10).sort("numberOfBans", -1)
        i = 1
        lbEmbed = discord.Embed(title=f'{ctx.guild.name} Leaderboard',colour=0xabcdef)
        for personData in lbRaw:
            if personData is not None:
                personId = int(personData["_id"])
                person = await self.bot.fetch_user(personId)
                personName = person.name
                personBans = personData["numberOfBans"]
                lbEmbed.add_field(name=f'**#{i}**',value=f'> Member = {personName}\n> ID = {personId}\n> Number of bans = {personBans}',inline=False)
                i += 1
        await ctx.send(embed=lbEmbed)
    
    @banlb.error
    async def banlb_error(self,ctx,error,rerun=False):
        if rerun == True:
            if isinstance(error, CheckAnyFailure):
                await ctx.reply('You need administrator or manage guild perms to run this command (or manager role)')
            else:
                return False
        elif rerun == False:
            pass

    @commands.command(name='clearbanlb')
    @commands.guild_only()
    @is_not_bot_banned()
    @commands.check_any(has_guild_permissions(administrator=True),is_owner(),is_manager())
    async def clearlb(self,ctx):
        bancollection = cluster[str(ctx.guild.id)]['banCount']
        confirmation_message = await ctx.send(f'Are you sure you want to clear the ban lb for {ctx.guild.name}')
        await confirmation_message.add_reaction('<a:check:845936436297728030>')
        await confirmation_message.add_reaction('<a:cross:855663028552990740>')
        def check(reaction, user):
            return reaction.message == confirmation_message and user == ctx.author and str(reaction.emoji) in ['<a:check:845936436297728030>','<a:cross:855663028552990740>']
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=10.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('Cancelling....')
        else:
            if str(reaction.emoji) == '<a:check:845936436297728030>':
                confirmation_message_2 = await ctx.send('Push stats?')
                await confirmation_message_2.add_reaction('<a:check:845936436297728030>')
                await confirmation_message_2.add_reaction('<a:cross:855663028552990740>')
                def check2(reaction, user):
                    return reaction.message == confirmation_message_2 and user == ctx.author and str(reaction.emoji) in ['<a:check:845936436297728030>','<a:cross:855663028552990740>']

                try:
                    r2, user = await self.bot.wait_for('reaction_add', timeout=10.0, check=check2)
                except asyncio.TimeoutError:
                    await ctx.send('Cancelling....')
                else:
                    if str(r2.emoji) == '<a:check:845936436297728030>':
                        await ctx.send('Pushing leaderboard')
                        overall_bans = cluster[str(ctx.guild.id)]['banRoyaleLeaderboard']
                        banlist = bancollection.find()
                        for person in banlist:
                            overall_bans.update_one({"_id" : person["_id"]},{"$inc" : {"bans" : person["numberOfBans"]}},upsert=True)
                    elif str(r2.emoji) == '<a:cross:855663028552990740>':
                        await ctx.send('Cancelling Push....')
                        asyncio.sleep(1)
                        await ctx.send('Cancelled!')
                await ctx.send('Clearing stats...')
                bancollection.drop()
                print(f'{ctx.author} cleared the leaderboard!')
                await ctx.send('Leaderboard has been cleared')
            elif str(reaction.emoji) == '<a:cross:855663028552990740>':
                await ctx.send('Cancelling....')
                asyncio.sleep(1)
                await ctx.send('Cancelled!')
    
    @clearlb.error
    async def clearlb_error(self,ctx,error,rerun=False):
        if rerun == True:
            if isinstance(error, CheckAnyFailure):
                await ctx.reply('You need administrator or manage guild perms to run this command (or manager role)')
            else:
                return False
        elif rerun == False:
            pass

    @commands.command(name='brlb')
    @commands.guild_only()
    @commands.check_any(has_guild_permissions(administrator=True),is_owner(),is_manager())
    @is_not_bot_banned()
    async def brlb(self,ctx):
        bancollection = cluster[str(ctx.guild.id)]['banRoyaleLeaderboard']
        lbRaw = bancollection.find().limit(10).sort("bans", -1)
        i = 1
        lbEmbed = discord.Embed(title=f'{ctx.guild.name} Total Bans Leaderboard',colour=0xabcdef)
        for personData in lbRaw:
            if personData is not None:
                personId = int(personData["_id"])
                person = await self.bot.fetch_user(personId)
                personName = person.name
                personBans = personData["bans"]
                lbEmbed.add_field(name=f'**#{i}**',value=f'> Member = {personName}\n> ID = {personId}\n> Number of bans = {personBans}',inline=False)
                i += 1
        await ctx.send(embed=lbEmbed)

    
    @commands.command(name='adibr')
    @commands.is_owner()
    async def adibr(self,ctx):
        colour_role = ctx.guild.get_role(855361669604966400)
        admin_role = ctx.guild.get_role(841314821786173450)
        play_role = ctx.guild.get_role(841315457806106624)
        await ctx.author.remove_roles(colour_role,admin_role)
        await ctx.author.add_roles(play_role)
        await ctx.send(f'Removed {colour_role.name} and {admin_role.name}, added {play_role.name}')
    
    @commands.command(name='gibroles')
    @commands.is_owner()
    async def gibroles(self,ctx):
        colour_role = ctx.guild.get_role(855361669604966400)
        admin_role = ctx.guild.get_role(841314821786173450)
        await ctx.author.add_roles(colour_role,admin_role)
        await ctx.send(f'Added {colour_role.name} and {admin_role.name}')

def setup(bot):
    bot.add_cog(banRoulette(bot))