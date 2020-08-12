from discord.ext import commands
import speedrun
import refunct
import technique
import os
import traceback
import time

bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def c(ctx):
    await ctx.send('The race will begin in 10 seconds!')
    time.sleep(5)
    await ctx.send('The race will begin in 5 seconds!')
    time.sleep(2)
    await ctx.send("3")
    time.sleep(1)
    await ctx.send("2")
    time.sleep(1)
    await ctx.send("1")
    time.sleep(1)
    await ctx.send("Go!")

@bot.command()
async def ranking(ctx, arg):
    if "Refunct" in str(ctx.guild):
        send_list = refunct.get_ranking(arg)
        send_str = '\n'.join(send_list)
        await ctx.send(send_str)
    elif "記録" in str(ctx.channel) or "きろく" in str(ctx.channel) or "record" in str(ctx.channel):
        user, user_id = speedrun.get_user(arg)
        send_str = '\n'.join(user)
        await ctx.send(send_str)
        if user_id == '':
            return
        user_data = speedrun.get_user_data(user_id)
        send_list = []
        game_id = ''
        count = 0
        for data in user_data:
            previous_id = game_id
            game_id = data.get('run').get('game')
            if previous_id != game_id:
                if not count == 0:
                    send_str = '\n'.join(send_list)
                    await ctx.send(send_str)
                    send_list.clear()
                count = count + 1
                send_list.append('\n' + speedrun.get_title(game_id))
            records = speedrun.get_records(data)
            if not records == '':
                send_list.append(records)
        if len(send_list) == 1:
            send_list.append('\n' + 'records is not found')
        send_str = '\n'.join(send_list)
        await ctx.send(send_str)
        send_str = '\n'.join(user)
        await ctx.send(f'{send_str} record is End')

@bot.command()
async def tech(ctx, arg):
    if "雑談" in str(ctx.channel):
        if "Refunct" in str(ctx.guild):
            send_list = technique.get_tech(arg)
            send_str = '\n'.join(send_list)
            await ctx.send(send_str)

@bot.command()
async def test(ctx):
    if "ぐにぴったん" in str(ctx.guild):
        await ctx.send(ctx.guild)

bot.run(token)
