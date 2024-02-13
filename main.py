import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot = commands.Bot(command_prefix='!', intents=intents)

with open("facts.txt", "r") as facts_file:
    facts = facts_file.readlines()
    size = len(facts)


@bot.command(name='fact')
async def give_random_fact(ctx):
    response = facts[random.randrange(0, size)]
    await ctx.send(response)


bot.run(TOKEN)
