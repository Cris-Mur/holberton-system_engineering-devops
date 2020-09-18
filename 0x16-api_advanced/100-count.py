#!/usr/bin/python3
""" Write a recursive function that queries API, parses the titles """
import operator
import requests


def count_words(subreddit, word_list, hot_list=[], after='', values={}):
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                   after)
    usr_agnt = {'user-agent': 'test/charlie/0.1'}
    if len(hot_list) == 0:
        for i in range(0, len(word_list)):
            values[word_list[i]] = 0
    try:
        resp = requests.get(url,
                            allow_redirects=False,
                            headers=usr_agnt).json()

        son = resp.get('data').get('children')
        after = resp.get('data').get('after')
        coso = values
        for boy in son:
            res = boy.get('data').get('title')
            for i in range(0, len(word_list)):
                if word_list[i].lower() in res.lower():
                    coso[word_list[i]] += 1
            hot_list.append(res)
        values = coso
        if after is None:
            sort_val = sorted(values.items(), key=operator.itemgetter(1))
            for x in range(len(sort_val), 0, -1):
                if sort_val[x - 1][1] > 0:
                    print("{}: {}".format(sort_val[x - 1][0],
                                          sort_val[x - 1][1]))
            return hot_list
        return count_words(subreddit, word_list, hot_list, after, values)
    except:
        return None
