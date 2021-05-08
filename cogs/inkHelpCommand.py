#importing required stuff
import discord
from discord.ext import commands


#cog contents
class inkHelpCommand(commands.Cog):
    def __init__(self,bot):
        self.bot= bot

    #help command
    @commands.group(name="help",invoke_without_command=True)
    async def help_cmd(self,context):
        helpEmbed = discord.Embed(Title="inkBot help",description='Say `ink help <command>` for more info about a particular command',colour=0x9933ff)
        helpEmbed.add_field(name='Fun',value='`say`,`describe`,`hi`,`iq`,`besmooth`,`8ball`',inline=False)
        helpEmbed.add_field(name='Utils',value='`whois`,`info`,`help`,`ping`',inline=False)
        helpEmbed.add_field(name='Server Config',value='`autobanScammers`',inline=False)
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

    @help_cmd.command()
    async def whois(self,context):
        helpEmbed = discord.Embed(title='Whois command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Gives info on a user regardless of wether they are in the server(Use `ink info` for more detailed info on a user in the server)',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink whois <user>`',inline=False)
        await context.message.channel.send(embed=helpEmbed)

    @help_cmd.command()
    async def info(self,context):
        helpEmbed = discord.Embed(title='Info command',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Gives detailed info on a user in the server(Use `ink whois` for info on a user regardless of wether they are in the server )',inline=False)
        helpEmbed.add_field(name='Syntax',value='`ink info <user>`',inline=False)
        await context.message.channel.send(embed=helpEmbed)

    @help_cmd.command()
    async def autobanScammers(self,context):
        helpEmbed = discord.Embed(title='Autoban scammers',colour=0x9933ff)
        helpEmbed.add_field(name='Feature', value='Automatically bans members that are reported in the alert channels of various servers',inline=False)
        helpEmbed.add_field(name='Setup',value='You have to dm Adi for this till he learns to set up global vars',inline=False)
        await context.message.channel.send(embed=helpEmbed)

#cog setup
def setup(bot):
    bot.add_cog(inkHelpCommand(bot))