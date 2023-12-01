#!/usr/bin/python3
"""
1-hbtn_header.py: A script to send a request to a URL and display the
value of the X-Request-Id header.
Usage:
    $ ./1-hbtn_header.py <URL>
"""

import urllib.request
import sys


def fetch_x_request_id(url):
    """
    Fetches a URL and displays the value of the X-Request-Id header.

    Args:
        url (str): The URL to fetch.

    Returns:
        None
    """
    try:
        # Send a GET request to the specified URL
        with urllib.request.urlopen(url) as response:
            # Get the value of the X-Request-Id header
            x_request_id = response.getheader('X-Request-Id')

            if x_request_id:
                print(x_request_id)
            else:
                print("X-Request-Id header not found in the response.")
    except urllib.error.URLError as e:
        # Handle any URL-related errors
        print("Error:", e)


if __name__ == "__main__":
    # Check if a URL argument is provided
    if len(sys.argv) != 2:
        print("Usage: python 1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_x_request_id(url)
