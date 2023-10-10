#!/usr/bin/python3

"""
This module contains a function that queries the Reddit API and returns the
number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and returns the number of
    subscribers for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent header as per Reddit's API guidelines
    headers = {"User-Agent": "MyRedditBot/1.0"}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Check if the 'data' dictionary contains 'subscribers' information
        if "data" in data and "subscribers" in data["data"]:
            # Return the number of subscribers
            return data["data"]["subscribers"]
        else:
            # If the required data is not present, return 0
            return 0
    else:
        # If the subreddit is invalid or an issue with request, return 0
        return 0
