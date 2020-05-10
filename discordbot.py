from discord.ext import commands
import os
import traceback
import time
import requests

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
    user_search_url = 'https://www.speedrun.com/api/v1/users?name=' + arg
    user_search_data = requests.get(user_search_url).json()
    for user in user_search_data.get('data'):
        user_id = user.get('id')

    url = 'https://www.speedrun.com/api/v1/users/' + user_id + '/personal-bests'
    user_data = requests.get(url)

    send_list = []
    for data in user_data.json().get('data'):
        if data.get('run').get('game') == "nd22xvd0" or data.get('run').get('game') == "w6jmye6j":
            for links in data.get('run').get('links'):
                if links.get('rel') == 'category':
                    category_url = links.get('uri')
                    category_data = requests.get(category_url)
                    category_name = category_data.json().get('data').get('name')
                    send_list.append('category : ' + category_data.json().get('data').get('name'))
            send_list.append('place : ' + str(data.get('place')))
    
    send_str = '\n'.join(send_list)
    await ctx.send(send_str)

bot.run(token)
