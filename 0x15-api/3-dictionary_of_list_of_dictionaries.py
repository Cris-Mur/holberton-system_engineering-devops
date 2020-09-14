#!/usr/bin/python3
""" request to use API """
if __name__ == "__main__":
    import sys
    import requests
    import json

    all_Users = requests.get('https://jsonplaceholder.typicode.com/users')
    all_TODO = requests.get('https://jsonplaceholder.typicode.com/todos')

    User_tbl = {}
    tasks_ = {}
    listoe = []
    for usr in all_Users.json():
        User_tbl[usr.get('id')] = []
        name = usr.get('username')
        for i in all_TODO.json():
            if i.get('userId') == usr.get('id'):
                tasks_['username'] = name
                tasks_['task'] = i.get("title")
                tasks_['completed'] = i.get("completed")
                listoe.append(tasks_.copy())
                task_ = {}
        User_tbl[usr.get('id')] = listoe
        listoe = []

    with open("todo_all_employees.json", 'w', newline='') as son:
        json.dump(User_tbl, son)
