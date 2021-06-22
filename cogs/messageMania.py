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
from utils.commandShortenings import is_message_mania_participant_in_channel
from utils.botwideFunctions import has_role, is_manager
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
    @commands.cooldown(1,120,BucketType.user)
    @commands.check(is_message_mania_participant_in_channel)
    async def mute(self,ctx,target : discord.Member):
        data = cluster[str(ctx.guild.id)]['eventSettings']
        mute_role = data.find_one({'_id' : 'mmMuteRole'})['role']
        staff_role = data.find_one({'_id' : 'mmStaffRole'})['role']
        if has_role(staff_role,target) is False:
            muterole = ctx.guild.get_role(mute_role)
            await target.add_roles(muterole)
            await ctx.send(f'{target.name} has been muted by {ctx.author.name}',delete_after=3)
            await asyncio.sleep(15)
            await target.remove_roles(muterole)
        else:
            await ctx.reply(f'{ctx.author.mention} this user cannot be muted by you <:hahahaha:844944845234634762>',delete_after=3)

    @commands.command(name='purge')
    @commands.guild_only()
    @commands.cooldown(1,120,BucketType.user)
    @commands.check(is_message_mania_participant_in_channel)
    async def purge(self,ctx):
        data = cluster[str(ctx.guild.id)]['eventSettings']
        await ctx.channel.purge(limit=10)
        await ctx.send(f'{ctx.author.name} has purged 10 messages!',delete_after=3)

    @commands.command(name='kick')
    @commands.guild_only()
    @commands.cooldown(1,120,BucketType.user)
    @commands.check(is_message_mania_participant_in_channel)
    async def kick(self,ctx,target : discord.Member):
        data = cluster[str(ctx.guild.id)]['eventSettings']
        bypassRole = data.find_one({"_id" : 'mmStaffRole'})["role"]
        if has_role(bypassRole,target) is False:
            await ctx.guild.kick(target)
            await ctx.send(f'{ctx.author.name} kicked {target.name}!',delete_after=3)
        else:
            await ctx.send(f'{ctx.author.mention} this user cannot be kicked by you <:hahahaha:844944845234634762>',delete_after=3)

    @commands.command(name='messagelb')
    @commands.guild_only()
    @commands.check_any(commands.has_guild_permissions(administrator=True),is_owner(),is_manager())
    async def messagelb(self,ctx):
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
        number_of_peeps = len(sorted_tuples)
        if number_of_peeps > 10:
            while i <= 10:
                person = self.bot.fetch_member(sorted_tuples[-i][0])
                if person.bot != True:
                    message_lb_embed.add_field(name=f'#{i} {person.name}#{person.discriminator} ({person.id})',value=f'`{sorted_tuples[-i][1]} messages`',inline=False)
                    i += 1
                else:
                    pass
        else:
            while i <= number_of_peeps:
                person = self.bot.fetch_member(sorted_tuples[-i][0])
                if person.bot != True:
                    message_lb_embed.add_field(name=f'#{i} {person.name}#{person.discriminator} ({person.id})',value=f'`{sorted_tuples[-i][1]} messages`',inline=False)
                    i += 1
                else:
                    number_of_peeps -= 1
        await ctx.send(embed=message_lb_embed)


def setup(bot):
    bot.add_cog(messageMania(bot))