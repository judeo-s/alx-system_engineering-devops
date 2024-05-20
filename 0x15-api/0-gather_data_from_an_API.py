#!/usr/bin/python3

"""
A python script that uses sends requests/response to-and-fro REST APIs
"""

import json
import requests
import sys

if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users/{}"
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    completed = 0
    total = 0

    if sys.argv[1].isdigit():
        ID = int(sys.argv[1])
        content = requests.get(user_url.format(sys.argv[1]))
        users = json.loads(content.text)
        name = users['name']
        content = requests.get(todo_url)
        todo_list = json.loads(content.text)

        for item in todo_list:
            if item['userId'] == ID:
                total += 1
                if item['completed'] is True:
                    completed += 1
        print(f'Employee {name} is done with tasks({completed}/{total}):')

        for item in todo_list:
            if item['userId'] == ID and item['completed'] == True:
                print(f'\t{item["title"]}')
    else:
        pass

