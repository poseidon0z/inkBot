#importing required stuff
import discord
from discord import colour
from discord.ext import commands


#cog contents
class inkHelpCommand(commands.Cog):
    def __init__(self,bot):
        self.bot= bot

    #help command
    @commands.group(name="help2",invoke_without_command=True)
    @commands.guild_only()
    async def help_cmd(self,context):
        helpEmbed = discord.Embed(Title="inkBot help",description='Say `ink help <command>` for more info about a particular command',colour=0x9933ff)
        helpEmbed.set_thumbnail(url=self.bot.user.avatar_url)
        helpEmbed.add_field(name='Fun',value='`say`,`describe`,`hi`,`iq`,`besmooth`,`8ball`',inline=False)
        helpEmbed.add_field(name='Utils',value='`whois`,`info`,`help`,`ping`',inline=False)
        helpEmbed.add_field(name='Donations',value='`donation`',inline=False)
        helpEmbed.add_field(name='Server Config',value='`autobanScammers`,`channelmanagement`,`addchannel`,`removechannel`,`addchannelmanager`,`removechannelmanager`',inline=False)
        helpEmbed.set_footer(text='bot by Adi#1874')
        await context.message.channel.send(embed=helpEmbed)

    @help_cmd.command()
    async def say(self,context):
        helpEmbed = discord.Embed(title='Say command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Makes the bot repeat something for you, in the same channel',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink say <your_text>`',inline=False)
        await context.message.channel.send(embed=helpEmbed)

    @help_cmd.command()
    async def describe(self,context):
        helpEmbed = discord.Embed(title='Describe command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Makes the bot describe the person you ping',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink describe <target>`',inline=False)
        helpEmbed.add_field(name='Xtra Feature:', value='type `ink describe list` to see list of possible descriptions',inline=False)
        await context.message.channel.send(embed=helpEmbed)

    @help_cmd.command()
    async def hi(self,context):
        helpEmbed = discord.Embed(title='hi ink command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Makes the bot reply with a hi',inline=False)
        helpEmbed.add_field(name='Syntax',value='`hi ink`',inline=False)
        await context.message.channel.send(embed=helpEmbed)

    @help_cmd.command()
    async def help(self,context):
        helpEmbed = discord.Embed(title='Help command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Opens the `ink help` embed to see all ink features and find out how to use them',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink help`',inline=False)
        await context.message.channel.send(embed=helpEmbed)

    @help_cmd.command()
    async def iq(self,context):
        helpEmbed = discord.Embed(title='Iq command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Generates a random value to be the iq for the user mentioned',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink iq <target>`',inline=False)
        await context.message.channel.send(embed=helpEmbed)

    @help_cmd.command()
    async def besmooth(self,context):
        helpEmbed = discord.Embed(title='besmooth command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Generates a random pickup line',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink besmooth`',inline=False)
        await context.message.channel.send(embed=helpEmbed)

    @help_cmd.command()
    async def ping(self,context):
        helpEmbed = discord.Embed(title='Ping command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Gives a message telling you the ping you\'re getting at that time',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink ping`',inline=False)
        await context.message.channel.send(embed=helpEmbed)

    @help_cmd.command(name = '8ball')
    async def eightball(self,context):
        helpEmbed = discord.Embed(title='8ball command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Predict the future <a:winks:839524896270319707>',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink 8ball <what you want predicted>`',inline=False)
        await context.message.channel.send(embed=helpEmbed)

    @help_cmd.command(name = 'whois',aliases=['wi'])
    async def whois(self,context):
        helpEmbed = discord.Embed(title='Whois command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Gives info on a user regardless of wether they are in the server(Use `ink info` for more detailed info on a user in the server)',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink whois <user>`',inline=False)
        helpEmbed.add_field(name='Aliases',value='`wi``',inline=False)
        await context.message.channel.send(embed=helpEmbed)

    @help_cmd.command(name = 'info', aliases=['i'])
    async def info(self,context):
        helpEmbed = discord.Embed(title='Info command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Gives detailed info on a user in the server(Use `ink whois` for info on a user regardless of wether they are in the server )',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink info <user>`',inline=False)
        helpEmbed.add_field(name='Aliases',value='`i`',inline=False)
        await context.message.channel.send(embed=helpEmbed)

    @help_cmd.group(name='donation', aliases=['d','dono'], invoke_without_command=True)
    async def donations(self,ctx):
        donationEmbed = discord.Embed(title='Donations Category',description='Aliases for this command are `d` and `dono`',colour=0x9933ff)
        donationEmbed.add_field(name='**giveaway:**', value='adds a specifc amount to the person\'s donations(used if gaw donation)',inline=False)
        donationEmbed.add_field(name='**event**:', value='adds a specifc amount to the person\'s donations(used if event donation)',inline=False)
        donationEmbed.add_field(name='**special**:', value='adds a specific amount to the person\'s donations (used if the donation was for a special celeb)',inline=False)
        donationEmbed.add_field(name='**check**:', value='Checks how much a member has donated',inline=False)
        donationEmbed.add_field(name='**gmanlb**:', value='Shows a leaderboard of giveaway manager activity',inline=False)
        donationEmbed.add_field(name='**emanlb**:', value='Shows a leaderboard of event manager activity',inline=False)
        donationEmbed.add_field(name='**lb**:', value='tShows a leaderboard of top donators',inline=False)
        donationEmbed.add_field(name='**mine**:', value='Checks how much you have donated',inline=False)
        donationEmbed.add_field(name='**eventsheld**:', value='Shows number of events held by an event manager',inline=False)
        donationEmbed.add_field(name='**giveawaysheld**:', value='Shows number of gveaways held by a giveaway manager',inline=False)
        donationEmbed.set_footer(text='use "ink dono <subcommand_name>" for more info on a subcommand')
        await ctx.send(embed=donationEmbed)

    @donations.command(name='giveaway',aliases=['gaw'])
    async def gaw(self,ctx):
        helpEmbed = discord.Embed(title='Gaw command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Adds a specifc amount to the person\'s donations(used if gaw donation)',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink dono giveaway <member> <amount>`',inline=False)
        helpEmbed.add_field(name='Aliases',value='`gaw`',inline=False)
        await ctx.send(embed=helpEmbed)

    @donations.command(name='event')
    async def gaw(self,ctx):
        helpEmbed = discord.Embed(title='Event command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Adds a specifc amount to the person\'s donations(used if event donation)',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink dono event <member> <amount>`',inline=False)
        await ctx.send(embed=helpEmbed)

    @donations.command(name='special')
    async def gaw(self,ctx):
        helpEmbed = discord.Embed(title='Special command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Adds a specifc amount to the person\'s donations(used if special celeb donation)',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink dono special <member> <amount>`',inline=False)
        await ctx.send(embed=helpEmbed)

    @donations.command(name='check')
    async def gaw(self,ctx):
        helpEmbed = discord.Embed(title='Check command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Checks how much a member has donated',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink dono check <member>`',inline=False)
        await ctx.send(embed=helpEmbed)
    
    @donations.command(name='giveawaymanagerleaderboard',aliases=['gmanlb', 'glb'])
    async def gaw(self,ctx):
        helpEmbed = discord.Embed(title='Giveaway manager leaderboard',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Shows a leaderboard of giveaway manager activity',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink dono giveawaymanagerleaderboard <member> <amount>`',inline=False)
        helpEmbed.add_field(name='Aliases',value='`gmanlb`,`glb`',inline=False)
        await ctx.send(embed=helpEmbed)

    @donations.command(name='eventmanagerleaderboard',aliases=['emanlb','elb'])
    async def gaw(self,ctx):
        helpEmbed = discord.Embed(title='Event manager leaderboard',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Shows a leaderboard of event manager activity',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink eventmanagerleaderboard <member> <amount>`',inline=False)
        helpEmbed.add_field(name='Aliases',value='`emanlb`,`elb`',inline=False)
        await ctx.send(embed=helpEmbed)

    @donations.command(name='donationleaderboard',aliases=['donolb','dlb'])
    async def gaw(self,ctx):
        helpEmbed = discord.Embed(title='Donations leaderboard',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Shows a leaderboard of top donators',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink donationleaderboard <member> <amount>`',inline=False)
        helpEmbed.add_field(name='Aliases',value='`donolb`,`dlb`',inline=False)
        await ctx.send(embed=helpEmbed)
    
    @donations.command(name='mine')
    async def gaw(self,ctx):
        helpEmbed = discord.Embed(title='Mydono command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Checks how much you have donated',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink dono mine`',inline=False)
        await ctx.send(embed=helpEmbed)

    @donations.command(name='eventsheld',aliases=['eheld','eh'])
    async def gaw(self,ctx):
        helpEmbed = discord.Embed(title='Events held command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Shows number of events held by an event manager',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink eventsheld <member>`',inline=False)
        helpEmbed.add_field(name='Aliases',value='`eheld`,`eh`',inline=False)
        await ctx.send(embed=helpEmbed)
    
    @donations.command(name='giveawaysheld',aliases=['gheld','gh'])
    async def giveawaysheld(self,ctx):
        helpEmbed = discord.Embed(title='Giveaways held command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Shows number of gveaways held by a giveaway manager',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink giveawayssheld <member>`',inline=False)
        helpEmbed.add_field(name='Aliases',value='`gheld`,`gh`',inline=False)
        await ctx.send(embed=helpEmbed)


    @help_cmd.group(name='channelmanagement',aliases=['chanmanagement','cm'],invoke_without_command=True)
    async def channelManagement(self, ctx):
        helpEmbed = discord.Embed(title='Channel Management Commands',description='Commands in this category are disabled in Dank Trades',colour=0x9933ff)
        helpEmbed.add_field(name='Commands in this category: ', value='`addchannel`,`removechannel`,`addchannelmanager`,`removechannelmanager`',inline=False)
        helpEmbed.add_field(name='removechannel: ', value='Adds a member to a channel if you have manage channel perms in that channel',inline=False)
        helpEmbed.add_field(name='removechannel: ', value='Removes a member from a channel if you have manage channel perms in that channel',inline=False)
        helpEmbed.add_field(name='addchannelmanager',value='Gives a member manage channels perms for the given channel',inline=False)
        helpEmbed.add_field(name='removechannelmanager',value='Removes the manage channels perms for a member in the given channnel',inline=False)
        helpEmbed.set_footer(text='run "ink help <command_name>" for more info on a particular command')
        await ctx.send(embed=helpEmbed)

    @channelManagement.command(name='addchannel',aliases=['ac', 'addchan','achan'])
    async def addchannel(self,context):
        helpEmbed = discord.Embed(title='Addchannel command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Adds a member to the private channel',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink addchannel <target>`',inline=False)
        helpEmbed.add_field(name='Aliases',value='`ac`,`addchan`,`achan`',inline=False)
        helpEmbed.set_footer(text='Using this command requires you to have manage channels or higher permissions for that channel')
        await context.message.channel.send(embed=helpEmbed)
        
    @channelManagement.command(name='removechannel',aliases=['rc', 'removechan','rchan'])
    async def removechannel(self,ctx):
        helpEmbed = discord.Embed(title='Removechannel command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Removes a member from the private channel',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink removechannel <target>`',inline=False)
        helpEmbed.add_field(name='Aliases',value='`rc`,`removechan`,`rchan`',inline=False)
        helpEmbed.set_footer(text='Using this command requires you to have manage channels or higher permissions for that channel')
        await ctx.send(embed=helpEmbed)
    
    @channelManagement.command(name='addchannelmanager',aliases=['acm','addchanman'])
    async def addchannelmanager(self,context):
        helpEmbed = discord.Embed(title='Add channel manager command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Adds a member as the manager of a channel',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink addchannelmanager <channel> <target>`',inline=False)
        helpEmbed.add_field(name='Aliases',value='`acm`,`addchanman`',inline=False)
        helpEmbed.set_footer(text='Using this command requires you to have manage channels or higher permissions')
        await context.message.channel.send(embed=helpEmbed)
    
    @channelManagement.command(name='removechannelmanager',aliases=['rcm','remchanman'])
    async def removechannelmanager(self,context):
        helpEmbed = discord.Embed(title='Remove channel manager command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Removes a member from the position of manager of a channel',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink removechannelmanager <channel> <target>`',inline=False)
        helpEmbed.add_field(name='Aliases',value='`rcm`,`remchanman`',inline=False)
        helpEmbed.set_footer(text='Using this command requires you to have manage channels or higher permissions')
        await context.message.channel.send(embed=helpEmbed)

    @help_cmd.command(name='autobanscammers',aliases=['autoban'])
    async def autobanScammers(self,context):
        helpEmbed = discord.Embed(title='Autoban scammers',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Automatically bans members that are reported in the alert channels of various servers',inline=False)
        helpEmbed.add_field(name='Setup',value='DM  Adi#1874 to add this feature',inline=False)
        helpEmbed.add_field(name='Aliases',value='`autoban`',inline=False)
        await context.message.channel.send(embed=helpEmbed)

#cog setup
def setup(bot):
    bot.add_cog(inkHelpCommand(bot))