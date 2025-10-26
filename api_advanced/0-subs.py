#!/usr/bin/python3
"""
0-subs module

This module provides a function to query the Reddit API and return
the number of subscribers for a given subreddit.

Function:
    number_of_subscribers(subreddit)

Usage:
    >>> from 0-subs import number_of_subscribers
    >>> number_of_subscribers('python')
    1001234

Notes:
- The function returns 0 if the subreddit is invalid or does not exist.
- No authentication is required to access this endpoint.
- The Reddit API requires a custom User-Agent header to avoid request rejection.
- Invalid subreddits may redirect to a search results page; this function disables redirects.
"""
import requests

def number_of subscribers(subreddit):
 """Return the number of subscribers for a subreddit or 0 if invalid."""
    # URL for subreddit info (do not follow redirects)
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Python:subreddit.sub.count:v1.0 (by /u/yourusername)'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except Exception:
        return 0
