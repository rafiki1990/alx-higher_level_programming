#!/usr/bin/python3

"""
A script that:
- takes in a URL
- sends a request to the URL
- displays the value of the X-Request-Id variable in the response header
"""

import sys
import requests


def fetch_x_request_id(url):
    """
    Fetches a URL and displays the value of the X-Request-Id
    variable in the response header.
    Args:
        url (str): The URL to fetch.
    Returns:
        None
    """
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Get the value of the X-Request-Id header
            x_request_id = response.headers.get('X-Request-Id')

            if x_request_id:
                print(x_request_id)
            else:
                print("X-Request-Id header not found in the response.")
        else:
            print("Error: HTTP Status Code", response.status_code)
    except requests.exceptions.RequestException as e:
        # Handle any request-related errors
        print("Error:", e)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_x_request_id(url)
