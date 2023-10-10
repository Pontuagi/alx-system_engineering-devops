#!/usr/bin/python3

"""
a recursive function that queries the Reddit API
"""

import requests


def count_words(subreddit, word_list):
    # Base case: if the subreddit is not valid, return
    if not is_valid_subreddit(subreddit):
        return

    # Define the Reddit API URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

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
            # Create a dictionary to store word counts
            word_counts = {}

            # Iterate through the posts and parse their titles
            for post in data["data"]["children"]:
                title = post["data"]["title"]

                # Split the title into words and convert to lowercase
                words = [word.lower() for word in title.split()]

                # Iterate through the word list
                for keyword in word_list:
                    keyword = keyword.lower()

                    # Check if the keyword appears in the title's words
                    if keyword in words:
                        # Increment the keyword's count in the dictionary
                        word_counts[keyword] = (
                            word_counts.get(keyword, 0) + words.count(keyword))

            # Sort the word counts by count (descending)
            # and then alphabetically (ascending)
            sorted_counts = sorted(
                word_counts.items(), key=lambda x: (-x[1], x[0]))

            # Print the sorted counts
            for keyword, count in sorted_counts:
                print(f"{keyword}: {count}")

            # Check if there are more pages (next page 'after' parameter)
            if "after" in data["data"] and data["data"]["after"]:
                # Recursively call the function to fetch the next page
                count_words(subreddit, word_list)
        else:
            # If the required data is not present, return
            return
    else:
        # If there was an issue with the request, return
        return


def is_valid_subreddit(subreddit):
    # Define a function to check if a subreddit exists by querying its data
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditBot/1.0"}

    response = requests.get(url, headers=headers)

    return response.status_code == 200
