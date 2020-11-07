import discord
from discord.ext import commands
import sqlite3
import asyncio
import random
import embed

async def wild_db(ctx):
    # Chooses a random index between 1 to 151
    numID = random.randint(1, 152)

    # Connect to the Pokemon database
    conn = sqlite3.connect('Pokemon.db')
    c = conn.cursor()
    c.execute('''SELECT ID, NAME, IMAGES
    FROM INFO
    WHERE ID = ?''', (numID,))
    res = c.fetchone()                      # Returns a tuple
    c.close()

    # Create the embed for the randomly generator Pokemon
    name = res[1]
    image = res[2]
    print('No. ' + str(res[0]) + ':')       # Prints the entry number in terminal
    if (res[0] == numID):
        await embed.wild_embed(ctx, image)
        return name

async def dex_db(name):
    # Connect to the Pokemon database
    conn = sqlite3.connect('Pokemon.db')
    c = conn.cursor()
    c.execute('''SELECT *
    FROM INFO
    WHERE NAME = ?''', (name.title(),))
    res = c.fetchone()
    c.close()
    return res
