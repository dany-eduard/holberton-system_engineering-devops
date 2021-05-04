#!/usr/bin/python3
""" Export to JSON. """
import json
import requests
from sys import argv


if __name__ == '__main__':
    """Prevent execution of this code when imported"""
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    user_dict = {user_id: []}

    user_name = requests.get(url + 'users/{}'.format(user_id)).json()
    user_tasks = requests.get(url + 'users/{}/todos'.format(user_id)).json()

    for task in user_tasks:
        user_dict[user_id].append({'task': task['title'],
                                   'completed': task['completed'],
                                   'username': user_name['username']})

    with open('{}.json'.format(user_id), 'w') as json_f:
        json_f.write(json.dumps(user_dict))
