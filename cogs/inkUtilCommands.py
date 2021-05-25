'''
1. WHAT IS THIS FILE?
This is the cog for all my utility commands, that can be used to find information

2. WHAT ARE THE COMMANDS HERE?
(a) ping
(b) whois
(c) info
(d) botinfo
(e) rules
(f) invite

IMPORTS:
1. discord to define vars to be of discord.User like types
2. commands cause basically everything depends on it
3. error handlers
4. is_not_bot_banned to disable banned members from using commands
'''
from os import name
import discord
from discord import colour
from discord import invite
from discord.ext import commands
from discord.ext.commands.errors import MemberNotFound, MissingRequiredArgument, UserNotFound
from utils.botwideFunctions import is_not_bot_banned

'''
FILE WIDE VARIABLES
1. allowed_mentions - used to restrict bot mentions so it can only mention users, not roles or everyone 
2. embed colour - colour for embeds
'''
allowed_mentions = discord.AllowedMentions(everyone=False,roles=False)
embed_colour = 0x52476B


class inkUtilCommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    

    '''
    The 'ping' command:
    Gives the ping
    '''
    @commands.command(name='ping',aliases=['pig'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def ping(self,ctx):
        await ctx.send(f'Pong! <a:spongebobdance:845550564741349377>\nPing is {round(self.bot.latency*1000)}ms')


    '''
    The 'whois' command:
    Gives an embed with information on any discord user
    Running this command makes the bot recieve and give out information on a discord user in an organised embed form
    '''
    @commands.command(name='whois',aliases=['wi'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def whois(self,ctx,user : discord.User):
        whois_embed = discord.Embed(title=f'whois info for {user.name}#{user.discriminator}',colour=embed_colour)
        whois_embed.add_field(name='ID:',value=user.id,inline=False)
        whois_embed.add_field(name='Name and discriminator:',value=f'{user.name}#{user.discriminator}',inline=False)
        whois_embed.add_field(name='Account creation date:',value=str(user.created_at)[0:16],inline=False)
        whois_embed.add_field(name='Mention:',value=user.mention,inline=False)
        whois_embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=whois_embed)

    @whois.error
    async def whois_error(self,ctx,error):
        if isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink whois <user>\n\n{error.param} is a required argument that is missing!```')
        if isinstance(error,UserNotFound):
            await ctx.send(f'Couldn\'t find the user {error.argument} on discord! <a:nya_sadguitarmusic:845576181167554581> Make sure you provided the correct id',allowed_mentions=allowed_mentions)
        else:
            print(error)


    '''
    The 'info' command:
    Gives and embed giving info on a member of the guild the command was invoked in
    Running the command makes the bot return information about a member and represent it in an organised manner
    '''
    @commands.command(name='info',aliases=['i'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def info(self,ctx,member : discord.Member):
        role_list = [role.mention for role in member.roles if role != ctx.guild.default_role]
        roles = ', '.join(role_list)
        if len(role_list) == 0:
            grammer_correct_item = f'The member has no roles'
        elif len(role_list) == 1:
            grammer_correct_item = f'The member has {len(role_list)} role, which is:'
        else:
            grammer_correct_item = f'The member has {len(role_list)} roles, which are:'

        info_embed = discord.Embed(title=f'Info for {member.display_name}',colour=embed_colour)
        info_embed.add_field(name='ID:',value=member.id,inline=False)
        info_embed.add_field(name='Name and discriminator:',value=f'{member.name}#{member.discriminator}',inline=False)
        info_embed.add_field(name='Account created on:',value=str(member.created_at)[0:16],inline=False)
        info_embed.add_field(name='User mention:',value=member.mention,inline=False)
        info_embed.add_field(name='Roles:',value=f'{grammer_correct_item}\n{roles}')
        info_embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=info_embed)

    @info.error
    async def info_error(self,ctx,error):
        if isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink info <user>\n\n{error.param} is a required argument that is missing!```')
        if isinstance(error,MemberNotFound):
            await ctx.send(f'Couldn\'t find the user {error.argument} on in the guild! <a:nya_sadguitarmusic:845576181167554581> Make sure you provided the correct id',allowed_mentions=allowed_mentions)
        else:
            print(error)

    '''
    The 'botinfo' command:
    Gives an embed with info on the bot
    '''
    @commands.command(name='botinfo',aliases=['bi'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def botinfo(self,ctx):
        info_embed = discord.Embed(title='inkBot',description='Information about ink!',colour=embed_colour)
        info_embed.set_thumbnail(url=self.bot.user.avatar_url)
        info_embed.add_field(name='Bot name:',value=self.bot.user.name,inline=False)
        info_embed.add_field(name='Created on:',value=str(self.bot.user.created_at)[0:10],inline=False)
        info_embed.add_field(name='Bot made by:',value='Adi#1874',inline=False)
        info_embed.add_field(name='Status:',value='Public',inline=False)
        info_embed.add_field(name='Support Server:',value='[The inkPot](https://discord.gg/ujZ62Y9ANN)',inline=False)
        info_embed.add_field(name='Bot Invite:',value='[Admin Perms](https://discord.com/api/oauth2/authorize?client_id=839052539395440710&permissions=8&scope=bot)\n[Minimum perms for all functions](https://discord.com/api/oauth2/authorize?client_id=839052539395440710&permissions=268823636&scope=bot)\n[Giveaway utils only](https://discord.com/api/oauth2/authorize?client_id=839052539395440710&permissions=388160&scope=bot)',inline=False)
        await ctx.send(embed=info_embed)

    '''
    The 'rules' command:
    Tells you the bot rules
    '''
    @commands.command(name='rules')
    @is_not_bot_banned()
    @commands.guild_only()
    async def rules(self,ctx):
        rules_embed = discord.Embed(title='inkBot rules',description='Rules for the bot!\nFailure to follow these rules will result in blacklists or bans from the bot!',colour=embed_colour)
        rules_embed.add_field(name='Rule 1 - SPAMMING',value='Excessive spam of bot commands or aurtoresponces or other kinds of spam with malicious intent is not allowed',inline=False)
        rules_embed.add_field(name='Rule 2 - USAGE OF BUGS/EXPLOITS',value='Do **not** use any exploits or bugs you find, instead, report them in the [Support server](https://discord.gg/ujZ62Y9ANN)',inline=False)
        await ctx.send(embed=rules_embed)
    
    '''
    The 'invite' command:
    Givves you invite links for the bot
    '''
    @commands.command(name='invite')
    @is_not_bot_banned()
    @commands.guild_only()
    async def invite(self,ctx):
        invite_embed = discord.Embed(title='Invite links for inkBot',description='Use these links to invite ink or join our support server!',colour=embed_colour)
        invite_embed.add_field(name='Bot Invites:',value='[Admin Perms](https://discord.com/api/oauth2/authorize?client_id=839052539395440710&permissions=8&scope=bot)\n[Minimum perms for all functions](https://discord.com/api/oauth2/authorize?client_id=839052539395440710&permissions=268823636&scope=bot)\n[Giveaway utils only](https://discord.com/api/oauth2/authorize?client_id=839052539395440710&permissions=388160&scope=bot)',inline=False)
        invite_embed.add_field(name='Support Server:',value='[The inkPot](https://discord.gg/ujZ62Y9ANN)',inline=False)
        await ctx.send(embed=invite_embed)

        
def setup(bot):
    bot.add_cog(inkUtilCommands(bot))
    print("""Cog inkUtilCommands has loaded successfully
--------------------""")