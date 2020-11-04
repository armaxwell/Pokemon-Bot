import discord
from discord.ext import commands
import sqlite3
import random

client = commands.Bot(command_prefix = ".")

# Message to know that the bot is ready
@client.event
async def on_ready():
    print('Bot is ready!')

# Wild encounter
@client.command()
async def wild(ctx):
    # Connect to the Pokemon database
    conn = sqlite3.connect('Pokemon.db')
    c = conn.cursor()
    c.execute('''SELECT ID, NAME
    FROM INFO''')
    res = c.fetchall()                         # Returns a list of tuples i.e. data[list_num][tuple_num]
    
    # Chooses a random index between 0 to 150 for entries 1 to 151
    idx = random.randint(0, 151)
    name = res[idx][1]
    print('No. ' + str(res[idx][0]) + ':')     # Prints the entry number
    if (res[idx][0] == (idx + 1)):
        print(res[idx][1])                     # Prints the name of the Pokemon associated with the entry number

        # Display embed
        embed = discord.Embed(
            title = 'A wild ' + name + ' has appeared!',
            description = 'Catch it!',
            color = 0xff0000
        )
        
        await ctx.send(embed = embed)


# Bot token
client.run('NzcwNTE2OTQyMjc1NzM5NjY5.X5et0g.eZ6uYEc2IVPJ88FE767gr9UnBSY')