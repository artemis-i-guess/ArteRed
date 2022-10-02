import discord
import random
import praw
from discord.ext import commands
import os
from dotenv import load_dotenv # <- This is used to find and use .env files

load_dotenv()

# Imported from config.env file -> 
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                     username=USERNAME, password=PASSWORD, user_agent="pythonwrapper")


class emb(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def red(self, ctx, subred="memes"):

        subreddit = reddit.subreddit(subred)
        subsarray = []

        for submission in subreddit.top(limit=50):
            subsarray.append(submission)

        randomsub = random.choice(subsarray)
        name = randomsub.title
        url = randomsub.url

        embed = discord.Embed(title=name)
        embed.set_image(url=url)

        embed.set_footer(text="Requested by " + str(ctx.author.name))

        await ctx.send(embed=embed)

    @commands.command()
    async def gay(self, ctx, member: discord.Member):
        embed = discord.Embed(title="Gaymeter", color=discord.Color.red())
        value = random.randint(1, 100)

        embed.add_field(name="The gaymeter for " + str(member.name) +
                        " stands at " + str(value)+"%", value=member.name)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(emb(client))
