'''
1.WHAT IS THIS FILE?
This is the fun command cog  hosting commands that are for entertainment purposes only

2. WHAT ARE THE COMMANDS HERE?
The commands (in order of addition to the bot) are as follows:
(a) say
(b) iq
(c) describe
(d) besmooth


IMPORTS:
1. Discord to define many of the elements used
2. Commands from discord.ext to load the cog and to run bot commands
3. stuff from commands.errors to do error handling
4. random to choose a pickup line for besmooth
5. typing to add optional args
6. is_not_bot_banned to stop bot banned people from using commands
7. commandsShortenings to run functions that will reduce repition of long functions in commands 
'''
import discord
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument
import random
import typing
from utils.botwideFunctions  import is_not_bot_banned
from utils.commandShortenings import make_iq_embed,get_description


'''
Variables i use in the cog
allowedMentions is used to disable everyone and role pings in the say command
pickup_list is the list of all lines for besmooth
eightball_list is the list of all eightball lines
'''
allowed_mentions = discord.AllowedMentions(everyone=False,roles=False)
pickup_list = ["I could've fallen off a building, could've fallen off a tree, but instead, i decided to fall in love with you", 'I hope you know CPR, because you just took my breath away!', 'I ought to complain to Spotify for you not being named this week’s hottest single.', 'Are you a parking ticket? ‘Cause you’ve got ‘fine’ written all over you.', 'Your eyes are like the ocean I could swim in them all day.', 'When I look in your eyes, I see a very kind soul.', 'Do you happen to have a BandAid? ‘Cause I scraped my knees falling for you.', 'I never believed in love at first sight, but that was before I saw you.', ' I didn’t know what I wanted in a person until I saw you.', 'I was wondering if you could tell me: If you’re here, who’s running Heaven?', '(at night) No wonder the sky is dark all the color is in your eyes.', 'You’ve got everything I’ve been searching for, and believe me—I’ve been looking a long time.', 'You’re like a fine wine. The more of you I drink in, the better I feel.', 'You’ve got a lot of beautiful curves, but your smile is absolutely my favorite.', 'Are you as beautiful on the inside as you are on the outside?', 'If being sexy was a crime, you’d be guilty as charged.', 'I was wondering if you’re an artist because you were so good at drawing me in.', 'It says in the Bible to only think about what’s pure and lovely… So I’ve been thinking about you all day long.', 'Do you have a map? I just got lost in your eyes.', 'I’d like to take you to the movies, but they don’t let you bring in your own snacks.', 'You know what you would look really beautiful in? My arms.', 'I would never play hide and seek with you because someone like you is impossible to find.', 'Are you a magician? It’s the strangest thing, but every time I look at you, everyone else disappears.', 'I think there’s something wrong with my phone. Could you try calling it to see if it works?', 'Hi, I just wanted to thank you for the gift. . .\n\nI’ve been wearing this smile ever since you gave it to me.', 'Are you an electrician? Because you’re definitely lighting up my night!', 'I’ve heard it said that kissing is the ‘language of love.’ Would you care to have a conversation with me about it sometime?', 'I always thought happiness started with an ‘h,’ but it turns out mine starts with ‘u.’', 'I believe in following my dreams. Can I have your Instagram?', 'Do you know what the Little Mermaid and I have in common? We both want to be part of your world.', 'If you were a song, you’d be the best track on the album.', 'You know, I always thought that Disneyland was the ‘happiest place on Earth,’ but that was before I got a chance to stand here next to you.', 'Want to go outside and get some fresh air with me? You just took my breath away.', 'If you were a taser, you’d be set to ‘stun.’', 'If you were a Transformer, you’d be ‘Optimus Fine.’', 'Is your name Google? Because you have everything I’m searching for.', 'Do you ever get tired from running through my thoughts all night?', 'You know, they say that love is when you don’t want to sleep because reality is better than your dreams. And after seeing you, I don’t think I ever want to sleep again.', 'Trust me, I’m not drunk; I’m just intoxicated by you.', 'Do you have a name, or can I just call you ‘mine?’', "if u were a fruit, you'd be a fineapple", "Are you a tazer? cause you're stunning", "Don't clap! You've got my heart in your hands", "I'd swim in your eyes, but i don't know deep sea diving", "we can never be far apart, cause you're always on my mind", 'You should try loving anime\nWithout ani', 'I can’t turn water into wine\nBut I can turn you into mine', 'I fell so far falling for you, that i thought i was flying', 'Did you just come out of the oven? Because you’re hot', 'Anyone who says Disneyland is the happiest place on Earth has clearly never stood next to you', 'Are you a magician? Because when I’m looking at you, you make everyone else disappear!', 'They say nothing lasts forever, so would you be my nothing?', 'I think there’s something wrong with my phone. Your number’s not in it', 'Life without you is like a broken pencil…pointless', 'Something’s wrong with my eyes, because I can’t take them off you', "Am i dead? Cause I'm talking to an angel", 'Do you have a BandAid? I just scraped my knee falling for you', 'Are you French? Because Eiffel for you', 'I always thought happiness started with an ‘h,’ but it turns out mine starts with ‘u’', 'I’m not photographer, but I can definitely picture us together', 'You must be a hell of a thief, because you managed to steal my heart from across the room', ' My friends bet me I couldn’t talk to the prettiest girl in the bar. Want to use their money to buy some drinks?', 'I wish I’d paid more attention to science in high school, because you and I’ve got chemistry and I want to know all about it', 'Do you like Star Wars? Because Yoda only one for me!', "You and I are like nachos with jalapeños. I'm super cheesy, you're super hot, and we belong together.", 'Are you a camera? Because every time I look at you, I smile.', 'Is there an airport nearby, or was that just my heart taking off?', "I'm in the mood for pizza. A pizza you, that is!", "You're so sweet, you could put Hershey's out of business!"]
eightball_list = ['As I see it, yes','Ask again later','Better not tell you now',' Cannot predict now','Concentrate and ask again','Don’t count on it','It is certain','It is decidedly so','Most likely','My reply is no','My sources say no','Outlook not so good','Outlook good','Reply hazy, try again','Signs point to yes','Very doubtful','Without a doubt','Yes','Yes – definitely','You may rely on it']


