'''
WHAT IS THIS FILE?
This is the file with all commands needed for the ban roulette event with inkbot

WHAT ARE THE COMMANDS HERE?
1. ban_roulette_ban
2. banlb
3. clearlb
'''
import traceback
from discord.ext.commands.core import has_guild_permissions, is_owner
from discord.ext.commands.errors import CheckAnyFailure, CheckFailure, MemberNotFound, MissingRequiredArgument
from utils.botwideFunctions import has_role, is_manager
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
    async def brb(self, ctx, target : discord.Member):
        time1 = timer()
        settings_db = cluster[str(ctx.guild.id)]
        settings_col = settings_db['eventSettings']
        play_role = settings_col.find_one({'_id' : 'brParticipantRole'})['role']
        staff_role = settings_col.find_one({'_id' : 'brStaffRole'})['role']
        bancount = settings_db['banCount']
        time2 = timer()
        if has_role(staff_role,target) == False:
            if has_role(play_role,target) == True:
                for role in target.roles:
                    if role.id == play_role:
                        await target.remove_roles(role)
                        time3 = timer()
                await ctx.channel.send(f'{ctx.author.mention} banned {target.mention}!')
                time4 = timer()
                authorID = ctx.author.id
                status = bancount.find_one({'_id' : authorID})
                time5 = timer()
                if status is None:
                    person = {'_id' : authorID , "numberOfBans": 1}
                    bancount.insert_one(person)
                else:
                    myquery = {'_id' : authorID}
                    newBanNumber = status['numberOfBans'] + 1
                    bancount.update_one(myquery,{"$set":{"numberOfBans": newBanNumber}})
                time6 = timer()
                print(f'db fetch took {time2-time1}s, role remove {time3-time2}s, send message {time4-time3}, find author {time5-time4}, edit db {time6-time5}')
                role = ctx.guild.get_role(play_role)
                await target.add_roles(role)
            else:
                await ctx.reply(f'Don\'t try banning someone who can\'t participate <a:slowkek:838803911686750209>')
        else:
            await ctx.reply(f'You can\'t ban staff BAHAHAHAHA')

    @brb.error
    async def brb_error(self,ctx,error):
        if isinstance(error, CheckFailure):
            await ctx.reply('You don\'t have the roles required to run this command or are using it in the wrong channel')
        if isinstance(error,MemberNotFound):
            await ctx.reply('Pls provide a valid member to ban')
        if isinstance(error,MissingRequiredArgument):
            await ctx.reply('Make sure to use the correct format and provide all required args: ```ink brb <target>```')
        else:
            traceback.print_exc()
    
    @commands.command(name='banlb')
    @commands.check_any(has_guild_permissions(administrator=True),is_owner(),is_manager())
    @commands.guild_only()
    @commands.check(is_ban_royale_channel)
    async def banlb(self,ctx):
        bancollection = cluster[str(ctx.guild.id)]['banCount']
        lbRaw = bancollection.find().limit(10).sort("numberOfBans", -1)
        i = 1
        lbEmbed = discord.Embed(title='Dank Trades Ban Royale Leaderboard',colour=0xabcdef)
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
    async def banlb_error(self,ctx,error):
        if isinstance(error, CheckAnyFailure):
            await ctx.reply('You need administrator or manage guild perms to run this command (or manager role)')
        else:
            print(error)

    @commands.command(name='clearbanlb')
    @commands.check_any(has_guild_permissions(administrator=True),is_owner(),is_manager())
    @commands.guild_only()
    @commands.check(is_ban_royale_channel)
    async def clearlb(self,ctx):
        bancollection = cluster[str(ctx.guild.id)]['banCount']
        print(f'{ctx.author} cleared the leaderboard!')
        bancollection.drop()
        await ctx.send('Leaderboard has been cleared')
    
    @clearlb.error
    async def clearlb_error(self,ctx,error):
        if isinstance(error, CheckAnyFailure):
            await ctx.reply('You need administrator or manage guild perms to run this command (or manager role)')
        else:
            print(error)

            
def setup(bot):
    bot.add_cog(banRoulette(bot))