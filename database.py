import discord
from discord.ext import commands
import sqlite3
import asyncio
import random
import embed

async def wild_db():
    # Connect to the Pokemon database
    conn = sqlite3.connect('Pokemon.db')
    c = conn.cursor()
    c.execute('''SELECT ID, NAME, IMAGES
    FROM INFO''')
    res = c.fetchall()                         # Returns a list of tuples i.e. data[list_num][tuple_num]
    c.close()
    return res                                 # Tuple data output

async def randPkmn(ctx, data):
    # Chooses a random index between 0 to 150 for entries 1 to 151
    idx = random.randint(0, 151)
    name = data[idx][1]
    image = data [idx][2]                       # Retrieves the name of the image file
    print('No. ' + str(data[idx][0]) + ':')     # Prints the entry number
    if (data[idx][0] == (idx + 1)):
        await embed.wild_embed(ctx, image)
        return name

async def dex_db(name):
    # Connect to the Pokemon database
    conn = sqlite3.connect('Pokemon.db')
    c = conn.cursor()
    c.execute('''SELECT ID, NAME, HEIGHT, WEIGHT, IMAGES
    FROM INFO
    WHERE NAME = ?''', (name.title(),))
    res = c.fetchone()
    c.close()
    return res
