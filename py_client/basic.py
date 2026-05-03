import requests

endpoint = "http://localhost:8000/api/"

response = requests.post(endpoint, json={"title": "test", "content": "AAA"})

# print(response.text)
# print(response.status_code)


print(response.json())