#making the class, which is practaclly all the commands for the inkFunCommands cog
class inkFunCommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    '''
    The 'say' command:
    Running the command makes the bot repeat the given message (in a certain chanel if provided)
    '''
    @commands.command(name='say')
    @is_not_bot_banned()
    @commands.guild_only()
    async def say(self,ctx,channel : typing.Optional[discord.TextChannel]=None,*,watToSay):
        allowed_mentions = discord.AllowedMentions(everyone=False,roles=False,users=False)
        if channel is None:
            await ctx.send(watToSay,allowed_mentions = allowed_mentions)
        if channel is not None:
            if channel.permissions_for(ctx.author).send_messages == True: 
                await channel.send(watToSay,allowed_mentions = allowed_mentions)
                await ctx.send(f'Message has been sent in {channel.mention}',delete_after=5)
            else:
                await ctx.reply(f'Don\'t try making me say stuff in channels where you don\'t have perms <:lolnub:842673428695744522>')
        
    @say.error
    async def say_error(self,ctx,error):
        if isinstance(error,MissingRequiredArgument):
            await ctx.send(f'```ink say [channel] <message>\n\nMake sure to supply a message!```',allowed_mentions = allowed_mentions)
        
    '''
    The'iq' command:
    Gives the iq of the target (or the invoker if no target is provided)
    '''
    @commands.command(name='iq')
    @is_not_bot_banned()
    @commands.guild_only()
    async def iq(self,ctx,target : typing.Optional[discord.Member]=None):
        if target is not None:
            iq_embed = make_iq_embed(target)
            await ctx.send(embed=iq_embed)
        else:
            iq_embed = make_iq_embed(ctx.author)
            await ctx.send(embed=iq_embed)

    '''
    The 'describe' command:
    Gives a description of the target (or invoker if target isnt supplied)
    '''
    @commands.command(name='describe')
    @is_not_bot_banned()
    @commands.guild_only()
    async def describe(self,ctx,target : typing.Optional[discord.Member]=None):
        if target is not None:
            description = get_description(target)
            await ctx.send(f'{target.name} is {description}',allowed_mentions=allowed_mentions)
        else:
            description = get_description(ctx.author)
            await ctx.send(f'{ctx.author.name} you\'re {description}',allowed_mentions=allowed_mentions)

    '''
    The 'besmooth' command
    Gives a pickup line
    '''
    @commands.command(name='besmooth')
    @is_not_bot_banned()
    @commands.guild_only()
    async def besmooth(self,ctx):
        pickup_line = random.choice(pickup_list)
        await ctx.send(pickup_line,allowed_mentions=allowed_mentions)
    
    '''
    The '8ball' command
    Predicts the future
    '''
    @commands.command(name='8ball')
    @is_not_bot_banned()
    @commands.guild_only()
    async def eight_ball(self,ctx,*,question):
        eightball_output = random.choice(eightball_list)
        await ctx.send(f':crystal_ball:{eightball_output}, {ctx.author.name}',allowed_mentions=allowed_mentions)

    @eight_ball.error
    async def eight_ball_error(self,ctx,error):
        if isinstance(error,MissingRequiredArgument):
            await ctx.send('Oi! Gimme something to predict <a:PI_Angry:838736380674572328>')

#running the setup for the cog
def setup(bot):
    bot.add_cog(inkFunCommands(bot))
    print("""Cog inkFunCommands has loaded successfully
--------------------""")