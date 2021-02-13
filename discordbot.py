import os
import asyncio
from discord.ext import commands
from script import common
from script import refunct
from script import technique

bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.command()
async def c(ctx):
    await ctx.send('The race will begin in 10 seconds!')
    await asyncio.sleep(5)
    await ctx.send('The race will begin in 5 seconds!')
    await asyncio.sleep(2)
    await ctx.send("3")
    await asyncio.sleep(1)
    await ctx.send("2")
    await asyncio.sleep(1)
    await ctx.send("1")
    await asyncio.sleep(1)
    await ctx.send("Go!")

@bot.command()
async def ranking(ctx, arg):
    send_list = refunct.get_ranking(arg)
    send_str = '\n'.join(send_list)
    await ctx.send(send_str)

@bot.command()
async def tech(ctx, arg):
    send_list = technique.get_tech(arg)
    send_str = '\n'.join(send_list)
    await ctx.send(send_str)

bot.run(token)
