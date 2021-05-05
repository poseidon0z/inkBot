#importing required stuff
import random
import discord
from discord.ext.commands import MemberNotFound

#base vars for the commands
describeList = ['big nab','a qt','simp','hot','friendly','an irritating bitch','an ass','a dick','a hoe','dum','tiny','the best','the poggest','sweet','cute','<:bigbrain:838472543705759824>','teeny brain','an alien','a waifu','a dumbass']
pickupLines = ['I hope you know CPR, because you just took my breath away!','So, aside from taking my breath away, what do you do for a living?','I ought to complain to Spotify for you not being named this week’s hottest single.','Are you a parking ticket? ‘Cause you’ve got ‘fine’ written all over you.','Your eyes are like the ocean; I could swim in them all day.','When I look in your eyes, I see a very kind soul.','If you were a vegetable, you’d be a ‘cute-cumber.’','Do you happen to have a Band-Aid? ‘Cause I scraped my knees falling for you.','I never believed in love at first sight, but that was before I saw you.',' I didn’t know what I wanted in a woman until I saw you.','I was wondering if you could tell me: If you’re here, who’s running Heaven?','(at night) No wonder the sky is dark all the color is in your eyes.','You’ve got everything I’ve been searching for, and believe me—I’ve been looking a long time.','You’re like a fine wine. The more of you I drink in, the better I feel.','You’ve got a lot of beautiful curves, but your smile is absolutely my favorite.','Are you as beautiful on the inside as you are on the outside?','If being sexy was a crime, you’d be guilty as charged.','I was wondering if you’re an artist because you were so good at drawing me in.','It says in the Bible to only think about what’s pure and lovely… So I’ve been thinking about you all day long.','Do you have a map? I just got lost in your eyes.','I’d like to take you to the movies, but they don’t let you bring in your own snacks.','You know what you would look really beautiful in? My arms.','I would never play hide and seek with you because someone like you is impossible to find.','Are you a magician? It’s the strangest thing, but every time I look at you, everyone else disappears.','I think there’s something wrong with my phone. Could you try calling it to see if it works?','Hi, I just wanted to thank you for the gift. (pause) I’ve been wearing this smile ever since you gave it to me.','Are you an electrician? Because you’re definitely lighting up my day/night!','I’ve heard it said that kissing is the ‘language of love.’ Would you care to have a conversation with me about it sometime?','I always thought happiness started with an ‘h,’ but it turns out mine starts with ‘u.’','I believe in following my dreams. Can I have your Instagram?','Do you know what the Little Mermaid and I have in common? We both want to be part of your world.','If you were a song, you’d be the best track on the album.','You know, I always thought that Disneyland was the ‘happiest place on Earth,’ but that was before I got a chance to stand here next to you.','Want to go outside and get some fresh air with me? You just took my breath away.','If you were a taser, you’d be set to ‘stun.’','If you were a Transformer, you’d be ‘Optimus Fine.’','Is your name Google? Because you have everything I’m searching for.','Do you ever get tired from running through my thoughts all night?','You know, they say that love is when you don’t want to sleep because reality is better than your dreams. And after seeing you, I don’t think I ever want to sleep again.','Trust me, I’m not drunk; I’m just intoxicated by you.','Do you have a name, or can I just call you ‘mine?’','if u were a fruit, you\'d be a fineapple','Are you a tazer? cause you\'re stunning']

#describe command code
async def describe(context):
    try:
        personToDescribe = context.message.mentions[0].id
        peopleDescriptions = describeList
        ranvar = (random.choice(peopleDescriptions))
        if context.message.mentions[0].id == 652756616185380894:  
            await context.message.channel.send('<@' + str(personToDescribe) + '> is awesome')
        else:
            await context.message.channel.send('<@' + str(personToDescribe) + '> is ' + ranvar)
    except IndexError:
        if context.message.content[13:18] == 'list':
            displayList = ', '.join(describeList)
            await context.message.channel.send(displayList)
        else:
            await context.message.channel.send('<@' + str(context.message.author.id) + '> mention someone to describe, dumbass <:facepalm:838671083481333781>')
        
    except:
        await context.message.channel.send('something went wrong and idfk wat')

#say command code
async def say(context,whatToSay):
    allowedMentions = discord.AllowedMentions(everyone=False,roles=False)
    await context.message.channel.send(whatToSay,allowed_mentions=allowedMentions)

#iq command code
async def iq(context, target : discord.member):
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
    await context.message.channel.send(embed= iqEmbed)


#flirt command  
async def besmooth(context):
    await context.message.channel.send(random.choice(pickupLines))