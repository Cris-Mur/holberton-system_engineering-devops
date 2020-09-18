#!/usr/bin/python3
""" get number of the subs in a subreddit """
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{:s}/about.json'.format(subreddit)
    usr_agnt = {'user-agent': 'test/charlie/0.1'}
    resp = requests.get(url, headers=usr_agnt)
    if resp:
        return resp.json()['data']['subscribers']
    else:
        return 0


if __name__ == '__main__':
    number_of_subscribers()
