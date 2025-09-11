#!/usr/bin/python3
"""This module gathers data from an API"""
import csv
import json
import requests
import sys


def get_user_todo_list():
    """Export user TODO list to CSV format"""
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
    
    path = "{}.csv".format(employee_id)

    try:
        with open(path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
            for todo in todo_list:
                writer.writerow([employee_id, user.get('username'),
                                todo.get('completed'), todo.get('title')])
    except IOError as e:
        print("Error writing CSV file: {}".format(e))
        sys.exit(1)


if __name__ == '__main__':
    get_user_todo_list()
