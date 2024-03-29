'''
1. WHAT IS THIS FILE?
This is the embeds that form the help command for inkbot

IMPORTS:
1. discord to define the embeds
2. commands cause this is a cog, and works based on it
3. is_not_bot_banned to prevent bot banned users from running commands
'''
from utils.botwideFunctions import is_not_bot_banned
import discord
from discord.ext import commands

'''
Variables:
1. emb_colour - the colour for all embeds
'''
emb_colour = 0x2B324D

'''
SAMPLE FORMAT TO COPY:
1.IF NO ALIAS:
    @help_cmd.command(name='')
    @is_not_bot_banned()
    @commands.guild_only()
    async def _help_cmd(self,ctx):
        help_embed = discord.Embed(title='** command**',description='',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink `',inline=False)
        await ctx.send(embed=help_embed)

2.IF HAS ALIAS:
    @help_cmd.command(name='',aliases=[''])
    @is_not_bot_banned()
    @commands.guild_only()
    async def _help_cmd(self,ctx):
        help_embed = discord.Embed(title='** command**',description='',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink `',inline=False)
        help_embed.add_field(name='**Aliases**:',value='``',inline=False)
        await ctx.send(embed=help_embed)
'''

#making the class which consists of all the stuff in the cog
class inkHelpCommand(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.group(name='help',aliases=['h'],invoke_without_command=True)
    @is_not_bot_banned()
    @commands.guild_only()
    async def help_cmd(self,ctx):
        help_embed = discord.Embed(title='inkBot help',description='Use `ink help <command>` to get more info on a command or group',colour=emb_colour)
        help_embed.set_thumbnail(url=self.bot.user.avatar_url)
        help_embed.add_field(name='**Fun Commands**:',value='`say` , `iq` , `describe` , `besmooth`',inline=False)
        help_embed.add_field(name='**Util Commands**:',value='`ping` , `whois` , `info` , `botinfo` , `rules` , `invite`',inline=False)
        help_embed.add_field(name='**Donation Management**:',value='`donation` , `settings`')
        help_embed.add_field(name='**Channel Management**:',value='`addchannel` , `removechannel` , `addchannelmanager` , `removechannelmanager`',inline=False)
        help_embed.add_field(name='**Event Commands**:',value='`ban_royale` , `message_mania` , `event_settings`')
        await ctx.send(embed=help_embed)

    @help_cmd.command(name='say')
    @is_not_bot_banned()
    @commands.guild_only()
    async def say_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Say command**',description='Repeats a provided message, in a specified channel\n(returns in the channel the command was called if no channel is provided)',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink say [channel] <message>`',inline=False)
        await ctx.send(embed=help_embed)
    
    @help_cmd.command(name='iq')
    @is_not_bot_banned()
    @commands.guild_only()
    async def iq_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**IQ command**',description='Gives the iq of a member (or of the author if no one is specified)',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink iq [target]`',inline=False)
        await ctx.send(embed=help_embed)

    @help_cmd.command(name='describe')
    @is_not_bot_banned()
    @commands.guild_only()
    async def describe_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Describe command**',description='Describes a mentioned user (or the author if no one is specified)',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink describe [target]`',inline=False)
        await ctx.send(embed=help_embed)

    @help_cmd.command(name='besmooth')
    @is_not_bot_banned()
    @commands.guild_only()
    async def besmooth_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Besmooth command**',description='Drops a pickup line',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink besmooth`',inline=False)
        await ctx.send(embed=help_embed)

    @help_cmd.command(name='ping',aliases=['pig'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def ping_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Ping command**',description='Gives the ping',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink ping`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`pig`',inline=False)
        await ctx.send(embed=help_embed)

    @help_cmd.command(name='whois',aliases=['wi'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def whois_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Whois command**',description='Gives info about any discord user',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink whois <user>`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`wi`',inline=False)
        await ctx.send(embed=help_embed)

    @help_cmd.command(name='info',aliases=['i'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def info_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Info command**',description='Givess info on any server member',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink info <member>`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`i`',inline=False)
        await ctx.send(embed=help_embed)
    
    @help_cmd.command(name='botinfo',aliases=['bi'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def botinfo_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Botinfo command**',description='Gives information about the bot',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink botinfo`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`bi`',inline=False)
        await ctx.send(embed=help_embed)

    @help_cmd.command(name='rules')
    @is_not_bot_banned()
    @commands.guild_only()
    async def rules_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Rules command**',description='Gives information on bot rules',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink rules`',inline=False)
        await ctx.send(embed=help_embed)

    @help_cmd.command(name='invite')
    @is_not_bot_banned()
    @commands.guild_only()
    async def invite_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Invite command**',description='Invite links to add ink to your server',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink invite`',inline=False)
        await ctx.send(embed=help_embed)
    
    @help_cmd.group(name='donation',aliases=['dono','d'],invoke_without_command=True)
    @is_not_bot_banned()
    @commands.guild_only()
    async def donation_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Donation Group**',description='Commands under the donation group\nP.S: aliases for donation are `dono` and `d`\nuse `ink help dono <subcommand>` for more info on a subcommand',colour=emb_colour)
        help_embed.add_field(name='**giveaway**:',value='Adds a certain amout to the total donation of a user (used for giveaway donations)',inline=False)
        help_embed.add_field(name='**event**:',value='Adds a certain amout to the total donation of a user (used for event donations)',inline=False)
        help_embed.add_field(name='**special**:',value='Adds a certain amout to the total donation of a user (used for special celebration donations)',inline=False)
        help_embed.add_field(name='**check**:',value='Shows the donations for a member',inline=False)
        help_embed.add_field(name='**mine**:',value='Shows your own donations',inline=False)
        help_embed.add_field(name='**checkeman**:',value='Checks the stats for donations taken for an event manager',inline=False)
        help_embed.add_field(name='**checkgman**:',value='Checks the stats for donations taken for a giveaway manager',inline=False)
        help_embed.add_field(name='**donolb**:',value='Shows the top 10 donors',inline=False)
        help_embed.add_field(name='**emanlb**:',value='Group with 2 ways of representing most active event managers',inline=False)
        help_embed.add_field(name='**gmanlb**:',value='Group with 2 ways of representing most active giveaway managers',inline=False)
        help_embed.add_field(name='**clearemanlb**:',value='Clears the eman leaderboard',inline=False)
        help_embed.add_field(name='**cleargmanlb**:',value='Clears the gman leaderboard',inline=False)
        await ctx.send(embed=help_embed)

    @donation_help_cmd.command(name='giveaway',aliases=['gaw'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def gaw_donation_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Giveaway dono command**',description='Adds a certain amout to the total donation of a user (used for giveaway donations)',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink donation giveaway <user> <amount>`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`gaw`',inline=False)
        help_embed.add_field(name='**Roles required**:',value='Giveaway manager, mod or admin')
        await ctx.send(embed=help_embed)

    @donation_help_cmd.command(name='event')
    @is_not_bot_banned()
    @commands.guild_only()
    async def event_donation_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Event dono command**',description='Adds a certain amout to the total donation of a user (used for event donations)',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink donation event <user> <amount>`',inline=False)
        help_embed.add_field(name='**Roles required**:',value='Event manager, mod or admin')
        await ctx.send(embed=help_embed)

    @donation_help_cmd.command(name='special')
    @is_not_bot_banned()
    @commands.guild_only()
    async def special_donation_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Special dono command**',description='Adds a certain amout to the total donation of a user (used for special celeb donations)',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink donation special <user> <amount>`',inline=False)
        help_embed.add_field(name='**Roles required**:',value='Event manager,Giveaway manager, mod or admin')
        await ctx.send(embed=help_embed)

    @donation_help_cmd.command(name='check')
    @is_not_bot_banned()
    @commands.guild_only()
    async def check_donation_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Check dono command**',description='Check the donations for a member',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink donations check <user>`',inline=False)
        help_embed.add_field(name='**Roles required**:',value='Event manager,Giveaway manager, mod or admin')
        await ctx.send(embed=help_embed)

    @donation_help_cmd.command(name='mine')
    @is_not_bot_banned()
    @commands.guild_only()
    async def mine_donation_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Mine command**',description='Check your own donations!',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink donations mine`',inline=False)
        await ctx.send(embed=help_embed)
    
    @donation_help_cmd.command(name='checkeman')
    @is_not_bot_banned()
    @commands.guild_only()
    async def checkeman_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Check eman command**',description='Check the eventss activity of an event manager',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink checkeman <member>`',inline=False)
        help_embed.add_field(name='**Role required**:',value='Admin')
        await ctx.send(embed=help_embed)
    
    @donation_help_cmd.command(name='checkgman')
    @is_not_bot_banned()
    @commands.guild_only()
    async def checkgman_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Check gman command**',description='Check the giveaways activity of a giveaway manager',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink checkgman <member>`',inline=False)
        help_embed.add_field(name='**Role required**:',value='Admin')
        await ctx.send(embed=help_embed)

    @donation_help_cmd.command(name='donolb')
    @is_not_bot_banned()
    @commands.guild_only()
    async def donolb_donation_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Donor leaderboard command**',description='Find the top donors for the guild!',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink donations donolb`',inline=False)
        help_embed.add_field(name='**Restriction**:',value='This command has a 30 second cd to avoid spam',inline=False)
        await ctx.send(embed=help_embed)

    @donation_help_cmd.group(name='emanlb',invoke_without_command=True)
    @is_not_bot_banned()
    @commands.guild_only()
    async def emanlb_donation_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Emanlb Group**',description='Commands under the emanlb group',colour=emb_colour)
        help_embed.add_field(name='**number**:',value='Gives a leaderboad ranking the event managers according to number of donations taken',inline=False)
        help_embed.add_field(name='**amount**:',value='Gives a leaderboard ranking the event managers according to amount in donations collected',inline=False)
        help_embed.add_field(name='**Roles required**:',value='Admin')
        await ctx.send(embed=help_embed)

    @emanlb_donation_help_cmd.command(name='number',aliases=['num'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def number_emanlb_donation_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Emanlb by number command**',description='Gives a leaderboad ranking the event managers according to number of donations taken',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink dono emanlb number`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`num`',inline=False)
        help_embed.add_field(name='**Roles required**:',value='Admin')
        await ctx.send(embed=help_embed)

    @emanlb_donation_help_cmd.command(name='amount',aliases=['amt'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def amount_emanlb_donation_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Emanlb by amount command**',description='Gives a leaderboard ranking the event managers according to amount in donations collected',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink dono emanlb amount`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`amt`',inline=False)
        help_embed.add_field(name='**Roles required**:',value='Admin')
        await ctx.send(embed=help_embed)
    
    @donation_help_cmd.group(name='gmanlb',invoke_without_command=True)
    @is_not_bot_banned()
    @commands.guild_only()
    async def gmanlb_donation_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Gmanlb Group**',description='Commands under the gmanlb group',colour=emb_colour)
        help_embed.add_field(name='**number**:',value='Gives a leaderboad ranking the giveaway managers according to number of donations taken',inline=False)
        help_embed.add_field(name='**amount**:',value='Gives a leaderboard ranking the giveaway managers according to amount in donations collected',inline=False)
        help_embed.add_field(name='**Roles required**:',value='Admin')
        await ctx.send(embed=help_embed)

    @gmanlb_donation_help_cmd.command(name='number',aliases=['num'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def number_gmanlb_donation_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Gmanlb by number command**',description='Gives a leaderboad ranking the giveaway managers according to number of donations taken',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink dono gmanlb number`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`num`',inline=False)
        help_embed.add_field(name='**Roles required**:',value='Admin')
        await ctx.send(embed=help_embed)

    @gmanlb_donation_help_cmd.command(name='amount',aliases=['amt'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def amount_gmanlb_donation_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Gmanlb by amount command**',description='Gives a leaderboard ranking the giveaway managers according to amount in donations collected',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink dono gmanlb amount`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`amt`',inline=False)
        help_embed.add_field(name='**Roles required**:',value='Admin')
        await ctx.send(embed=help_embed)

    @donation_help_cmd.command(name='clearemanlb',aliases=['cleareman'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def clearemanlb_donation_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Clear event manager leaderboard command**',description='Clears the eman leaderboard',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink donations clearemanlb`',inline=False)
        help_embed.add_field(name='**Roles required**:',value='Admin')
        await ctx.send(embed=help_embed)

    @donation_help_cmd.command(name='cleargmanlb',aliases=['cleargman'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def cleargmanlb_donation_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Clear giveaway manager leaderboard command**',description='Clears the egman leaderboard',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink donations cleargmanlb`',inline=False)
        help_embed.add_field(name='**Roles required**:',value='Admin')
        await ctx.send(embed=help_embed)
    
    @help_cmd.group(name='settings',aliases=['set'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def settings_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Settings Group Commands**', description='Alias for this command is `set`\nYou need admin or manage server perms to run commands in this category!',colour=emb_colour)
        help_embed.add_field(name='Giveaway manager',value='Sets a role as a giveaway manager role\nMembers with this role have perms to set giveaway donos, special donos and check a member\'s donos',inline=False)
        help_embed.add_field(name='Event manager',value='Sets a role as a event manager role\nMembers with this role have perms to set event donos, special donos and check a member\'s donos',inline=False)
        help_embed.add_field(name='Moderator',value='Sets a role as a mod role\nMembers with this role have perms to set event donos, giveaway donos, special donos and check a member\'s donos',inline=False)
        help_embed.add_field(name='Administrator',value='Sets a role as the administrator role\nMembers with this role have perms to run all commands under the donation group!',inline=False)
        help_embed.add_field(name='alertchannel',value='Sets a channel as the alert channel, that is used for the autoban feature',inline=False)
        help_embed.add_field(name='failchannel',value='Sets a channel as the fail channel, that is used for the autoban feature',inline=False)
        await ctx.send(embed=help_embed)
    
    @settings_help_cmd.command(name='giveawaymanager',aliases=['gman'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def giveawaymanager_settings_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Giveaway manager command**',description='Sets a role as a giveaway manager role\nMembers with this role have perms to set giveaway donos, special donos and check a member\'s donos',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink settings giveawaymanager <role>`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`gman`',inline=False)
        await ctx.send(embed=help_embed)
    
    @settings_help_cmd.command(name='eventmanager',aliases=['eman'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def eventmanager_settings_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Event Manager command**',description='Sets a role as a event manager role\nMembers with this role have perms to set event donos, special donos and check a member\'s donos',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink settings eventmanager <role>`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`eman`',inline=False)
        await ctx.send(embed=help_embed)

    @settings_help_cmd.command(name='moderator',aliases=['mod'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def moderator_settings_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Moderator command**',description='Sets a role as a mod role\nMembers with this role have perms to set event donos, giveaway donos, special donos and check a member\'s donos',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink settings moderator <role>`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`mod`',inline=False)
        await ctx.send(embed=help_embed)
    
    @settings_help_cmd.command(name='administrator',aliases=['admin'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def administrator_settings_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Administrator command**',description='Sets a role as the administrator role\nMembers with this role have perms to run all commands under the donation group!',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink settings administrator <role>`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`admin`',inline=False)
        await ctx.send(embed=help_embed)
    
    @settings_help_cmd.command(name='alertchannel',aliases=['alertchan'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def alertchannel_settings_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Alert Channel command**',description='Sets a channel as the alert channel, from which ink bans scammers reported from scam reports recieved from followed alert channels',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink settings alertchannel <role>`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`alertchan`',inline=False)
        await ctx.send(embed=help_embed)

    @settings_help_cmd.command(name='failchannel',aliases=['failchan'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def failchannel_settings_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Fail Channel command**',description='Sets a channel as the fail channel, where messages from which scammer id\'s are indetectable are left behind to be removed by someone else',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink settings failchannel <role>`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`failchan`',inline=False)
        await ctx.send(embed=help_embed)
    

    @help_cmd.command(name='addchannel',aliases=['ac','achan'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def addchannel_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Add channel command**',description='Adds a member to a channel',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink addchannel <member>`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`ac` , `achan`',inline=False)
        await ctx.send(embed=help_embed)
    
    @help_cmd.command(name='removechannel',aliases=['rc','rchan'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def removechannel_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Remove channel command**',description='Removes a member from a channel',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink removechannel <member>`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`rc` , `rchan`',inline=False)
        await ctx.send(embed=help_embed)

    @help_cmd.command(name='addchannelmanager',aliases=['acm'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def addchannelmanager_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Add channel manager command**',description='Sets a memeber as a channel manager by giving them manage channel perms in that channel',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink acm <channel> <member>`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`acm`',inline=False)
        await ctx.send(embed=help_embed)
    
    @help_cmd.command(name='removechannelmanager',aliases=['rcm'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def removechannelmanager_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Remove channel manager command**',description='Removes a member from channel manager',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink rcm <channel> <member>`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`rcm`',inline=False)
        await ctx.send(embed=help_embed)
    
    @help_cmd.group(name='event_settings',aliases=['eset','es'],invoke_without_command=True)
    @is_not_bot_banned()
    @commands.guild_only()
    async def event_settings_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Event settings commands**',description='All commands in this section require manage server permissions or the manager role (Manager role can be set with `ink eset manager_role`)\nOther vars are set using `ink eset <ban_royale/message_mania> <command>`\nAliases for `event_settings` are: `eset` and `es`',colour=emb_colour)
        help_embed.add_field(name='ban_royale',value='**Subcommands**: `channel` , `participant_role` , `staff_role` , `check`',inline=False)
        help_embed.add_field(name='message_mania', value='**Subcommands**: `channel` , `participant_role` , `staff_role` , `mute_role` , `check`', inline=False)
        help_embed.add_field(name='manager', value='Adds a role as manager role, giving members with the role access to change ban royale and message mania settings', inline=False)
        await ctx.send(embed=help_embed)
    
    @event_settings_help_cmd.group(name='ban_royale',aliases=['brcommands', 'br'],invoke_without_command=True)
    @is_not_bot_banned()
    @commands.guild_only()
    async def ban_royale_help_command(self,ctx):
        help_embed = discord.Embed(title='Ban Royale settings',description='Roles you need to set before being able to conduct a ban royale event',colour=emb_colour)
        help_embed.add_field(name='channel',value='Set a channel to play the ban royale event in',inline=False)
        help_embed.add_field(name='participant_role',value='Role required to run the ban command',inline=False)
        help_embed.add_field(name='staff_role',value='Members with this role cannot be affected by the ban command',inline=False)
        help_embed.add_field(name='check',value='Gives an embed to check if all reqired variables have been set',inline=False)
        await ctx.send(embed=help_embed)
    
    @ban_royale_help_command.command(name='channel',aliases=['chan'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def ban_royale_channel_help_cmd(self,ctx):
        help_embed = discord.Embed(title='channel',decription='Sets a channel that the ban royale event is to be held in!',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink eset br channel <channel>`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`chan`',inline=False)
        await ctx.send(embed=help_embed)
        
    @ban_royale_help_command.command(name='participant_role',aliases=['playrole'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def ban_royale_participant_role_help_cmd(self,ctx):
        help_embed = discord.Embed(title='participant_role',decription='Role required to run commands for the event',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink eset br participant_role <role>`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`playrole`',inline=False)
        await ctx.send(embed=help_embed)
    
    @ban_royale_help_command.command(name='staff_role',aliases=['staffrole'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def ban_royale_staff_role_help_cmd(self,ctx):
        help_embed = discord.Embed(title='staff_role',decription='Members with this role are immune to the ban command',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink eset br staff_role`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`staffrole`',inline=False)
        await ctx.send(embed=help_embed)
    
    @ban_royale_help_command.command(name='check')
    @is_not_bot_banned()
    @commands.guild_only()
    async def ban_royale_check_help_cmd(self,ctx):
        help_embed = discord.Embed(title='check',decription='Gives an embed to check if all reqired variables have been set',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink eset br check`',inline=False)
        await ctx.send(embed=help_embed)
    
    @event_settings_help_cmd.group(name='message_mania',aliases=['mmcommands', 'mm'],invoke_without_command=True)
    @is_not_bot_banned()
    @commands.guild_only()
    async def message_mania_help_command(self,ctx):
        help_embed = discord.Embed(title='Message Mania settings',description='Roles you need to set before being able to conduct a message mania event',colour=emb_colour)
        help_embed.add_field(name='channel',value='Set a channel to play the event in',inline=False)
        help_embed.add_field(name='participant_role',value='Role required to participate in the event',inline=False)
        help_embed.add_field(name='staff_role',value='Members with this role cannot be affected by message mania commands',inline=False)
        help_embed.add_field(name='mute_role',value='role given to muted members',inline=False)
        help_embed.add_field(name='check',value='Gives an embed to check if all reqired variables have been set',inline=False)
        await ctx.send(embed=help_embed)
    
    @message_mania_help_command.command(name='channel',aliases=['chan'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def message_mania_channel_help_cmd(self,ctx):
        help_embed = discord.Embed(title='channel',decription='Set a channel to play the event in',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink eset mm channel <channel>`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`channel`',inline=False)
        await ctx.send(embed=help_embed)
    
    @message_mania_help_command.command(name='participant_role',aliases=['playrole'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def message_mania_participant_role_help_cmd(self,ctx):
        help_embed = discord.Embed(title='participant_role',decription='Role required to participate in the event',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink eset mm participant_role <role>`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`playrole`',inline=False)
        await ctx.send(embed=help_embed)
    
    @message_mania_help_command.command(name='staff_role',aliases=['staffrole'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def message_mania_staff_role_help_cmd(self,ctx):
        help_embed = discord.Embed(title='staff_role',decription='Members with this role cannot be affected by message mania commands',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink eset mm staff_role <role>`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`staffrole`',inline=False)
        await ctx.send(embed=help_embed)
    
    @message_mania_help_command.command(name='mute_role',aliases=['muterole'])
    @is_not_bot_banned()
    @commands.guild_only()
    async def message_mania_mute_role_help_cmd(self,ctx):
        help_embed = discord.Embed(title='mute_role',decription='Role given to muted members',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink eset mm mute_role <role>`',inline=False)
        help_embed.add_field(name='**Aliases**:',value='`muterole`',inline=False)
        await ctx.send(embed=help_embed)
    
    @message_mania_help_command.command(name='check')
    @is_not_bot_banned()
    @commands.guild_only()
    async def ban_royale_check_help_cmd(self,ctx):
        help_embed = discord.Embed(title='check',decription='Gives an embed to check if all reqired variables have been set',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink eset mm check`',inline=False)
        await ctx.send(embed=help_embed)

    @event_settings_help_cmd.command(name='manager')
    @is_not_bot_banned()
    @commands.guild_only()
    async def event_settings_manager_cmd(self,ctx):
        help_embed = discord.Embed(title='Manager command',description='Adds a role as manager role, giving members with the role access to change ban royale and message mania settings',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink eset manager <role>`',inline=False)
        await ctx.send(embed=help_embed)

    @help_cmd.group(name='ban_royale',aliases=['banroyale'],invoke_without_command=True)
    @is_not_bot_banned()
    @commands.guild_only()
    async def ban_royale_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Ban royale commands**',description='Commands that you can use for ban royale, make sure to set all the vars required in `ink eset ban_royale` before starting a ban royale event\nRun `ink help <command>` for more info on a command in this category',colour=emb_colour)
        help_embed.add_field(name='**brb**:',value='Bans a member mentioned',inline=False)
        help_embed.add_field(name='**banlb**:',value='Shows the leaderboard for most bans',inline=False)
        help_embed.add_field(name='**clearbanlb**',value='Clear the ban leaderboard',inline=False)
        await ctx.send(embed=help_embed)
    
    @ban_royale_help_cmd.command(name='brb')
    @is_not_bot_banned()
    @commands.guild_only()
    async def ban_royale_brb_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**brb command**',description='Bans a member mentioned during the ban royale event',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink brb <target>`',inline=False)
        await ctx.send(embed=help_embed)
    
    @ban_royale_help_cmd.command(name='banlb')
    @is_not_bot_banned()
    @commands.guild_only()
    async def ban_royale_banlb_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**banlb command**',description='Shows the leaderboard for most bans after the ban royale event',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink banlb`',inline=False)
        help_embed.add_field(name='**Requirements**',value='Administrator perms or manager role')
        await ctx.send(embed=help_embed)
    
    @ban_royale_help_cmd.command(name='clearbanlb')
    @is_not_bot_banned()
    @commands.guild_only()
    async def ban_royale_clearbanlb_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**clearbanlb command**',description='Clear the ban leaderboard for ban royale event',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink clearbanlb`',inline=False)
        help_embed.add_field(name='**Requirements**',value='Administrator perms or manager role')
        await ctx.send(embed=help_embed)

    @help_cmd.group(name='message_mania',aliases=['mm'],invoke_without_command=True)
    @is_not_bot_banned()
    @commands.guild_only()
    async def message_mania_help_cmd(self,ctx):
        help_embed = discord.Embed(title='**Message mania commands**',description='Commands that you can use for message mania, make sure to set all the vars required in `ink eset message_mania` before starting a message mania event\nRun `ink help <command>` for more info on a command in this category',colour=emb_colour)
        help_embed.add_field(name='**mute**:',value='Mutes a member mentioned',inline=False)
        help_embed.add_field(name='**kick**:',value='Kicks a member mentioned',inline=False)
        help_embed.add_field(name='**purge**',value='purge 10 messages',inline=False)
        help_embed.add_field(name='**messagelb**:',value='Shows the leaderboard for most messages by a member in the channel',inline=False)
        await ctx.send(embed=help_embed)

    @message_mania_help_cmd.command(name='mute')
    @is_not_bot_banned()
    @commands.guild_only()
    async def message_mania_mute_command(self,ctx):
        help_embed = discord.Embed(title='**Mute command**',description='Mutes a member mentioned during message mania event',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink mute <target>`',inline=False)
        await ctx.send(embed=help_embed)
    
    @message_mania_help_cmd.command(name='kick')
    @is_not_bot_banned()
    @commands.guild_only()
    async def message_mania_kick_command(self,ctx):
        help_embed = discord.Embed(title='**Kick command**',description='Kicks a member mentioned during the message mania event',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink kick <target>`',inline=False)
        await ctx.send(embed=help_embed)
    
    @message_mania_help_cmd.command(name='purge')
    @is_not_bot_banned()
    @commands.guild_only()
    async def message_mania_purge_command(self,ctx):
        help_embed = discord.Embed(title='**purge command**',description='Deletes the last 10 messages sent in the channel during the message mania event',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink purge`',inline=False)
        await ctx.send(embed=help_embed)
    
    @message_mania_help_cmd.command(name='messagelb')
    @is_not_bot_banned()
    @commands.guild_only()
    async def message_mania_messagelb_command(self,ctx):
        help_embed = discord.Embed(title='**messagelb command**',description='Shows the leaderboard for most messages by a member in the channel',colour=emb_colour)
        help_embed.add_field(name='**Syntax**:',value='`ink messagelb`',inline=False)
        help_embed.add_field(name='**Requirements**',value='Administrator perms or manager role')
        await ctx.send(embed=help_embed)

#defining setup
def setup(bot):
    bot.add_cog(inkHelpCommand(bot))
    print("""Cog inkHelpCommand loaded successfully
--------------------""")