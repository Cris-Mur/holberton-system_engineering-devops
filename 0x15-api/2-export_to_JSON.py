#!/usr/bin/python3
""" request to use API """
if __name__ == "__main__":
    import sys
    import requests
    import json

    Uid = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(Uid)
    req = requests.get(url)
    if req.status_code != 404:
        url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            Uid)
        all_TODO = requests.get(url)
        name = req.json()['username']

        tasks_ = {}
        listoe = []
        for i in all_TODO.json():
            tasks_['task'] = i.get("title")
            tasks_['completed'] = i.get("completed")
            tasks_['username'] = name
            listoe.append(tasks_)
            tasks_ = {}

        tasks_[str(Uid)] = listoe

        with open("{}.json".format(Uid), 'w', newline='') as son:
            json.dump(tasks_, son)
