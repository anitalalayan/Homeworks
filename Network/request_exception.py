import requests

url = "https://jsonplaceholder.typicode.com/invalid-url"

try:
    response = requests.get(url)
    print(response.raise_for_status())

    try:
        print("Response received successfully:", response.json())
    except ValueError:
        print("Response is not in valid JSON format.")

except requests.exceptions.RequestException as error:
    print(f"Error occurred: {error}")