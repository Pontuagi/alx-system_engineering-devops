#!/usr/bin/python3

"""
This module contains a function that queries the Reddit API
"""

import requests


def top_ten(subreddit):
    """
    a function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    If not a valid subreddit, print None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set a custom User-Agent header
    headers = {"User-Agent": "MyRedditBot/1.0"}

    # Send a Get request to the Reddit API
    response = requests.get(url, headers=headers)

    # Send a Get request to the Reddit API
    if response.status_code == 200:
        data = response.json()

        # Check if 'data' dictionary contains 'children'
        if "data" in data and "children" in data["data"]:
            for post in data["data"]["children"]:
                print(post["data"]["title"])
        else:
            print("None")

    else:
        print("None")
