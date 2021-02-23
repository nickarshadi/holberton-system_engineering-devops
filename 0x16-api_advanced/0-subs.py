#!/usr/bin/python3
"""Contain the number_of_subscribers function."""

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get("http://www.reddit.com/r/{}/about.json".format(subreddit),
                     headers={'User-Agent': 'Python/requests:\
APIproject:'}).json()
    subscribers = r.get("data", {}).get("subscribers", 0)
    return subscribers
