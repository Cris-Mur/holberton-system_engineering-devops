#!/usr/bin/python3
""" get number of the subs in a subreddit """
import requests


def recurse(subreddit, hot_list=[], after=""):
    url = 'https://www.reddit.com/r/{:s}/hot.json?after={}'.format(subreddit,
                                                                   after)
    usr_agnt = {'user-agent': 'test/charlie/0.1'}
    resp = requests.get(url,
                        allow_redirects=False,
                        headers=usr_agnt).json()
    try:
        for x in resp.get('data').get('children'):
            hot_list.append(x.get('data').get('title'))
    except:
        return None

    nxt_p = resp.get('data').get('after')
    if nxt_p is None:
        return hot_list
    return recurse(subreddit, hot_list, nxt_p)
