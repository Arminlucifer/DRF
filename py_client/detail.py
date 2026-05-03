import requests

endpoint = 'http://localhost:8000/api/products/8'

response = requests.get(endpoint)
print(response.json())
