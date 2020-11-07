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
    data = await database.wild_db()
    pkmnName = await database.randPkmn(ctx, data)
    print(pkmnName + ' is the answer.')

@client.command()
async def catch(ctx, arg):
    global pkmnName
    if (pkmnName. title() == arg.title()):
        await ctx.send('Congratulations! You caught a {}!'.format(pkmnName))
        print('Caught')
        pkmnName = ''

@client.command()
async def pokedex(ctx, arg):
    data = await database.dex_db(arg)
    await embed.dex_embed(ctx, data)
    

# Bot token
client.run('token')
