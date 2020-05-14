from discord.ext import commands
import subFunction
import os
import traceback
import time
import requests
import datetime

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
    send_list = []
    user_search_url = 'https://www.speedrun.com/api/v1/users?name=' + arg
    user_search_data = requests.get(user_search_url).json()
    for user in user_search_data.get('data'):
        if user.get('names').get('international') == arg:
            user_id = user.get('id')
            send_list.append('user name : ' + user.get('names').get('international'))

    user_url = 'https://www.speedrun.com/api/v1/users/' + user_id + '/personal-bests'
    user_data = requests.get(user_url)

    for data in user_data.json().get('data'):
        if data.get('run').get('game') == "nd22xvd0" or data.get('run').get('game') == "w6jmye6j":
            run_time = subFunction.get_time(datetime.timedelta(seconds=data.get('run').get('times').get('primary_t')))
            run_values = data.get('run').get('values')
            for links in data.get('run').get('links'):
                if links.get('rel') == 'category':
                    category_url = links.get('uri')
                    category_data = requests.get(category_url)
                    category_name = category_data.json().get('data').get('name')
                    if len(run_values) != 0: 
                        for category_links in category_data.json().get('data').get('links'):
                            if category_links.get('rel') == 'variables':
                                variables_url = category_links.get('uri')
                                variables_data = requests.get(variables_url)
                                variables_choices = variables_data.json().get('data')[0].get('values').get('choices')
                                for variables_keys in variables_choices.keys():
                                    for run_value in run_values.values():
                                        if run_value == variables_keys:
                                            variables_name = variables_choices.get(variables_keys)
                                            send_list.append('category : ' + category_name + '(' + variables_name + ')')
                    else:
                        send_list.append('category : ' + category_name)
            place = subFunction.get_place(data.get('place'))
            send_list.append('place : ' + place + ' (' + run_time + ')')
    
    send_str = '\n'.join(send_list)
    await ctx.send(send_str)

bot.run(token)
