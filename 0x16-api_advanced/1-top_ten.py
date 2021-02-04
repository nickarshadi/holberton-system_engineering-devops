#!/usr/bin/python3
"""Contain the top ten function."""

import requests


def top_ten(subreddit):
    """Print the top ten titles."""
    if subreddit is None or type(subreddit) is not str:
        print(None)
    else:
        r = requests.get("http://reddit.com/r/{}/hot.json".format(subreddit),
                         headers={"User-Agent": 'Python/requests:APIproject'},
                         params={'limit': 10}).json()
    posts = r.get("data", {}).get("children", None)
    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        print(None)
    else:
        for post in posts:
            print(post.get('data', {}).get("title", None))
