#!/usr/bin/python3
"""Gather data from an API."""


import requests
import sys


base_url = 'https://jsonplaceholder.typicode.com/'


def do_request():
    """Perform request."""
    if len(sys.argv) < 2:
        return print("USAGE: {} <empleyee id>".format(__file__))
    user_id = sys.argv[1]
    try:
        _user_id = int(sys.argv[1])
    except ValueError:
        return print("Employee id must be an integer.")
    response = requests.get(base_url + 'users/' + user_id)
    if response.status_code == 404:
        return print("User id not found.")
    elif response.status_code != 200:
        return print("Error: status_code: {}".format(response.status_code))
    user = response.json()

    response = requests.get(base_url + 'todos/')
    if response.status_code != 200:
        return print("Error: status_code: {}".format(response.status_code))
    todos = response.json()

    user_todos = []
    for todo in todos:
        if todo.get("userId") == user.get('id'):
            user_todos.append(todo)
    completed = []
    for todo in user_todos:
        if todo.get('completed'):
            completed.append(todo)
    print("Employee {} is done with tasks({}/{}):".format(user.get('name'),
          len(completed), len(user_todos)))
    for task in completed:
        print('\t {}'.format(task.get('title')))


if __name__ == "__main__":
    do_request()
