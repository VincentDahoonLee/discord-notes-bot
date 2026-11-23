import discord
from discord import app_commands
from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')  
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))
GUILD_ID = int(os.getenv('GUILD_ID'))


intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True
intents.presences = True

bot = commands.Bot(command_prefix=':3 ', intents=intents)


channel = discord.Object(id=CHANNEL_ID)
guild = discord.Object(id=GUILD_ID)


@bot.event
async def on_ready():

    bot.tree.copy_global_to(guild=guild)

    await bot.tree.sync(guild=guild)
    print(f'We have logged in as {bot.user}!')

@bot.event
async def on_message(message):
    c = bot.get_channel(channel.__getattribute__("id"))
    if message.author == bot.user:
        return
    
    if message.guild == None:
        print("hi")
        await message.channel.send('Hello!')
        await c.send("Test")

    if message.guild == guild:
        print("mrrraow")
        await c.send("mrraow")

@bot.tree.command()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')

@bot.tree.command()
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(
    first_value='The first value you want to add something to',
    second_value='The value you want to add to the first value',
)
async def add(interaction: discord.Interaction, first_value: int, second_value: int):
    """Adds two numbers together."""
    await interaction.response.send_message(f'{first_value} + {second_value} = {first_value + second_value}')


bot.run(TOKEN)