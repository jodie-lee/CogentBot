# Date Created: June 8, 2021
# Date Updated: June 15, 2021
# Author: Jodie Lee
# Description: simple dice rolling bot for cogent roleplay
# Credit: adapted from https://github.com/Rapptz/discord.py/blob/v1.7.3/examples/basic_bot.py

import discord
from discord.ext import commands
import os
import random as rand

# bot set up
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix = '-', intents = intents)
client = discord.Client(activity=discord.Game(name='-help'))

# on start up
@bot.event
async def on_ready():
  print(f'Successfully connected as {bot.user}')


# roll command
@bot.command(name = 'roll', help = 'rolls the corresponding number of D6s')
async def roll(ctx, number: int):
  '''rolls the corresponding number of D6s'''
  rolls = []
  wins = 0
  success = [4, 5, 6]
  for i in range(number):
    rolls.append(rand.randint(1, 6))
    
  for j in rolls:
    if (j in success):
      wins += 1
    
  await ctx.send('[' + ', '.join([str(x) for x in rolls]) + ']')

  if (wins == 1):
    await ctx.send('You rolled 1 success!')
  else:
    message = 'You rolled ' + str(wins) + ' successes!'
    await ctx.send(message)

# advantage command
@bot.command(name = 'advantage', help = 'rolls the corresponding number of D6s with advantage')
async def advantage(ctx, number: int):
  '''rolls the corresponding number of D6s with advantage'''
  rolls = []
  wins = 0
  success = [3, 4, 5, 6]
  for i in range(number):
    rolls.append(rand.randint(1, 6))
    
  for j in rolls:
    if (j in success):
      wins += 1
    
  await ctx.send('[' + ', '.join([str(x) for x in rolls]) + ']')

  if (wins == 1):
    await ctx.send('You rolled 1 success!')
  else:
    message = 'You rolled ' + str(wins) + ' successes!'
    await ctx.send(message)

# destiny command
@bot.command(name = 'destiny', help = 'makes a destiny roll')
async def destiny(ctx):
  '''makes a destiny roll'''
  message = 'You rolled a ' + str(rand.randint(1, 20)) + '!'
  await ctx.send(message)

# combat command
@bot.command(name = 'combat', help = 'makes a combat roll and determines the winner')
async def combat(ctx, player1: str, num1: int, player2: str, num2: int):
  '''makes a combat roll and determines the winner'''
  # rolling for player 1
  rolls1 = []
  win1 = 0
  success = [4, 5, 6]
  
  for i in range(num1):
    rolls1.append(rand.randint(1, 6))
  for j in rolls1:
    if j in success:
      win1 += 1

  await ctx.send(player1 + ': [' + ', '.join([str(x) for x in rolls1]) + ']')

  # rolling for player 2
  rolls2 = []
  win2 = 0

  for x in range(num2):
    rolls2.append(rand.randint(1, 6))
  for y in rolls2:
    if y in success:
      win2 += 1

  await ctx.send(player2 + ': [' + ', '.join([str(x) for x in rolls2]) + ']')
  
  # determining the winner
  if win1 > win2:
    victory = win1 - win2
    message = player1 + ' scored ' + str(victory) + ' victory level(s) over ' + player2
    await ctx.send(message)

  elif win2 > win1:
    victory = win2 - win1
    message = player2 + ' scored ' + str(victory) + ' victory level(s) over ' + player1
    await ctx.send(message)

  else:
    await ctx.send('There was a tie in successes: please remake your rolls.')


# start bot
token = os.getenv('DISCORD_BOT_SECRET')
bot.run(token)