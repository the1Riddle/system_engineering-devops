#!/usr/bin/python3
"""Contains the count_words function"""
import requests


def count_words(subreddit, word_list, found_list=None, after=None):
    """
    Prints counts of given words found in hot posts of a given subreddit
    """
    if found_list is None:
        found_list = []
        
    user_agent = {'User-agent': 'test45'}
    
    try:
        posts = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'
                           .format(subreddit, after), 
                           headers=user_agent, timeout=10)
    except requests.exceptions.RequestException:
        return

    if after is None:
        word_list = [word.lower() for word in word_list]

    if posts.status_code == 200:
        try:
            posts_data = posts.json()['data']
            aft = posts_data['after']
            posts_children = posts_data['children']
            
            for post in posts_children:
                title = post['data']['title'].lower()
                for word in title.split(' '):
                    if word in word_list:
                        found_list.append(word)
                        
            if aft is not None:
                count_words(subreddit, word_list, found_list, aft)
            else:
                result = {}
                for word in found_list:
                    if word.lower() in result.keys():
                        result[word.lower()] += 1
                    else:
                        result[word.lower()] = 1
                for key, value in sorted(result.items(), key=lambda item: item[1],
                                       reverse=True):
                    print('{}: {}'.format(key, value))
                    
        except (KeyError, ValueError, TypeError):
            return
    else:
        return
