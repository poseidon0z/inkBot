'''
1. WHAT IS THIS FILE?
This is a cog containing all of the event commands for inkbot

2. WHAT ARE THE COMMANDS HERE?
(a)eventsettings
    (1)ban_royale
        > channel
        > banned_role
        > participant_role
        > staff_role
    
    (2)message_mania
        > channel
        > participant_role
        > staff_role
        > mute_role
    
    (3)manager
'''

from utils.commandShortenings import does_exist
import discord
from discord.ext import commands
from discord.ext.commands.core import has_guild_permissions, is_owner
from json import load
from discord.ext.commands.errors import ChannelNotFound, CheckAnyFailure, MissingRequiredArgument, RoleNotFound
import pymongo
from pathlib import Path
from utils.botwideFunctions import is_manager, is_not_bot_banned

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


class eventSettings(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.group(name='event_settings',aliases=['es','eset'],invoke_without_command=True)
    @is_not_bot_banned()
    @commands.guild_only()
    async def event_settings(self,ctx):
        eset_embed = discord.Embed(title='Event Settings',description='All commands in this section require manage server permissions or the manager role (Manager role can be set with `ink eset manager_role`)\nOther vars are set using `ink eset <ban_royale/message_mania> <command>`',colour=embed_colour)
        eset_embed.add_field(name='Ban Royale Settings',value='`channel` , `banned_role` , `participant_role` , `staff_role` , `check`',inline=False)
        eset_embed.add_field(name='Message Mania Settings', value='`channel` , `participant_role` , `staff_role` , `mute_role` , `check`', inline=False)
        eset_embed.add_field(name='manager', value='Adds a role as manager role, giving them access to change settings under ban royale commands or message mania commands', inline=False)
        await ctx.send(embed=eset_embed)

    @event_settings.group(name='ban_royale',aliases=['brcommands', 'br'],invoke_without_command=True)
    @commands.check_any(has_guild_permissions(administrator=True),has_guild_permissions(manage_guild=True),is_owner(),is_manager())
    @is_not_bot_banned()
    @commands.guild_only()
    async def ban_royale_settings(self,ctx):
        brset_embed = discord.Embed(title='Ban Royale settings',description='Roles you need to set before being able to conduct a ban royale event',colour=embed_colour)
        brset_embed.add_field(name='channel',value='Set a channel to play the ban royale event in',inline=False)
        brset_embed.add_field(name='banned_role',value='Set a role that is given to members who are banned',inline=False)
        brset_embed.add_field(name='participant_role',value='Role required to run the ban command',inline=False)
        brset_embed.add_field(name='staff_role',value='Members with this role cannot be affected by the ban command',inline=False)
        brset_embed.add_field(name='check',value='Checks if all the required variables have been set',inline=False)
        # brset_embed.add_field(name='trueban',value='If enabled, the ban command actually bans the member from the server on running it, if disabled then members are given a "banned" role instead (Trueban is set to disabled by default)',inline=False)
        await ctx.send(embed=brset_embed)

    @ban_royale_settings.command(name='channel',aliases=['chan'])
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.check_any(has_guild_permissions(administrator=True),has_guild_permissions(manage_guild=True),is_owner(),is_manager())
    async def br_channel(self,ctx,channel : discord.TextChannel):
        server_settings = cluster[str(ctx.guild.id)]['eventSettings']
        query = {"_id" : 'brChannel'}
        server_settings.update_one(query,{"$set": {'channel' : channel.id}},upsert=True)
        await ctx.send(f'Channel for ban royale has been set as {channel.mention}')
    
    @br_channel.error
    async def brchannel_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        elif isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink eset br channel <channel>\n\nchannel is not specified```')
        elif isinstance(error,ChannelNotFound):
            await ctx.send(f'Couldn\'t find the channel "{error.argument}" <:lotsofpain:839371861346222112>')
        else:
            print(error)

    @ban_royale_settings.command(name='banned_role',aliases=['banrole'])
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.check_any(has_guild_permissions(administrator=True),has_guild_permissions(manage_guild=True),is_owner(),is_manager())
    async def br_banned_role(self,ctx,role : discord.Role):
        server_settings = cluster[str(ctx.guild.id)]['eventSettings']
        query = {'_id' : 'brBannedRole'}
        server_settings.update_one(query,{"$set" : {"role" : role.id}},upsert=True)
        await ctx.send(f'Banned role has been set as {role.mention}')

    @br_banned_role.error
    async def br_banned_role_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        elif isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink eset br banrole <role>\n\nrole is not specified```')
        elif isinstance(error,RoleNotFound):
            await ctx.send(f'Couldn\'t find the role "{error.argument}" <:lotsofpain:839371861346222112>')
        else:
            print(error)
        
    @ban_royale_settings.command(name='participant_role',aliases=['playrole'])
    @commands.check_any(has_guild_permissions(administrator=True),has_guild_permissions(manage_guild=True),is_owner(),is_manager())
    @is_not_bot_banned()
    @commands.guild_only()
    async def br_participant_role(self,ctx,role : discord.Role):
        server_settings = cluster[str(ctx.guild.id)]['eventSettings']
        query = {'_id' : 'brParticipantRole'}
        server_settings.update_one(query,{"$set" : {"role" : role.id}},upsert=True)
        await ctx.send(f'Participant role has been set as {role.mention}')

    @br_participant_role.error
    async def br_participant_role_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        elif isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink eset br participant_role <role>\n\nrole is not specified```')
        elif isinstance(error,RoleNotFound):
            await ctx.send(f'Couldn\'t find the role "{error.argument}" <:lotsofpain:839371861346222112>')
        else:
            print(error)
        
    @ban_royale_settings.command(name='staff_role',aliases=['staffrole'])
    @is_not_bot_banned()
    @commands.guild_only()
    @commands.check_any(has_guild_permissions(administrator=True),has_guild_permissions(manage_guild=True),is_owner(),is_manager())
    async def br_staff_role(self,ctx,role : discord.Role):
        server_settings = cluster[str(ctx.guild.id)]['eventSettings']
        query = {'_id' : 'brStaffRole'}
        server_settings.update_one(query,{"$set" : {"role" : role.id}},upsert=True)
        await ctx.send(f'Staff role has been set as {role.mention}')

    @br_staff_role.error
    async def br_staff_role_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        elif isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink eset br staff_role <role>\n\nrole is not specified```')
        elif isinstance(error,RoleNotFound):
            await ctx.send(f'Couldn\'t find the role "{error.argument}" <:lotsofpain:839371861346222112>')
        else:
            print(error)

    @ban_royale_settings.command(name='check')
    @commands.guild_only()
    @commands.check_any(has_guild_permissions(administrator=True),has_guild_permissions(manage_guild=True),is_owner(),is_manager())
    @is_not_bot_banned()
    async def br_check(self,ctx):
        server_settings = cluster[str(ctx.guild.id)]['eventSettings']
        stuff_to_check = ['Channel','BannedRole','ParticipantRole','StaffRole']
        br_set_embed = discord.Embed(title='Ban Royale Settings',colour=embed_colour)
        for thing in stuff_to_check:
            query = {'_id' : 'br' + thing}
            check_result = does_exist(query,server_settings)
            if check_result == True:
                emote = '<a:check:845936436297728030>'
            else:
                emote = '<:cancel:845945583835283487>'
            br_set_embed.add_field(name='\u200b',value=f'{emote} {thing}',inline=False)
        await ctx.send(embed=br_set_embed)
            

    @event_settings.group(name='message_mania',aliases=['mmcommands', 'mm'],invoke_without_command=True)
    @commands.check_any(has_guild_permissions(administrator=True),has_guild_permissions(manage_guild=True),is_owner(),is_manager())
    @is_not_bot_banned()
    @commands.guild_only()
    async def message_mania_settings(self,ctx):
        mmset_embed = discord.Embed(title='Message Mania settings',description='Roles you need to set before being able to conduct a message mania event',colour=embed_colour)
        mmset_embed.add_field(name='channel',value='Set a channel to play the event in',inline=False)
        mmset_embed.add_field(name='participant_role',value='Role required to participate in the event',inline=False)
        mmset_embed.add_field(name='staff_role',value='Members with this role cannot be affected by message mania commands',inline=False)
        mmset_embed.add_field(name='mute_role',value='role given to muted members',inline=False)
        mmset_embed.add_field(name='check',value='Checks if all the required variables have been set',inline=False)
        await ctx.send(embed=mmset_embed)


    @message_mania_settings.command(name='channel',aliases=['chan'])
    @commands.check_any(has_guild_permissions(administrator=True),has_guild_permissions(manage_guild=True),is_owner(),is_manager())
    @is_not_bot_banned()
    @commands.guild_only()
    async def mm_channel(self,ctx,channel : discord.TextChannel):
        server_settings = cluster[str(ctx.guild.id)]['eventSettings']
        query = {'_id' : 'mmChannel'}
        server_settings.update_one(query,{'$set' : {'channel' : channel.id}},upsert=True)
        await ctx.send(f'Message mania channel has been set as {channel.mention}')
    
    @mm_channel.error
    async def mm_channel_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        elif isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink eset mm channel <channel>\n\nchannel is not specified```')
        elif isinstance(error,ChannelNotFound):
            await ctx.send(f'Couldn\'t find the channel "{error.argument}" <:lotsofpain:839371861346222112>')
        else:
            print(error)
        
    @message_mania_settings.command(name='participant_role',aliases=['playrole'])
    @commands.check_any(has_guild_permissions(administrator=True),has_guild_permissions(manage_guild=True),is_owner(),is_manager())
    @is_not_bot_banned()
    @commands.guild_only()
    async def mm_participant_role(self,ctx,role : discord.Role):
        server_settings = cluster[str(ctx.guild.id)]['eventSettings']
        query = {'_id' : 'mmParticipantRole'}
        server_settings.update_one(query,{'$set' : {'role' : role.id}},upsert=True)
        await ctx.send(f'Participant role has been set as {role.mention}')
    
    @mm_participant_role.error
    async def mm_participant_role_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        elif isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink eset mm playrole <role>\n\nrole is not specified```')
        elif isinstance(error,RoleNotFound):
            await ctx.send(f'Couldn\'t find the role "{error.argument}" <:lotsofpain:839371861346222112>')
        else:
            print(error)
        
    @message_mania_settings.command(name='staff_role',aliases=['staffrole'])
    @commands.check_any(has_guild_permissions(administrator=True),has_guild_permissions(manage_guild=True),is_owner(),is_manager())
    @is_not_bot_banned()
    @commands.guild_only()
    async def mm_staff_role(self,ctx,role : discord.Role):
        server_settings = cluster[str(ctx.guild.id)]['eventSettings']
        query = {'_id' : 'mmStaffRole'}
        server_settings.update_one(query,{'$set' : {'role' : role.id}},upsert=True)
        await ctx.send(f'Staff role has been set as {role.mention}')
    
    @mm_staff_role.error
    async def mm_staff_role_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        elif isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink eset mm staffrole <role>\n\nRole is not specified```')
        else:
            print(error)

    @message_mania_settings.command(name='mute_role',aliases=['muterole'])
    @commands.check_any(has_guild_permissions(administrator=True),has_guild_permissions(manage_guild=True),is_owner(),is_manager())
    @is_not_bot_banned()
    @commands.guild_only()
    async def mm_mute_role(self,ctx,role : discord.Role):
        server_settings = cluster[str(ctx.guild.id)]['eventSettings']
        query = {'_id' : 'mmMuteRole'}
        server_settings.update_one(query,{'$set' : {'role' : role.id}},upsert=True)
        await ctx.send(f'Mute role has been set as {role.mention}')
    
    @mm_mute_role.error
    async def mm_mute_role_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        elif isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink eset mm muterole <role>\n\nRole is not specified```')
        else:
            print(error)

    @message_mania_settings.command(name='check')
    @commands.guild_only()
    @commands.check_any(has_guild_permissions(administrator=True),has_guild_permissions(manage_guild=True),is_owner(),is_manager())
    @is_not_bot_banned()
    async def mm_check(self,ctx):
        server_settings = cluster[str(ctx.guild.id)]['eventSettings']
        stuff_to_check = ['Channel', 'ParticipantRole' , 'StaffRole', 'MuteRole']
        mm_set_embed = discord.Embed(title='Message Mania Settings',colour=embed_colour)
        for thing in stuff_to_check:
            query = {'_id' : 'mm' + thing}
            check_result = does_exist(query,server_settings)
            if check_result == True:
                emote = '<a:check:845936436297728030>'
            else:
                emote = '<:cancel:845945583835283487>'
            mm_set_embed.add_field(name='\u200b',value=f'{emote} {thing}',inline=False)
        await ctx.send(embed=mm_set_embed)


    @event_settings.command(name='manager')
    @commands.check_any(has_guild_permissions(administrator=True),has_guild_permissions(manage_guild=True),is_owner())
    @is_not_bot_banned()
    @commands.guild_only()
    async def eset_manager(self,ctx,role : discord.Role):
        server_settings = cluster[str(ctx.guild.id)]['eventSettings']
        query = {'_id' : 'managerRole'}
        server_settings.update_one(query,{'$set' : {'role' : role.id}},upsert=True)
        await ctx.send(f'Manager role has been set as {role.mention}')
    
    @eset_manager.error
    async def eset_manager_error(self,ctx,error):
        if isinstance(error,CheckAnyFailure):
            await ctx.send('You dont have perms to run this command! <a:HAHA:840658400723206235>')
        elif isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink eset manager <role>\n\nRole is not specified```')
        else:
            print(error)


def setup(bot):
    bot.add_cog(eventSettings(bot))