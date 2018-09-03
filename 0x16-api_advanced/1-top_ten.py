#!/usr/bin/python3
"""
    This function returns top ten posts
"""
import json
import requests


def top_ten(subreddit):
    """
        Return top ten posts
    """
    headers = {'Content-Type': 'application/json',
               'User-agent': 'Ruby'}

    url = requests.get('https://api.reddit.com/r/{}/hot'.format(subreddit),
                       headers=headers).json()

    if url.status_code == 200:
        for title in range(10):
            print(url['data']['children'][title]['data']['title'])
    else:
        print(None)
