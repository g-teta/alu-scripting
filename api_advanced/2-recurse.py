#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list containing the titles of hot articlesfor a given subreddit.
"""
import requests 

def recurse(subreddit, hot_list=None, after=None):
    """Recursively retrieves all hot post titles for a given subreddit."""
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Python:recursion:v1.0 (by /u/yourusername)'}
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )

        if response.status_code != 200:
            return None

        data = response.json().get('data', {})
        children = data.get('children', [])
        for post in children:
            hot_list.append(post.get('data', {}).get('title'))

        # Get the next page token
        after = data.get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list

    except Exception:
        return None
