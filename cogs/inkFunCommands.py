from discord import message
from discord.ext import commands
import random
import discord
from discord.ext.commands import MemberNotFound
from discord.ext.commands import MissingRequiredArgument
from utils import simplifications

describeList = ['big nab','a qt','simp','hot','friendly','an irritating bitch','an ass','a dick','a hoe','dum','tiny','the best','the poggest','sweet','cute','<:bigbrain:838472543705759824>','teeny brain','an alien','a waifu','a dumbass']
pickupLines = ['I hope you know CPR, because you just took my breath away!','So, aside from taking my breath away, what do you do for a living?','I ought to complain to Spotify for you not being named this week’s hottest single.','Are you a parking ticket? ‘Cause you’ve got ‘fine’ written all over you.','Your eyes are like the ocean; I could swim in them all day.','When I look in your eyes, I see a very kind soul.','If you were a vegetable, you’d be a ‘cute-cumber.’','Do you happen to have a Band-Aid? ‘Cause I scraped my knees falling for you.','I never believed in love at first sight, but that was before I saw you.',' I didn’t know what I wanted in a woman until I saw you.','I was wondering if you could tell me: If you’re here, who’s running Heaven?','(at night) No wonder the sky is dark all the color is in your eyes.','You’ve got everything I’ve been searching for, and believe me—I’ve been looking a long time.','You’re like a fine wine. The more of you I drink in, the better I feel.','You’ve got a lot of beautiful curves, but your smile is absolutely my favorite.','Are you as beautiful on the inside as you are on the outside?','If being sexy was a crime, you’d be guilty as charged.','I was wondering if you’re an artist because you were so good at drawing me in.','It says in the Bible to only think about what’s pure and lovely… So I’ve been thinking about you all day long.','Do you have a map? I just got lost in your eyes.','I’d like to take you to the movies, but they don’t let you bring in your own snacks.','You know what you would look really beautiful in? My arms.','I would never play hide and seek with you because someone like you is impossible to find.','Are you a magician? It’s the strangest thing, but every time I look at you, everyone else disappears.','I think there’s something wrong with my phone. Could you try calling it to see if it works?','Hi, I just wanted to thank you for the gift. (pause) I’ve been wearing this smile ever since you gave it to me.','Are you an electrician? Because you’re definitely lighting up my day/night!','I’ve heard it said that kissing is the ‘language of love.’ Would you care to have a conversation with me about it sometime?','I always thought happiness started with an ‘h,’ but it turns out mine starts with ‘u.’','I believe in following my dreams. Can I have your Instagram?','Do you know what the Little Mermaid and I have in common? We both want to be part of your world.','If you were a song, you’d be the best track on the album.','You know, I always thought that Disneyland was the ‘happiest place on Earth,’ but that was before I got a chance to stand here next to you.','Want to go outside and get some fresh air with me? You just took my breath away.','If you were a taser, you’d be set to ‘stun.’','If you were a Transformer, you’d be ‘Optimus Fine.’','Is your name Google? Because you have everything I’m searching for.','Do you ever get tired from running through my thoughts all night?','You know, they say that love is when you don’t want to sleep because reality is better than your dreams. And after seeing you, I don’t think I ever want to sleep again.','Trust me, I’m not drunk; I’m just intoxicated by you.','Do you have a name, or can I just call you ‘mine?’','if u were a fruit, you\'d be a fineapple','Are you a tazer? cause you\'re stunning']
eightBallOptions = ['As I see it, yes','Ask again later','Better not tell you now',' Cannot predict now','Concentrate and ask again','Don’t count on it','It is certain','It is decidedly so','Most likely','My reply is no','My sources say no','Outlook not so good','Outlook good','Reply hazy, try again','Signs point to yes','Very doubtful','Without a doubt','Yes','Yes – definitely','You may rely on it']
allowedMentions = discord.AllowedMentions(everyone=False,roles=False)


class inkFunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #command to echo
    @commands.command(name = 'say')
    @commands.check(simplifications.isNotbanned)
    @commands.guild_only()    
    async def say(self,context,*,whatToSay):
        await context.message.channel.send(whatToSay,allowed_mentions=allowedMentions)  

    @say.error
    async def say_error(self,ctx,error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send('Follow the syntax:\n```ink say <content>```')


    #gives a description of the person mentioned
    @commands.command(name = 'describe')
    @commands.check(simplifications.isNotbanned)
    @commands.guild_only()    
    async def describe(self, context, target : discord.Member):
        #rigging it for myself
        if target.id == 652756616185380894: 
            await context.message.channel.send(f'''{target.name} is awesome''', allowed_mentions = allowedMentions)
        else:
            await context.channel.send(f'''{target.name} is {random.choice(describeList)}''', allowed_mentions = allowedMentions)

    @describe.error
    async def describe_error(self, cxt, error):
        if isinstance(error, MemberNotFound):
            await cxt.channel.send('Oi gimme an actual member to describe <a:PI_Angry:838736380674572328>')
        elif isinstance(error, MissingRequiredArgument):
            await cxt.send('Follow the syntax:\n```ink describe <member>```')
        else:
            pass

    #iq command
    @commands.command(name='iq')
    @commands.check(simplifications.isNotbanned)
    @commands.guild_only()    
    async def iq(self, cxt,target : discord.Member):
        #rigging it for myself
        if target.id == 652756616185380894:
            personIq = 160
        else:
            personIq = random.randint(a= 40, b= 160)
        
        if personIq >= 116:
            personEmoji = '<:bigbrain:838472543705759824>'
        elif personIq >= 84:
            personEmoji = ':brain:'
        elif personIq >= 40:
            personEmoji = '<:dumbfuck:838730636175998976>'
        
        iqEmbed = discord.Embed(title=f"""{target.name}'s iq:""",description=f"""{target.mention} has an iq of {str(personIq)} {personEmoji}""",color= 0xabcdef)
        await cxt.send(embed= iqEmbed)


    @iq.error
    async def iq_error(self,cxt, error):
        if isinstance(error, MemberNotFound):
            await cxt.channel.send('Oi gimme an actual member to find iq of <a:PI_Angry:838736380674572328>')
        elif isinstance(error, MissingRequiredArgument):
            await cxt.send('Follow the syntax:\n```ink iq <member>```')
        else:
            pass

    #flirt command
    @commands.command(name = 'besmooth')
    @commands.check(simplifications.isNotbanned)
    @commands.guild_only()    
    async def besmooth(self,context):
        await context.message.channel.send(random.choice(pickupLines))
    
    #8ball cmd
    @commands.command(name = '8ball')
    @commands.check(simplifications.isNotbanned)
    @commands.guild_only()    
    async def eightball(self,ctx):
        if 'adi' in ctx.message.content:
            await ctx.send(f'dont ask me stuff about my creator, idk')
        else:
            await ctx.channel.send(f""":crystal_ball:{random.choice(eightBallOptions)}, {ctx.author.name}""", allowed_mentions = allowedMentions)

    @eightball.error
    async def eightball_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.send('Give me something to predict <:facepalm:838671083481333781>')
        else:
            pass
        

def setup(bot):
    bot.add_cog(inkFunCommands(bot))
