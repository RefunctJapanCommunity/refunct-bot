import requests
import datetime

def get_ranking(user_name):
    send_list = []
    send_list.append('user name : ' + user_name)
    user_data = get_user(user_name)

    for data in user_data.json().get('data'):
        if data.get('run').get('game') == "nd22xvd0" or data.get('run').get('game') == "w6jmye6j":
            run_time = get_time(datetime.timedelta(seconds=data.get('run').get('times').get('primary_t')))
            run_values = data.get('run').get('values')
            place = get_place(data.get('place'))
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
        send_list.append(category_name.ljust(20) + '  ' + place + ' (' + run_time + ')')
    return send_list

def get_user(user_name):
    user_search_url = 'https://www.speedrun.com/api/v1/users?name=' + user_name
    user_search_data = requests.get(user_search_url).json()
    for user in user_search_data.get('data'):
        if user.get('names').get('international') == user_name:
            user_id = user.get('id')

    user_url = 'https://www.speedrun.com/api/v1/users/' + user_id + '/personal-bests'
    return requests.get(user_url)

def get_time(time):
    m, s = divmod(time.seconds, 60)
    h, m = divmod(m, 60)
    hour = str(h)
    mins = str(m)
    sec = str(s)
    ms = str(time.microseconds)[:2]
    if h != 0:
        if time.microseconds != 0:
            return hour + 'h ' + mins.zfill(2) + 'm ' + sec.zfill(2) + 's ' + ms.zfill(2) + '0ms'
        else:
            return hour + 'h ' + mins.zfill(2) + 'm ' + sec.zfill(2) + 's'
    else:
        if time.microseconds != 0:
            return mins + 'm ' + sec.zfill(2) + 's ' + ms.zfill(2) + '0ms'
        else:
            return mins + 'm ' + sec.zfill(2) + 's '

def get_place(place):
    place = str(place)
    if place[-1] == '1':
        return place + 'st'
    elif place[-1] == '2':
        return place + 'nd'
    elif place[-1] == '3':
        return place + 'rd'
    else:
        return place + 'th'