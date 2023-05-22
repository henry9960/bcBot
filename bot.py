import discord
from discord.ext import commands

# Used for the random personality stuff.
import random

# Used for the API stuff
import json
import requests



# Enviroment variable stuff
import os
from dotenv import load_dotenv

# Time stuff
from datetime import datetime
currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%H:%M")

# Loads the .env file containing our Bot token.
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

# Sets the bot prefix to bc . Disables the default Discord bot help command.
bot = commands.Bot(command_prefix="bc ", help_command=None, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Online, the current date and time is", currentTime)
    channel = bot.get_channel(1109479655054004256)
    await channel.send("Black Cat activated.")

# Help command.
@bot.command()
async def help(ctx):
    await ctx.send(
        "```Command List```"
        "`bc help` | Gives you a list of commands." "\n"
        "`bc hello` | Says hello to you." "\n"
        "`bc time` | Tells you the time." "\n"
        "`bc personality` | Tells you your personality." "\n"
        "`bc dadjoke` | Tells you a dadjoke." "\n"
    )

# Command that displays the time.
@bot.command()
async def time(ctx):
    await ctx.send(f"It is currently {currentTime}.")

# Command that says hello.
@bot.command()
async def hello(ctx):
    await ctx.send("Hi, I'm Black Cat :)")

# Command that tells you your personality type.
@bot.command()
async def personality(ctx):
    await ctx.send(f"Your personality type is: " + "**__" +
        random.choice([
            "Introverted", "Extroverted", "Judging", "Perceiving", "Thinking",
            "Feeling", "Assertive", "Turbulent", "Optimistic", "Pessimistic",
            "Conscientious", "Carefree", "Emotional", "Logical", "Creative",
            "Analytical", "Traditional", "Open-minded", "Independent", "Dependable"]) + "__**!")

# Command that tells you a joke.
@bot.command()
async def dadjoke(ctx):
    await ctx.send(dadjoke_holder)
limit = 1
api_url = 'https://api.api-ninjas.com/v1/dadjokes?limit='.format(limit)
response = requests.get(api_url, headers={'X-Api-Key': 'Q0A22WsX3FMVMx28YXEIEg==dh1OKY5OpgvMNFJU'})
# Parses the JSON retrieved from the API and only includes the joke itself.
data = json.loads(response.text)
# The joke I received from the API was a list, and not a dictionary, so I convert it below.
dadjoke_holder = data[0]["joke"]


# Runs the bot.
bot.run(TOKEN)