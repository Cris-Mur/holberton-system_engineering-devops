#!/usr/bin/python3
""" request to use API """
if __name__ == "__main__":
    import requests
    import sys

    Uid = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(Uid)
    req = requests.get(url)
    if req.status_code != 404:
        url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            Uid)
        all_TODO = requests.get(url)
        url = 'https://jsonplaceholder.typicode.com/todos\
?userId={}&completed=true'.format(Uid)
        done_TODO = requests.get(url)
        name = req.json()['name']
        print("Employee {} is done with tasks({}/{}):".format(
            name, len(done_TODO.json()), len(all_TODO.json())))
        for i in done_TODO.json():
            print("\t {}".format(i['title']))
