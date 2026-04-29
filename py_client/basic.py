import requests

endpoint = "http://localhost:8000/api/"

response = requests.get(endpoint, json={
                        'product_id': 123})

# print(response.text)
# print(response.status_code)


print(response.json())
