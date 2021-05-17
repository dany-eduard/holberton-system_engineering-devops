#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ 10 hot posts. """
    res = requests.get("https://reddit.com/r/{}/hot.json".format(subreddit),
                       headers={"User-Agent": "Custom"}, params={"limit": 10})

    if (res.status_code == 200):
        for i in res.json().get("data").get("children"):
            print("{}".format(i.get("data").get("title")))
    else:
        print(None)
