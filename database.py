import discord
from discord.ext import commands
import sqlite3
import asyncio
import database
import embed

client = commands.Bot(command_prefix = '.')

pkmnName = ''

# Message to know that the bot is ready
@client.event
async def on_ready():
    print('Bot is ready!')

# Wild encounter
@client.command()
async def wild(ctx):
    global pkmnName
    pkmnName = await database.wild_db(ctx)      # Name is returned and stored in the global variable
    print(pkmnName + ' is the answer.')

# Catching mechanic
@client.command()
async def catch(ctx, arg):
    global pkmnName

    # Check is the input matches the Pokemon name
    if (pkmnName. title() == arg.title()):
        await ctx.send('Congratulations! You caught a {}!'.format(pkmnName))
        print('Caught')
        pkmnName = ''                           # Reset the global variable

# Pokedex command
@client.command()
async def pokedex(ctx, arg):
    data = await database.dex_db(arg)
    print(data)
    await embed.dex_embed(ctx, data)
    

# Bot token
client.run('token')
