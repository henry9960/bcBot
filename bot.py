import discord
from discord.ext import commands

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
        "`bc hello` | Says hello to you." "\n"
        "`bc time` | Tells you the time."
    )

# Command that displays the time.
@bot.command()
async def time(ctx):
    await ctx.send(f"It is currently {currentTime}.")

# Command that says hello.
@bot.command()
async def hello(ctx):
    await ctx.send("Hi, I'm Black Cat :)")

# Runs the bot.
bot.run(TOKEN)