#!/usr/bin/python3
"""
Queries the reddit API and prints the titles of the first 10 hot posts listed for a given subreddit. 
"""
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
