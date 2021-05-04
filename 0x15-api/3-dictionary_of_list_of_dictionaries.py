#!/usr/bin/python3
""" Dictionary of list of dictionaries. """
import json
import requests
from sys import argv


if __name__ == '__main__':
    """Prevent execution of this code when imported"""
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + 'users/').json()
    user_dict = {}

    for user in users:
        user_id = user['id']
        user_dict[user_id] = []
        user_tasks = requests.get(url + 'users/{}/todos'.format(
            user_id)).json()

        for task in user_tasks:
            user_dict[user_id].append({'username': user['username'],
                                       'task': task['title'],
                                       'completed': task['completed']})

    with open('todo_all_employees.json', 'w') as json_f:
        json_f.write(json.dumps(user_dict))
