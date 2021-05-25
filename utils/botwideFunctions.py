'''
WHAT IS THIS FILE?
This is the file where i dump all my custom functions which have bot wide implications!!

WHAT ARE THE FUNCTIONS HERE?
1. is_not_bot_banned
2. is_admin
3. is_mod
4. is_gman
5. is_eman


IMPORTS:
1. pymongo to connect and do stuff with my database
2. load to load the collect the cluster name
3. pathlib to define a path to secrets.json
4. commands to help define checks
'''
import pymongo
from json import load
from pathlib import Path
from discord.ext import commands

'''
Variables i use:
1. cluster - my bot's mongodb cluster 
'''
with Path("utils/secrets.json").open() as f:
    config = load(f)
cluster = config["cluster"]
cluster = pymongo.MongoClient(cluster)

'''
is_not_bot_banned function:
Checking if a user has been bot banned or not
'''
def is_not_bot_banned():
    def predicate(ctx):
        bans_collection = cluster['banned']['Ids']
        everything_in_bans = bans_collection.find()
        bannedList = []
        for result in everything_in_bans:
            if result is not None:
                bannedList.append(result['_id'])
        return ctx.author.id not in bannedList
    return commands.check(predicate)

'''
is_admin function:
checks if the invoker has the admin role if it has been set for a server
'''
def is_admin():
    def predicate(ctx):
        settings_collection = cluster[str(ctx.guild.id)]['serverSettings']
        admin_role_space = settings_collection.find_one({"_id" : 'adminRole'})
        admin_role_id = admin_role_space["role"]
        if admin_role_id is not None:
            admin_role = ctx.guild.get_role(admin_role_id)
            return admin_role in ctx.author.roles
        else:
            return False
    return commands.check(predicate)

'''
is_mod function:
checks if the invoker has the mod role if it has been set for a server
'''
def is_mod():
    def predicate(ctx):
        settings_collection = cluster[str(ctx.guild.id)]['serverSettings']
        mod_role_space = settings_collection.find_one({"_id" : 'modRole'})
        mod_role_id = mod_role_space["role"]
        if mod_role_id is not None:
            mod_role = ctx.guild.get_role(mod_role_id)
            return mod_role in ctx.author.roles
        else:
            return False
    return commands.check(predicate)


'''
is_gman function:
checks if the invoker has the gman role if it has been set for a server
'''
def is_gman():
    def predicate(ctx):
        settings_collection = cluster[str(ctx.guild.id)]['serverSettings']
        gman_role_space = settings_collection.find_one({"_id" : 'giveawayManagerRole'})
        gman_role_id = gman_role_space["role"]
        if gman_role_id is not None:
            gman_role = ctx.guild.get_role(gman_role_id)
            return gman_role in ctx.author.roles
        else:
            return False
    return commands.check(predicate)


'''
is_eman function:
checks if the invoker has the eman role if it has been set for a server
'''
def is_eman():
    def is_eman_predicate(ctx):
        settings_collection = cluster[str(ctx.guild.id)]['serverSettings']
        eman_role_space = settings_collection.find_one({"_id" : 'eventManagerRole'})
        eman_role_id = eman_role_space["role"]
        if eman_role_id is not None:
            eman_role = ctx.guild.get_role(eman_role_id)
            return eman_role in ctx.author.roles
        else:
            return False
    return commands.check(is_eman_predicate)