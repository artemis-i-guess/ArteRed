import discord
import random
import praw
from discord.ext import commands


reddit = praw.Reddit(client_id = "OEkJ7YUzngU4mutsyoMDGg",client_secret= "infroVmU5wjB2-Hefb1G3Hk11BAlrg", username = "Educational_Owl1957", password = "chessing63times", user_agent = "pythonwrapper")


class emb(commands.Cog):

  def __init__(self, client):
    self.client = client
 

  @commands.command()
  async def pfp(self,ctx,member:discord.Member):
    embed = discord.Embed(title = member.name, color = discord.Color.purple())
    urluser = str(member.avatar_url)
    embed.set_image(url = urluser)
    await ctx.send(embed=embed)


  @commands.command()
  async def red(self,ctx,subred= "memes"):
    
    subreddit = reddit.subreddit(subred)

    subsarray=[]

    for submission in subreddit.top(limit = 10):
      subsarray.append(submission)


    randomsub = random.choice(subsarray)
    name = randomsub.title 
    url = randomsub.url

    embed = discord.Embed(title = name)
    embed.set_image(url = url)

    embed.set_footer(icon_url = ctx.author.avatar_url, text = "Requested by " + str(ctx.author.name))
    
    await ctx.send(embed=embed)

  @commands.command()
  async def gay(self,ctx,member:discord.Member):
    embed= discord.Embed(title = "Gaymeter",color = discord.Color.red())
    value = random.randint(1,100)

    embed.add_field(name = "The gaymeter for " + str(member.name) + " stands at " + str(value)+"%" ,value =member.name )
    
    await ctx.send(embed=embed)



  
def setup (client):
  client.add_cog(emb(client))