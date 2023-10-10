#!/usr/bin/python3

"""
a recursive function that queries the Reddit API
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Base case: if the subreddit is not valid, or no more posts to fetch, or
    word_list is empty, return None
    """
    if not is_valid_subreddit(subreddit) or not word_list:
        return None

    # Initialize counts if it's None
    if counts is None:
        counts = {}

    # Define the Reddit API URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

    # If there is an 'after' parameter, add it to URL to fetch the next page
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
            # Iterate through the posts and parse their titles
            for post in data["data"]["children"]:
                title = post["data"]["title"].lower()

                # Count word occurrences in the title
                for word in word_list:
                    if word in counts:
                        counts[word] += title.count(word)
                    else:
                        counts[word] = title.count(word)

            # Check if there are more pages (next page 'after' parameter)
            if "after" in data["data"] and data["data"]["after"]:
                # Recursively call the function to fetch the next page
                return count_words(
                    subreddit, word_list, after=data["data"]["after"],
                    counts=counts
                    )
            else:
                # Sort and print the counts in descending order by count and
                # +ascending order by word
                sorted_counts = sorted(
                    counts.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
        else:
            # If the required data is not present, return None
            return None
    else:
        # If there was an issue with the request, return None
        return None


def is_valid_subreddit(subreddit):
    """
    A function to check if a subreddit exists by querying its data
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditBot/1.0"}

    response = requests.get(url, headers=headers)

    return response.status_code == 200
