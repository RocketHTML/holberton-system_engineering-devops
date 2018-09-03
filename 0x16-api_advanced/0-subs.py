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
                       headers=headers, allow_redirects=False)

    if url.status_code != 200:
        return 0

    data = url.json().get('data')
    subs = data.get('subscribers')
    return (subs)


if __name__ == "__main__":
    print(number_of_subscribers("programming"))
