#importing required stuff
import discord

#whois command code
async def whois(context,target : discord.User):
    whoIsEmbed = discord.Embed(title=f"""UserInfo for {target.display_name}""",color=0xabcdef)
    whoIsEmbed.add_field(name = "User Id:", value = target.id,inline=False)
    whoIsEmbed.add_field(name = "User Name:", value =f"""{target.name}#{target.discriminator}""",inline=False)
    whoIsEmbed.add_field(name = "User account creation date:", value = str(target.created_at)[0:16],inline=False)
    whoIsEmbed.set_thumbnail(url = target.avatar_url)
    await context.channel.send(embed = whoIsEmbed)


#info command code
async def info(context,target : discord.Member):
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