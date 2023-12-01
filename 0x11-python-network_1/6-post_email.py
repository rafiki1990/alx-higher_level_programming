#!/usr/bin/python3

"""
A script that:
- takes in a URL and an email address
- sends a POST request to the passed URL with the email as a parameter
- displays the body of the response
"""

import sys
import requests


def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with the email as a parameter.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email address to include as a parameter.

    Returns:
        None
    """
    try:
        # Create a dictionary with the email parameter
        data = {"email": email}

        # Send a POST request to the specified URL with the data
        response = requests.post(url, data=data)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Display the response body
            print("Response body:")
            print(response.text)
        else:
            print("Error: HTTP Status Code", response.status_code)
    except requests.exceptions.RequestException as e:
        # Handle any request-related errors
        print("Error:", e)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
