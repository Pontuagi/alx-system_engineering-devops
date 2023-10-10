#!/usr/bin/python3

"""
This module contains  a recursive function that queries the Reddit API
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    A recursive function that queries the Reddit API and
    returns a list containing the titles of all hot articles
    for a given subreddit.
    If no results are found for the given subreddit,
    the function returns None.
    """
    if not is_valid_subreddit(subreddit):
        return None

    # Define the Reddit API URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

    # If there is a 'after' parameter, add it to the URL to fetch the next page
    if after:
        url += f'&after={after}'

    # Set a custom User-Agent header as per Reddit's API guidelines
    headers = {"User-Agent": "MyRedditBot/1.0"}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Check if the 'data' dictionary contains 'children' (list of posts)
        if "data" in data and "children" in data["data"]:
            # Iterate through the posts and add their titles to the hot_list
            for post in data["data"]["children"]:
                hot_list.append(post["data"]["title"])

            # Check if there are more pages (next page 'after' parameter)
            if "after" in data["data"] and data["data"]["after"]:
                # Recursively call the function to fetch the next page
                return recurse(
                    subreddit, hot_list, after=data["data"]["after"])
            else:
                # No more pages, return the hot_list
                return hot_list
        else:
            # If the required data is not present, return None
            return None
    else:
        # If there was an issue with the request, return None
        return None


def is_valid_subreddit(subreddit):
    # Define a function to check if a subreddit exists by querying its data
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditBot/1.0"}

    response = requests.get(url, headers=headers)

    return response.status_code == 200
