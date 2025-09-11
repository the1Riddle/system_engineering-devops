#!/usr/bin/python3
"""
Script that queries the Reddit API and returns the numbers of
subscribers of a subreddit passed to it
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that returns the numbers of
    subscribers of a subreddit passed to it
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0
    
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, 
                              allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return 0
        
        data = response.json()
        return data['data']['subscribers']
        
    except (requests.exceptions.RequestException, 
            KeyError, ValueError, TypeError):
        return 0
