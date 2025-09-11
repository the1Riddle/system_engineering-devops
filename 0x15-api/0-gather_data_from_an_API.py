#!/usr/bin/python3
"""
For a given employee ID, returns information about
their TODO list progress
"""

import json
import requests
import sys


def get_user_todo_list():
    """Fetch and display user TODO list progress"""
    if len(sys.argv) != 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be a valid integer")
        sys.exit(1)
    
    url1 = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    url2 = '{}/todos'.format(url1)
    
    try:
        todo_response = requests.get(url2, timeout=10)
        todo_response.raise_for_status()
        todo_list = todo_response.json()
        
        user_response = requests.get(url1, timeout=10)
        user_response.raise_for_status()
        user = user_response.json()
        
    except requests.exceptions.RequestException as e:
        print("Error fetching data: {}".format(e))
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: Invalid JSON response")
        sys.exit(1)
    
    completed_todo = []
    for todo in todo_list:
        if todo.get('completed') is True:
            completed_todo.append(todo.get('title'))

    print("Employee {} is done with tasks({}/{}): "
          .format(user.get('name'), len(completed_todo), len(todo_list)))
    for todo in completed_todo:
        print("\t {}".format(todo))

if __name__ == '__main__':
    get_user_todo_list()
