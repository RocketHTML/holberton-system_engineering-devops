#!/usr/bin/python3
"""
    Function that returns the subscribers of a given subredit
"""
import json
import requests


def number_of_subscribers(subreddit):

    """
        Returns subscribers of given subreddit
    """

    headers = {'Content-Type': 'application/json',
               'User-Agent': 'Ruby'}

    url = requests.get('https://api.reddit.com/r/{}/about'.format(subreddit),
                       headers=headers)

    if url.status_code != 200:
        return 0

    reddit_data = url.json().get('data')
    subs = reddit_data.get('subscribers')
    return (subs)
