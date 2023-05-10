#!/usr/bin/python3
"""
Recursive function to count occurrences of given keywords in titles of all hot articles
of a given subreddit using Reddit API.
"""
import requests


def count_words(subreddit, word_list, instances=None, after=None):
    """
    Prints sorted count of given keywords in titles of all hot articles of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (dict): The dictionary of keyword counts. Defaults to None.
        after (str): The parameter for the next page of the API results. Defaults to None.
    """
    if instances is None:
        instances = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    try:
        data = response.json()["data"]
    except ValueError:
        return

    after = data["after"]
    children = data["children"]

    for child in children:
        title = child["data"]["title"].lower().split()

        for word in word_list:
            if word.lower() in title:
                if word not in instances:
                    instances[word] = 0

                instances[word] += title.count(word.lower())

    if after is not None:
        count_words(subreddit, word_list, instances, after)

    else:
        sorted_instances = sorted(instances.items(), key=lambda x: (-x[1], x[0]))

        for word, count in sorted_instances:
            print(f"{word}: {count}")
