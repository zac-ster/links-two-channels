# There are nothing to do here.
#Go to config.py to setup everything
from aiohttp import ClientSession

import discord, os, keep_alive, config

from discord.ext import commands as coms

bot = coms.Bot(command_prefix=">", intents=discord.Intents.all())

@bot.event

async def on_ready():
  print("Ready!")

@bot.event

async def on_message(msg):
    
  for guild in bot.guilds:
    if msg.author not in guild.members:
      return
  
  if msg.channel.id == config.CHANNELID1:
    async with ClientSession() as session:
      
          webhook2 = discord.Webhook.from_url(config.WEBHOOK_URL2, adapter=discord.AsyncWebhookAdapter(session))

          await webhook2.send(content=f"{msg.content}", username=msg.author.name, avatar_url=msg.author.avatar_url)

  elif msg.channel.id == config.CHANNELID2:
    async with ClientSession() as session:
      
          webhook1 = discord.Webhook.from_url(config.WEBHOOK_URL1, adapter=discord.AsyncWebhookAdapter(session))

          await webhook1.send(content=f"{msg.content}", username=msg.author.name, avatar_url=msg.author.avatar_url)

keep_alive.keep_alive()
bot.run(config.token)