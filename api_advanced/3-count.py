#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the titles of
all hot articles, and prints a sorted count of given keywords.
"""
import requests
import re


def count_words(subreddit, word_list, after=None, counts=None):
    """Prints a sorted count of given keywords found in hot article titles."""
    if counts is None:
        # Normalize word list (case-insensitive) and handle duplicates
        counts = {}
        for word in word_list:
            w = word.lower()
            counts[w] = counts.get(w, 0) + 0  # Initialize with 0

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Python:count.words:v1.0 (by /u/yourusername)'}
    params = {'after': after, 'limit': 100}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get('data', {})
    children = data.get('children', [])

    # Parse titles
    for post in children:
        title = post.get('data', {}).get('title', '').lower()
        # Split words by non-alphanumeric characters
        words_in_title = re.findall(r'\b\w+\b', title)
        for word in counts.keys():
            counts[word] += words_in_title.count(word)

    # Recursive call if there is another page
    next_after = data.get('after')
    if next_after is not None:
        return count_words(subreddit, word_list, next_after, counts)

    # Once all pages are processed, print sorted results
    filtered = {k: v for k, v in counts.items() if v > 0}
    if not filtered:
        return

    # Sort by count (descending), then alphabetically
    sorted_counts = sorted(filtered.items(),
                           key=lambda item: (-item[1], item[0]))

    for word, count in sorted_counts:
        print(f"{word}: {count}")
