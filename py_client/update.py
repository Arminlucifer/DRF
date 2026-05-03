import requests

endpoint = 'http://localhost:8000/api/products/6/update/'


data = {
    "title": "this is a test for Updating"
}

response = requests.put(endpoint, json=data)
print(response.json())
