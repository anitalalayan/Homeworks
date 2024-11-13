# Use the requests module to send a GET request to the URL https://jsonplaceholder.typicode.com/posts.
# Retrieve posts by a specific user by adding a query parameter (e.g., ?userId=1).
# Parse the JSON response and print the titles of the posts.

import requests

url = "https://jsonplaceholder.typicode.com/posts"
userId=1

response = requests.get(url, params={'userId':userId})

if response.status_code == 200:
    posts = response.json()


    for post in posts:
        print(post["title"])

else:
    print("Failed to retrieve data:", response.status_code)