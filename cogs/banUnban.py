#importing requirements
import discord
from discord.ext import commands
from discord.ext.commands.core import command
import pymongo
import secrets



class banUnban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

   

def setup(bot):
    bot.add_cog(banUnban(bot))
