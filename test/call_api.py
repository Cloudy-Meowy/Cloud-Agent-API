import requests

# URL của API Flask
url = "http://127.0.0.1:5000/get-ai-response"

# Dữ liệu test
param = {
    'query': 'Hello, how are you?',
    'system_prompt': 'You are a helpful assistant.',
    'his_message': '',  # Nếu có nhiều message, dùng list
    'es_cloud_id': 'agent_elastic:YXNpYS1zb3V0aGVhc3QxLmdjcC5lbGFzdGljLWNsb3VkLmNvbTo0NDMkMTVhN2M0YjQ2MjRhNDI3MjkzYjM5ZWNjMGYzNWRlNTEkYzYyNzdhOWJhMTFlNDBkOGI3NDg4NTFlNmVlYWUzNmU=',
    'es_username': 'elastic',
    'es_password': 'dfbrEbfnW6RHG0hTFHouCblj',
    'index': 'my_index',
}

# Gửi request GET
response = requests.get(url, params=param)

# In kết quả
print("Status code:", response.status_code)
print("Response:", response.json())
