#!/usr/bin/python3

"""
A script that:
- takes your GitHub credentials (username and password)
- uses the GitHub API to display your id
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


def get_github_user_id(username, password):
    """
    Fetches the user id from the GitHub API using Basic Authentication.

    Args:
        username (str): The GitHub username.
        password (str): The GitHub password (personal access token).

    Returns:
        int or None: The user id or None if authentication fails.
    """
    auth = HTTPBasicAuth(username, password)
    response = requests.get("https://api.github.com/user", auth=auth)

    return response.json().get("id")


if __name__ == "__main__":
    # Parse command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Call the function with the provided credentials
    user_id = get_github_user_id(username, password)
    print(user_id)
