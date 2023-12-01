#!/usr/bin/python3

"""
A script that:
- takes in a letter as an argument
- sends a POST request to http://0.0.0.0:5000/search_user with the
letter as a parameter
- handles the response based on JSON formatting and content
"""

import sys
import requests


def search_user(letter):
    """
    Sends a POST request to search for a user with the
    given letter as a parameter.

    Args:
        letter (str): The letter to search for.

    Returns:
        None
    """
    try:
        # Define the URL
        url = 'http://0.0.0.0:5000/search_user'

        # Set the letter as a parameter
        params = {'q': letter}

        # Send a POST request with the parameter
        response = requests.post(url, data=params)

        # Check if the response is JSON and not empty
        if response.headers.get('content-type') == 'application/json':
            if response.text:
                user_data = response.json()
                if 'id' in user_data and 'name' in user_data:
                    print("[{}] {}".format(user_data['id'], user_data['name']))
                else:
                    print("No result")
            else:
                print("Response is empty")
        else:
            print("Not a valid JSON")

    except requests.exceptions.RequestException as e:
        # Handle any request-related errors
        print("Error:", e)


if __name__ == "__main__":
    # Check if an argument is provided, otherwise set q=""
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    # Call the search_user function with the letter argument
    search_user(letter)
