#!/usr/bin/python3
"""
Function which recursively requests from reddit
"""
from requests import get


def recurse(subreddit, hot_list=[], after=""):
    """
      Recursively scan reddit page
    """
    reddit = get('https://api.reddit.com/r/{}/hot?after={}'.format(
                                                                   subreddit,
                                                                   after),
                 headers={'User-Agent': 'Rupee'},
                 allow_redirects=False)

    if reddit.status_code != 200:
        return(None)

    for child in reddit.json().get('data').get('children'):
        hot_list.append(child.get('data').get('title'))

    after = reddit.json().get('data').get('after')

    if after:
        return recurse(subreddit, hot_list, after)

    return (hot_list)
