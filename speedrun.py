import requests
import datetime
import common

prefix_url = 'https://www.speedrun.com/api/v1'

def get_ranking(user_name):
    send_list = []
    send_list.append('user name : ' + user_name)
    user_data = get_user(user_name)
    user_data_s = sorted(user_data.json().get('data'), key=lambda x: x['run']['game'])

    game_id = ''
    for data in user_data_s:
        if data.get('run').get('game') == "nd22xvd0" or data.get('run').get('game') == "w6jmye6j":
            if game_id != data.get('run').get('game'):
                send_list.append('\n' + get_title(data.get('run').get('game')))
            game_id = data.get('run').get('game')
            send_list.append(get_status(data))
    return send_list

def get_user(user_name):
    user_search_url = prefix_url + '/users?name=' + user_name
    user_search_data = requests.get(user_search_url).json()
    for data in user_search_data.get('data'):
        if data.get('names').get('international') == user_name:
            user_id = data.get('id')

    user_url = prefix_url + '/users/' + user_id + '/personal-bests'
    return requests.get(user_url)

def get_title(game_id):
    game_url = prefix_url + '/games/' + game_id
    return requests.get(game_url).json().get('data').get('names').get('international')

def get_status(data):
    run_time = common.get_time(datetime.timedelta(seconds=data.get('run').get('times').get('primary_t')))
    run_values = data.get('run').get('values')
    place = common.get_place(data.get('place'))
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
                                    category_name = category_name + ' (' + variables_name + ')'
    return category_name.ljust(20) + '  ' + place + ' (' + run_time + ')'
