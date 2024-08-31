import time
import random
import requests
import json

# URL to POST to
url = "https://silent-dew-3400.ploomber.com/getplayers"

# Payload to send in the POST request
payload = [
    {
        "league_id": 123123,
        "playerlist": ["9229", "11568", "11574", "8112", "9997", "11604", "11635", "11631", "9488", "6797"]
    },
    {
        "league_id": 123124,
        "playerlist": ["6804", "7528", "6845", "6786", "6819", "5857", "7525", "5947", "8167", "8183"]
    }
]

# Function to perform the POST request
def ping():
    print("Making POST request...")
    try:
        response = requests.post(url, json=payload)
        print(f"Response status code: {response.status_code}")
        if response.status_code == 200:
            print("POST request successful")
        else:
            print(f"POST request failed with status code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred during POST request: {e}")

if __name__ == "__main__":
    print("Starting...")
    while True:
        # Random delay between 6 and 8 hours
        print("So lets PING then shall we!")
        ping()
        delay = random.uniform(1 * 3600, 2 * 3600)
        print(f"Waiting for {delay / 3600:.2f} hours before making the next POST request.")
        time.sleep(delay)

        # Make the POST request

