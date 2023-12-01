#!/usr/bin/python3

"""
A script that:
- fetches the most recent 10 commits (from the most recent to oldest)
- of the repository specified by the user
- from the owner specified by the user
- using the GitHub API
- and prints all commits in the format: <sha>: <author name> (one per line)
"""

import sys
import requests


def fetch_commits(owner, repo):
    """
    Fetches the 10 most recent commits from a GitHub repository.

    Args:
        owner (str): The owner (username or organization) of the repository.
        repo (str): The name of the repository.

    Returns:
        list: A list of commit information in the format "<sha>:
        <author name>".
    """
    try:
        # Define the GitHub API endpoint for commits
        api_url = f"https://api.github.com/repos/{owner}/{repo}/commits"

        # Send a GET request to the GitHub API
        response = requests.get(api_url)

        # Check if the request was successful
        if response.status_code == 200:
            commits_data = response.json()
            commits_list = []

            # Iterate through commits until 10 commits are processed
            for commit in commits_data:
                sha = commit["sha"]
                author_name = commit["commit"]["author"]["name"]
                formatted_commit = f"{sha}: {author_name}"
                commits_list.append(formatted_commit)

                # Check if we have processed 10 commits
                if len(commits_list) >= 10:
                    break

            return commits_list
        else:
            print(
                "Failed to fetch commits. Status code:", response.status_code
                )

            return []
    except requests.exceptions.RequestException as e:
        # Handle any request-related errors
        print("Error:", e)
        return []


if __name__ == "__main__":
    # Parse command-line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Fetch and print the commits
    commits = fetch_commits(owner_name, repo_name)

    for commit in commits:
        print(commit)
