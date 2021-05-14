#importing requirements
import discord
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument
from discord.ext.commands.core import command
import pymongo
import varsToNotCopy

#defining my database
dbclient = pymongo.MongoClient(varsToNotCopy.clusterName)
bancollection = dbclient['banCount']['perMember']


#the actual cog
class banRoulette(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command(name='banrouletteban', aliases=['brb'])
    @commands.guild_only()
    async def banrouletteban(self,ctx,target : discord.Member):
        dtbr = await self.bot.fetch_guild(841312145991532565)
        if ctx.guild != dtbr:
            return
        allowedRole = ctx.guild.get_role(841315457806106624)
        cantBeBannedRole = ctx.guild.get_role(841314821786173450)
        iGotBannedRole = ctx.guild.get_role(841336094771642378)
        alreadyBannedRole = ctx.guild.get_role(841336094771642378)
        allowedMentions = discord.AllowedMentions(everyone=False,roles=False)
        if allowedRole in ctx.author.roles:
            if cantBeBannedRole not in target.roles:
                if ctx.channel.id == 841357068807176203 or ctx.channel.id == 841317703037616168:
                    if alreadyBannedRole not in target.roles:  
                        for role in target.roles:
                            if role == allowedRole:
                                await target.remove_roles(role)
                        await target.add_roles(iGotBannedRole)
                        await target.send(f'You got banned in ban roulette by {ctx.author.name}#{ctx.author.discriminator} 2bad4you <a:slowkek:838803911686750209>')
                        #await ctx.guild.ban(user=target,reason='You got banned in ban roulette 2bad4you',delete_message_days=0)
                        await ctx.channel.send(f'{ctx.author.mention} banned {target.mention}!')
                        #await ctx.guild.unban(user=target)
                        authorID = ctx.author.id
                        status = bancollection.find_one({'_id' : authorID})
                        if status is None:
                            person = {'_id' : authorID , "numberOfBans": 1}
                            bancollection.insert_one(person)
                        else:
                            myquery = {'_id' : authorID}
                            newBanNumber = status['numberOfBans'] + 1
                            bancollection.update_one(myquery,{"$set":{"numberOfBans": newBanNumber}})

                    else:
                        await ctx.send('This user\'s already been banned, give them a break <a:waca:786168442649968651>')
                else:
                    await ctx.send('this can only be used in <#841317703037616168>')
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

    @commands.command(name='clearLb')
    @commands.guild_only()
    async def clearLb(self,ctx):
        dtbr = await self.bot.fetch_guild(841312145991532565)
        if ctx.guild != dtbr:
            return
        adminRole = ctx.guild.get_role(841314821786173450)
        if adminRole in ctx.author.roles:
            print(f'{ctx.author} cleared the leaderboard!')
            bancollection.drop()
            await ctx.send('Leaderboard has been cleared')
        else:
            await ctx.send('Only admins can run this command')
    
    @commands.command(name='showLb')
    @commands.guild_only()
    async def showLb(self,ctx):
        dtbr = await self.bot.fetch_guild(841312145991532565)
        if ctx.guild != dtbr:
            return
        modRole = ctx.guild.get_role(841523062360113174)
        if modRole in ctx.author.roles:
            lbRaw = bancollection.find().limit(10).sort("numberOfBans", -1)
            i = 1
            lbEmbed = discord.Embed(title='Dank Trades Ban Royale Leaderboard',colour=0xabcdef)
            for personData in lbRaw:
                if personData is not None:
                    personId = int(personData["_id"])
                    person = await ctx.guild.fetch_member(personId)
                    personName = person.name
                    personBans = personData["numberOfBans"]
                    lbEmbed.add_field(name=f'**#{i}**',value=f'> Member = {personName}\n> ID = {personId}\n> Number of bans = {personBans}',inline=False)
                    i += 1
            await ctx.send(embed=lbEmbed)

    @commands.command(name='mybans')
    @commands.guild_only()
    async def mybans(self,ctx):
        dtbr = await self.bot.fetch_guild(841312145991532565)
        if ctx.guild != dtbr:
            return
        personId = ctx.author.id
        personData = bancollection.find_one({'_id' : personId})
        if personData is not None:
            await ctx.send(f'{ctx.author.mention} You have {personData["numberOfBans"]} bans!')
        else:
            await ctx.send(f'{ctx.author.mention} Couldnt find any bans by you, probably cause you dont have any <:lolnub:842673428695744522>')



    @commands.Cog.listener()
    async def on_message(self,message):
        dtbr = await self.bot.fetch_guild(841312145991532565)
        if message.guild == dtbr:
            return
        ctx = await self.bot.get_context(message)
        memberRoles = []
        cantalk = [841314821786173450,841667898162675763,841331662205354025,841312605187866645,841693690246463550,838390757449662496,841697013758165014]
        banRoyaleTestChannel = ctx.guild.get_channel(841357068807176203)
        banRoyaleChannel = ctx.guild.get_channel(841317703037616168)
        if message.channel == banRoyaleChannel or message.channel == banRoyaleTestChannel:
            for role in message.author.roles:
                memberRoles.append(role.id)
            if len(set(cantalk).intersection(memberRoles)) < 1:
                if ctx.valid == False:
                    await message.delete()


#loading the cog
def setup(bot):
    bot.add_cog(banRoulette(bot))