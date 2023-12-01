#!/usr/bin/python3

"""
A script that:
- takes in a URL.
- sends a request to the URL.
- displays the body of the response (decoded in utf-8)
- handles urllib.error.HTTPError exceptions
"""

import sys
import urllib.request
import urllib.error


def fetch_and_display_response(url):
    """
    Fetches a URL and displays the body of the response.

    Args:
        url (str): The URL to fetch.

    Returns:
        None
    """
    try:
        # Send a GET request to the specified URL
        with urllib.request.urlopen(url) as response:
            # Read and decode the response body
            body = response.read().decode('utf-8')

            print("Response body:")
            print(body)
    except urllib.error.HTTPError as e:
        # Handle HTTP errors and print the HTTP status code
        print("Error code:", e.code)
    except urllib.error.URLError as e:
        # Handle URL-related errors (e.g., invalid URL)
        print("URL Error:", e)


if __name__ == "__main__":
    # Check if a URL argument is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_and_display_response(url)
