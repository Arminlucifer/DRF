import requests

headers = {
    'Authorization': "Bearer 78927ee16f50b0de0f50fdc2e5db838397684be4"
}


endpoint = 'http://127.0.0.1:8000/api/products/'


data = {
    'title': "This field is DDDD",
    "content": "YOHAHAHAHAHHA"

}

response = requests.post(endpoint, json=data, headers=headers)

print(response.json())
