#importing required stuff
import discord
from discord.ext import commands


#cog contents
class inkHelpCommand(commands.Cog):
    def __init__(self,bot):
        self.bot= bot

    #help command
    @commands.group(name="help",invoke_without_command=True)
    @commands.guild_only()
    async def help_cmd(self,context):
        helpEmbed = discord.Embed(Title="inkBot help",description='Say `ink help <command>` for more info about a particular command',colour=0x9933ff)
        helpEmbed.add_field(name='Fun',value='`say`,`describe`,`hi`,`iq`,`besmooth`,`8ball`',inline=False)
        helpEmbed.add_field(name='Utils',value='`whois`,`info`,`help`,`ping`',inline=False)
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

    @help_cmd.command(name='ChannelManagement',aliases=['chanmanagement','channelmanagement'])
    async def info(self, ctx):
        helpEmbed = discord.Embed(title='Channel Management Commands',colour=0x9933ff)
        helpEmbed.add_field(name='Commands in this category: ', value='`addchannel`,`removechannel`,`addchannelmanager`,`removechannelmanager`',inline=False)
        helpEmbed.add_field(name='removechannel: ', value='Adds a member to a channel if you have manage channel perms in that channel',inline=False)
        helpEmbed.add_field(name='removechannel: ', value='Removes a member from a channel if you have manage channel perms in that channel',inline=False)
        helpEmbed.add_field(name='addchannelmanager',value='Gives a member manage channels perms for the given channel',inline=False)
        helpEmbed.add_field(name='removechannelmanager',value='Removes the manage channels perms for a member in the given channnel',inline=False)
        helpEmbed.set_footer(text='run "ink help <command_name>" for more info on a particular command')
        await ctx.send(embed=helpEmbed)

    @help_cmd.command(name='addchannel',aliases=['ac', 'addchan','achan'])
    async def addchannel(self,context):
        helpEmbed = discord.Embed(title='Addchannel command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Adds a member to the private channel',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink addchannel <target>`',inline=False)
        helpEmbed.add_field(name='Aliases',value='`ac`,`addchan`,`achan`',inline=False)
        helpEmbed.set_footer(text='Using this command requires you to have manage channels or higher permissions for that channel')
        await context.message.channel.send(embed=helpEmbed)
        
    @help_cmd.command(name='removechannel',aliases=['rc', 'removechan','rchan'])
    async def removechannel(self,ctx):
        helpEmbed = discord.Embed(title='Removechannel command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Removes a member from the private channel',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink removechannel <target>`',inline=False)
        helpEmbed.add_field(name='Aliases',value='`rc`,`removechan`,`rchan`',inline=False)
        helpEmbed.set_footer(text='Using this command requires you to have manage channels or higher permissions for that channel')
        await ctx.send(embed=helpEmbed)
    
    @help_cmd.command(name='addchannelmanager',aliases=['acm','addchanman'])
    async def addchannelmanager(self,context):
        helpEmbed = discord.Embed(title='Add channel manager command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Adds a member as the manager of a channel',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink addchannelmanager <channel> <target>`',inline=False)
        helpEmbed.add_field(name='Aliases',value='`acm`,`addchanman`',inline=False)
        helpEmbed.set_footer(text='Using this command requires you to have manage channels or higher permissions')
        await context.message.channel.send(embed=helpEmbed)
    
    @help_cmd.command(name='removechannelmanager',aliases=['rcm','remchanman'])
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
        helpEmbed.add_field(name='Setup',value='You have to dm Adi for this till he learns to set up global vars',inline=False)
        helpEmbed.add_field(name='Aliases',value='`autoban`',inline=False)
        await context.message.channel.send(embed=helpEmbed)

#cog setup
def setup(bot):
    bot.add_cog(inkHelpCommand(bot))