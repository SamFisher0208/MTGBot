import discord  #discord library
import os
from dotenv import load_dotenv
import postCards


client = discord.Client()

load_dotenv()

TOKEN = os.getenv("TOKEN")

@client.event
async def on_ready():
    #this just changes the status of the bot
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='[Scryfall]'))
    print('We have logged in as {0.user}'.format(client))
      
    
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("!randcard") or message.content.startswith("!vibes"):
    await message.channel.send(postCards.getVibe())
  
  if message.content.startswith("!randcreature"):
    await message.channel.send(postCards.getCreature())

  if message.content.startswith("!randinstant"):
    await message.channel.send(postCards.getInstant())

  if message.content.startswith("!randsorcery"):
    await message.channel.send(postCards.getSorcery())

  if message.content.startswith("!castinstant"):
    for member in message.mentions:
      victim = member.mention
    
    cast = f"{victim} was casted upon!\n{postCards.getInstant()}"
    await message.channel.send(cast)

  if message.content.startswith("!castsorcery"):
    for member in message.mentions:
      victim = member.mention
    
    cast = f"{victim} was casted upon!\n{postCards.getSorcery()}"
    await message.channel.send(cast)
  
  #if message.content.startswith("[["):



client.run(TOKEN)

