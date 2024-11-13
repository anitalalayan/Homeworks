import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    'title': "Getting acquainted with APIs",
    'body': "Learning how to use requests module",
    'userId': 1
}

x = requests.post(url, json = data)
print(x.text)