#!/usr/bin/python3
""" request to use API """
if __name__ == "__main__":
    import sys
    import requests
    import csv

    Uid = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(Uid)
    req = requests.get(url)
    if req.status_code != 404:
        url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            Uid)
        all_TODO = requests.get(url)
        name = req.json()['username']

        with open("{}.csv".format(Uid), 'w') as comma:
            csv_writer = csv.writer(comma,
                                    delimiter=',',
                                    quotechar='"',
                                    quoting=csv.QUOTE_ALL)
            for i in all_TODO.json():
                status = str(i.get('completed'))
                title = str(i.get('title'))
                csv_writer.writerow([Uid, name, status, title])
