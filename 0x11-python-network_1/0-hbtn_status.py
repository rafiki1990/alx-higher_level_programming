#!/usr/bin/python3
"""
0-hbtn_status.py: A script to fetch a URL and display information about
the response using urllib.

Usage:
    $ ./0-hbtn_status.py
"""

import urllib.request


def fetch_and_display_status(url):
    """
    Fetches a URL and displays information about the response.

    Args:
        url (str): The URL to fetch.

    Returns:
        None
    """
    try:
        # Send a GET request to the specified URL
        with urllib.request.urlopen(url) as response:
            # Read the response body as bytes
            body = response.read()

            # Decode the bytes to a UTF-8 string
            utf8_body = body.decode('utf-8')

        # Display information about the response
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", utf8_body)
    except urllib.error.URLError as e:
        # Handle any URL-related errors
        print("Error:", e)


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    fetch_and_display_status(url)
