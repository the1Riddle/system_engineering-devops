#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """Function that fetches top 10 posts"""
    if not subreddit or not isinstance(subreddit, str):
        print('None')
        return
    
    apiUrl = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    userAgent = "Mozilla/5.0"
    limits = 10

    try:
        response = requests.get(
            apiUrl, headers={"user-agent": userAgent}, 
            params={"limit": limits}, timeout=10)
        
        if response.status_code != 200:
            print('None')
            return
            
        response_data = response.json()
        list_obj = response_data['data']['children']
        for obj in list_obj:
            print(obj['data']['title'])
            
    except (requests.exceptions.RequestException, 
            KeyError, ValueError, TypeError):
        print('None')
