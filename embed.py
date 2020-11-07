import discord
from discord.ext import commands
import asyncio

async def wild_embed(ctx, image):
    # Display embed
    embed = discord.Embed(
        title = 'A wild Pokemon has appeared!',
        description = 'Catch it!',
        color = 0xff0000
    )
    image = image + '.png'
    filename = discord.File('PKMNImages/' + image, filename=image)
    embed.set_image(url='attachment://' + image)
    embed.set_footer(text='Type ".catch <Pokemon>" to catch it!')
    await ctx.send(file=filename, embed=embed)
    return

async def dex_embed(ctx, info):
    # Display embed
    num = info[0]
    name = info[1]
    height = str(float(info[2]) / 10)
    weight = str(float(info[3]) / 10)

    embed = discord.Embed(
        title = 'No. {}: {}'.format(num, name),
        color = 0xff0000
    )

    embed.add_field(name = 'Height', value = height + ' m')
    embed.add_field(name = 'Weight', value = weight + ' kg')
    image = info[4] + '.png'
    filename = discord.File('PKMNImages/' + image, filename=image)
    embed.set_image(url='attachment://' + image)
    await ctx.send(file=filename, embed=embed)
