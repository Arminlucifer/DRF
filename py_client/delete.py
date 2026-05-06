import requests

endpoint = 'http://127.0.0.1:8000/api/products/8/delete/'


response = requests.delete(endpoint)
print(response.status_code)
