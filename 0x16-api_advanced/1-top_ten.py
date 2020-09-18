#!/usr/bin/python3
""" get number of the subs in a subreddit """
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{:s}/hot.json'.format(subreddit)
    usr_agnt = {'user-agent': 'test/charlie/0.1'}
    resp = requests.get(url,
                        allow_redirects=False,
                        headers=usr_agnt,
                        params={'limit': 10})
    if resp.status_code == 200:
        for x in range(10):
            print(resp.json()['data']['children'][x]['data']['title'])
    else:
        print(None)


if __name__ == '__main__':
    top_ten()
