'''
1. WHAT IS THIS FILE?
This is the file containing all the autoresponse features for ink

2.WHAT ARE THE AUTORESPONSES HERE?
(a) ping
(b) basic help cmd with ping

IMPORTS:
1. discord cause discord
2. commands from discord.ext cause its wat the cog runs on
3. is_not_bot_banned to keep banned members from using the commands
'''
import discord
from discord.ext import commands
from utils.botwideFunctions import is_not_bot_banned


'''
VARIABLES
1. allowed_mentions - restricts mentions to user only on send calls when specified
'''
allowedMentions = discord.AllowedMentions(everyone=False,roles=False)

class inkAutoResponses(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    '''
    The 'ping' autoresponse:
    Makes the bot react with an emoji whenever one of the added people are mentioned
    '''
    @commands.Cog.listener("on_message")
    async def ping_ars(self,message):
        if len(message.mentions) > 0:
            for ok_someones_ping in message.mentions:
                #adi's ar
                #dumbfuck.
                if ok_someones_ping.id == 652756616185380894:
                    await message.add_reaction('<a:kittychase:848579766743597076>')
                #ceee's ar <3
                elif ok_someones_ping.id == 696754560429064263:
                    await message.add_reaction('<:an_urcute:776896089760333844>')
                #stick's ar 
                elif ok_someones_ping.id == 662114929754505217:
                    await message.add_reaction('<:angelsmile:846039595560992768>')
                #orions's ar :-:
                elif ok_someones_ping.id == 749126083416162375:
                    await message.add_reaction('<:pepeblush:846078935477518357>')
                #que's ar :)
                elif ok_someones_ping.id == 461496649324167168:
                    await message.add_reaction('<a:loveroll:846277965461323857>')
                #jorja's ar :)
                elif ok_someones_ping.id == 727431252541440040:
                    await message.add_reaction('<:stitchlove:846035269119115274>')
                #maverick's ar ( ^ - ^ )
                elif ok_someones_ping.id == 707247009035321465:
                    await message.add_reaction('<a:Raspberry:847390536956510238>')
                #Kaya's ar ( ^ - ^ )
                elif ok_someones_ping.id == 617332029993910352:
                    await message.add_reaction('<a:leave:848936937465184287>')
                #Tom's ar ( ^ - ^ )
                elif ok_someones_ping.id == 673861958398640140:
                    await message.add_reaction('<a:pandaclap:848937165035274260>')
                #Vian's ar ( ^ - ^ )
                elif ok_someones_ping.id == 690431027881050135:
                    await message.add_reaction('<a:animedance:870871655486980107>')
                    

    
    @commands.Cog.listener("on_message")
    @is_not_bot_banned()
    async def ink_mention_response(self,message):
        if str(message.content) == f'''<@!{self.bot.user.id}>''' or str(message.content) == f'''<@{self.bot.user.id}>''' and message.author.bot == False:
            await message.channel.send('Hi! My prefix is `ink `, run `ink help` for more details!!',delete_after=5)

def setup(bot):
    bot.add_cog(inkAutoResponses(bot))
    print("""Cog inkAutoResponses has loaded successfully
--------------------""")