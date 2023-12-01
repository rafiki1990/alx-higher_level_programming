#!/usr/bin/python3

"""
A script that:
- takes in a URL
- sends a request to the URL
- displays the body of the response
- handles HTTP status codes
"""

import sys
import requests


def fetch_and_display_response(url):
    """
    Fetches a URL, checks the HTTP status code, and displays the error
    code if >= 400.

    Args:
        url (str): The URL to fetch.

    Returns:
        None
    """
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Check if the HTTP status code is greater than or equal to 400
        if response.status_code >= 400:
            print("Error code:", response.status_code)
        else:
            # Display the response body for successful requests
            print("Response body:")
            print(response.text)
    except requests.exceptions.RequestException as e:
        # Handle any request-related errors
        print("Error:", e)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_and_display_response(url)
