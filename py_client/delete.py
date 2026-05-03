import requests

endpoint = 'http://localhost:8000/api/products/8/delete/'


response = requests.delete(endpoint)
print(response.status_code)
