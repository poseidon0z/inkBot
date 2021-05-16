import discord
from discord.ext import commands
from utils import simplifications

class inkUtilCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #whois feature
    @commands.command(name = 'whois',aliases=['wi'])
    @commands.check(simplifications.isNotbanned)
    @commands.guild_only()    
    async def whois(self,context,target : discord.User):
        whoIsEmbed = discord.Embed(title=f"""UserInfo for {target.display_name}""",color=0xabcdef)
        whoIsEmbed.add_field(name = "User Id:", value = target.id,inline=False)
        whoIsEmbed.add_field(name = "User Name:", value =f"""{target.name}#{target.discriminator}""",inline=False)
        whoIsEmbed.add_field(name = "User account creation date:", value = str(target.created_at)[0:16],inline=False)
        whoIsEmbed.set_thumbnail(url = target.avatar_url)
        await context.channel.send(embed = whoIsEmbed)


    #info feature
    @commands.command(name = 'info', aliases=['i'])
    @commands.check(simplifications.isNotbanned)
    @commands.guild_only()    
    async def info(self, context,target : discord.Member):
        roleList = [role.mention for role in target.roles if role != context.guild.default_role ]
        roles = ' '.join(roleList)
        infoEmbed = discord.Embed(title =f"""Info for {target.display_name}""", color=0xabcdef)
        infoEmbed.add_field(name = 'User Id:', value = target.id, inline=False)
        infoEmbed.add_field(name = 'User Name: ', value = f"""{target.name}#{target.discriminator}""",inline=False)
        infoEmbed.add_field(name = 'User Nick(None if no nick):', value = target.nick,inline=False)
        infoEmbed.add_field(name = 'Number of roles: ',value= len(roleList), inline=False)
        infoEmbed.add_field(name = 'User Roles: ', value = roles, inline=False)
        infoEmbed.set_thumbnail(url = target.avatar_url)
        await context.channel.send(embed = infoEmbed)

    #ping command
    @commands.command(name = 'ping')
    @commands.check(simplifications.isNotbanned)
    @commands.guild_only()    
    async def ping(self, content):
        await content.channel.send(f"""Ping is {round(self.bot.latency * 1000)}ms""")

def setup(bot):
    bot.add_cog(inkUtilCommands(bot))
