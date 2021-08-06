'''
WHAT IS THIS FILE?
This is the cog containing all message mania commands

WHAT ARE THE COMMANDS IN THIS FILE?
1. mute
2. kick
3. purge
4. messagelb
'''

import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from discord.ext.commands.core import is_owner
from json import load

from discord.ext.commands.errors import CheckAnyFailure, CheckFailure
from utils.commandShortenings import is_message_mania_channel, is_message_mania_participant_in_channel
from utils.botwideFunctions import has_role, is_manager, is_not_bot_banned
import asyncio
from pathlib import Path
import pymongo


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

class messageMania(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name='mute')
    @commands.guild_only()
    @is_not_bot_banned()
    @commands.cooldown(1,120,BucketType.user)
    @commands.check(is_message_mania_participant_in_channel)
    async def mute(self,ctx,target : discord.Member):
        data = cluster[str(ctx.guild.id)]['eventSettings']
        mute_role = data.find_one({'_id' : 'mmMuteRole'})['role']
        staff_role = data.find_one({'_id' : 'mmStaffRole'})['role']
        play_role = data.find_one({'_id' : 'mmParticipantRole'})['role']
        if has_role(staff_role,target) is False:
            if has_role(play_role,target) is True:
                muterole = ctx.guild.get_role(mute_role)
                await target.add_roles(muterole)
                await ctx.send(f'{target.name} has been muted by {ctx.author.name}')
                await asyncio.sleep(15)
                await target.remove_roles(muterole)
            else:
                await ctx.reply('Why are you trying to mute someone who can\'t participate <:smh:858209320188379197>')
        else:
            await ctx.reply(f'{ctx.author.mention} this user cannot be muted by you <:hahahaha:844944845234634762>')

    @mute.error
    async def mute_error(self,ctx,error,rerun=False):
        if rerun == True:
            if isinstance(error,CheckFailure):
                await ctx.reply('You need both participants role and have to be in the message mania channel to use this command <:smh:858209320188379197>')
            else:
                return False
        elif rerun == False:
            pass

    @commands.command(name='purge')
    @commands.guild_only()
    @is_not_bot_banned()
    @commands.cooldown(1,120,BucketType.user)
    @commands.check(is_message_mania_participant_in_channel)
    async def purge(self,ctx):
        data = cluster[str(ctx.guild.id)]['eventSettings']
        await ctx.channel.purge(limit=10)
        await ctx.send(f'{ctx.author.name} has purged 10 messages!')

    @purge.error
    async def purge_error(self,ctx,error,rerun=False):
        if rerun == True:
            if isinstance(error,CheckFailure):
                await ctx.reply('You need both participants role and have to be in the message mania channel to use this command <:smh:858209320188379197>')
            else:
                return False
        elif rerun == False:
            pass

    @commands.command(name='kick')
    @commands.guild_only()
    @is_not_bot_banned()
    @commands.cooldown(1,120,BucketType.user)
    @commands.check(is_message_mania_participant_in_channel)
    async def kick(self,ctx,target : discord.Member):
        data = cluster[str(ctx.guild.id)]['eventSettings']
        bypassRole = data.find_one({"_id" : 'mmStaffRole'})["role"]
        play_role = data.find_one({'_id' : 'mmParticipantRole'})['role']
        if has_role(bypassRole,target) is False:
            if has_role(play_role,target) is True:
                await ctx.guild.kick(target)
                await ctx.send(f'{ctx.author.name} kicked {target.name}!')
            else:
                await ctx.reply('Why are you trying to kick someone who can\'t participate <:smh:858209320188379197>')
        else:
            await ctx.send(f'{ctx.author.mention} this user cannot be kicked by you <:hahahaha:844944845234634762>')

    @kick.error
    async def kick_error(self,ctx,error,rerun=False):
        if rerun == True:
            if isinstance(error,CheckFailure):
                await ctx.reply('You need both participants role and have to be in the message mania channel to use this command <:smh:858209320188379197>')
            else:
                return False
        elif rerun == False:
            pass

    @commands.command(name='messagelb')
    @commands.guild_only()
    @is_not_bot_banned()
    @commands.check_any(commands.has_guild_permissions(administrator=True),is_owner(),is_manager())
    @commands.check(is_message_mania_channel)
    @commands.cooldown(1,600,BucketType.guild)
    async def messagelb(self,ctx):
        staff_role = cluster[str(ctx.guild.id)]['eventSettings'].find_one({'_id' : 'mmStaffRole'})['role']
        async with ctx.channel.typing():
            messages = await ctx.channel.history(limit=None).flatten()
            messagedata = {}
            message_lb_embed = discord.Embed(title=f'{ctx.guild.name} Leaderboard!',colour=0xabcdef)
            for message in messages:
                if message.author.bot == False:
                    author = message.author.id
                    if author not in messagedata:
                        messagedata[author] = 1
                    else:
                        number_of_messages = messagedata[author] + 1
                        messagedata[author] = number_of_messages
            sorted_tuples = sorted(messagedata.items(), key=lambda item: item[1])
            await ctx.send(f'Gathered data for messages from {len(sorted_tuples)} members')
            i = 1
            api_call_count = 0
            number_of_peeps = len(sorted_tuples)
            while i <= 10 and i <= number_of_peeps:
                try:
                    person = ctx.guild.get_member(sorted_tuples[-i][0])
                    message_lb_embed.add_field(name=f'#{i} {person.name}#{person.discriminator} ({person.id})',value=f'`{sorted_tuples[-i][1]} messages`',inline=False)
                except:
                    api_call_count +1
                    person = await self.bot.fetch_user(sorted_tuples[-i][0])
                    message_lb_embed.add_field(name=f'#{i} {person.name}#{person.discriminator} ({person.id})',value=f'`{sorted_tuples[-i][1]} messages`',inline=False)
                i += 1
            print(f'{api_call_count} API calls were made by {ctx.author.name} ({ctx.author.id})')
        await ctx.send(embed=message_lb_embed)
        confirmation_message = await ctx.send('Publish?')
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
                db_location = cluster[str(ctx.guild.id)]['messageManiaLeaderBoard']
                for data in sorted_tuples:
                    query = {"_id" : data[0]}
                    db_location.update_one(query,{"$inc" : {"messages" : data[1]}},upsert=True)
                await ctx.send('Published!')
            else:
                await ctx.send('Cancelling....')
                await asyncio.sleep(1)
                await ctx.send('Cancelled!')
    
    @mute.error
    async def mute_error(self,ctx,error,rerun=False):
        if rerun == True:
            if isinstance(error,CheckFailure):
                await ctx.reply('You need to be in the message mania channel to use this command <:smh:858209320188379197>')
            elif isinstance(error,CheckAnyFailure):
                await ctx.reply('You need either admin perms or the manager role to use this command')
            else:
                return False
        elif rerun == False:
            pass

    @commands.command(name='mostmessages',aliases=['mmlb'])
    @commands.guild_only()
    @is_not_bot_banned()
    @commands.check_any(commands.has_guild_permissions(administrator=True),is_owner(),is_manager())
    async def global_message_lb(self,ctx):
        totallb_embed = discord.Embed(title=f'Most messages in {ctx.guild.name}',colour=0xabcdef)
        data = cluster[str(ctx.guild.id)]['messageManiaLeaderBoard']
        raw_lb = data.find().sort('messages',-1).limit(10)
        i = 1
        for member_data in raw_lb:
            if member_data is not None:
                if i <= 10:
                    member_id = int(member_data["_id"])
                    person = await self.bot.fetch_user(member_id)
                    number_of_messages = '{:,.0f}'.format(member_data['messages'])
                    totallb_embed.add_field(name=f'#{i} {person.name}#{person.discriminator} ({person.id})',value=f'`{number_of_messages} messages`',inline=False)
        await ctx.send(embed=totallb_embed)




def setup(bot):
    bot.add_cog(messageMania(bot))
    print("""Cog messageMania has loaded successfully
--------------------""")