#!/usr/bin/python3
"""Contains recurse function"""
from requests import get

REDDIT = "https://www.reddit.com/"
HEADERS = {'user-agent': 'my-app/0.0.1'}


def recurse(subreddit, hot_list=None, after="", count=0):
    """
    Returns a list of titles of all hot posts on a given subreddit
    """
    if hot_list is None:
        hot_list = []
        
    if after is None:
        return hot_list

    url = REDDIT + "r/{}/hot/.json".format(subreddit)

    params = {
        'limit': 100,
        'after': after
    }

    try:
        r = get(url, headers=HEADERS, params=params, 
                allow_redirects=False, timeout=10)

        if r.status_code != 200:
            return None

        js = r.json()
        data = js.get("data")
        after = data.get("after")
        children = data.get("children")
        
        for child in children:
            post = child.get("data")
            hot_list.append(post.get("title"))

        return recurse(subreddit, hot_list, after)
        
    except (ValueError, KeyError, TypeError, Exception):
        return None
