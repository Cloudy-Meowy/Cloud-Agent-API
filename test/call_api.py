import requests

# URL của API Flask
url = "http://127.0.0.1:5000/get-ai-response"

# Dữ liệu test
param = {
    "query": "nêu những điểm quan trọng nhất về luật lao động",
    "system_prompt": "Bạn là một chuyên gia về luật. Dựa trên thông tin truy vấn được, hãy phản hồi câu query của người dùng. Bạn cũng được cung cấp lịch sử trò chuyện trước đó nếu có để trả lời khi người dùng tiếp tục hỏi các nội dung liên quan đến các nội dung trong lịch sử trò chuyện Luôn cung cấp nguồn thông tin cho câu trả lời của bạn.",
    "his_message": "",  
    "es_cloud_id": "agent_elastic:YXNpYS1zb3V0aGVhc3QxLmdjcC5lbGFzdGljLWNsb3VkLmNvbTo0NDMkMTVhN2M0YjQ2MjRhNDI3MjkzYjM5ZWNjMGYzNWRlNTEkYzYyNzdhOWJhMTFlNDBkOGI3NDg4NTFlNmVlYWUzNmU=",
    "es_username": "elastic",
    "es_password": "dfbrEbfnW6RHG0hTFHouCblj",
    "index": "my_index"
}

# Gửi request GET
response = requests.get(url, params=param)

# In kết quả
print("Status code:", response.status_code)
print("Response:", response.json())
