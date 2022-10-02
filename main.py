import discord
import random
from discord.ext import commands
import reddit
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

cogs = [reddit,]

client = commands.Bot(command_prefix='=', intents = discord.Intents.all())


for i in range (len(cogs)):
 cogs[i].setup(client)



@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game(name = "yo mom" ))
    print ("logged into server as {0.user}".format(client))


@commands.command()
async def pfp(self,ctx,member:discord.member):
   embed = discord.Embed(title = member.name,)
   embed.set_thumbnail(url=member.avatar)
   await ctx.send(embed=embed)

client.run(BOT_TOKEN)
