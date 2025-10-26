#!/usr/bin/python3
"""
This module provides a function to print the titles of the first
10 hot posts of a given subreddit.

Function:
    top_ten(subreddit)

Usage:
    >>> from 1-top_ten import top_ten
    >>> top_ten('python')
    Title1
    Title2
    ...

Notes:
- Prints 'None' if subreddit is invalid.
- Uses Reddit API's hot endpoint with limit=10.
- Redirects are disabled to detect invalid subreddits.
This module provides a function to print the titles of the first
10 hot posts of a given subreddit.

Function:
    top_ten(subreddit)

Usage:
    >>> from 1-top_ten import top_ten
    >>> top_ten('python')
    Title1
    Title2
    ...

Notes:
- Prints 'None' if subreddit is invalid.
- Uses Reddit API's hot endpoint with limit=10.
- Redirects are disabled to detect invalid subreddits."""
import requests 

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Python:top.ten:v1.0 (by /u/yourusername)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            posts = response.json().get('data', {}).get('children', [])
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
    except Exception:
        print(None)
