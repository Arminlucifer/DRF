import requests
from getpass import getpass

AuthEndpoint = 'http://127.0.0.1:8000/api/auth/'

username = input("What is your username? ")
password = getpass("Enter your password: ")

auth_response = requests.post(AuthEndpoint, json={
    'username': username,
    "password": password
})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = 'http://127.0.0.1:8000/api/products/'

    response = requests.get(endpoint, headers=headers)

    print(response.json())
