#importing requirements
import discord
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument

#the actual cog
class banRoulette(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name='banrouletteban', aliases=['brb'])
    async def banrouletteban(self,ctx,target : discord.Member):
        if ctx.message.guild.id == 841312145991532565:
            allowedRole = ctx.guild.get_role(841315457806106624)
            cantBeBannedRole = ctx.guild.get_role(841314821786173450)
            iGotBannedRole = ctx.guild.get_role(841336094771642378)
            alreadyBannedRole = ctx.guild.get_role(841336094771642378)
            allowedMentions = discord.AllowedMentions(everyone=False,roles=False)
            if allowedRole in ctx.author.roles:
                if cantBeBannedRole not in target.roles:
                    if ctx.channel.id == 841357068807176203:
                        if alreadyBannedRole not in target.roles:  
                            for role in target.roles:
                                if role == allowedRole:
                                    await target.remove_roles(role)
                            await target.add_roles(iGotBannedRole)
                            await target.send(f'You got banned in ban roulette by {ctx.author.name}#{ctx.author.discriminator} 2bad4you <a:slowkek:838803911686750209>\nHeres a link to rejoin: https://discord.gg/GyPxKEYf8z')
                            #await ctx.guild.ban(user=target,reason='You got banned in ban roulette 2bad4you',delete_message_days=0)
                            await ctx.channel.send(f'{ctx.author.mention} banned {target.mention}!')
                            #await ctx.guild.unban(user=target)
                        else:
                            await ctx.send('This user\'s already been banned, give them a break <a:waca:786168442649968651>')
                    else:
                        await ctx.send('this can only be used in <#841357068807176203>')
                else:
                    await ctx.send('You cant ban Admins BAHAHAH')
            else:
                await ctx.send('you cant ban yet, make sure you have the <@&841315457806106624> role',allowed_mentions=allowedMentions)
    
    @banrouletteban.error
    async def banrouletteban_error(self, ctx, error):
        if isinstance(error,MissingRequiredArgument):
            await ctx.channel.send(f'Missing arguemnts, make sure you follow the syntax:\n```ink banrouletteban <member>```')
        else:
            pass

                
#loading the cog
def setup(bot):
    bot.add_cog(banRoulette(bot))