#!/usr/bin/python3
""" Export to CSV. """
import csv
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]

    user_name = requests.get(url + 'users/{}'.format(user_id)).json()
    user_tasks = requests.get(url + 'users/{}/todos'.format(user_id)).json()

    for task in user_tasks:
        with open('{}.csv'.format(user_id), mode='w') as f:
            emp_w = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
            for task in user_tasks:
                emp_w.writerow([user_id, user_name['username'],
                                task['completed'], task['title']])
