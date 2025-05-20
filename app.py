from flask import Flask, request, jsonify
import openai
from elasticsearch import Elasticsearch
import os
from source.model import call_agent

app = Flask(__name__)

# Lấy API key từ biến môi trường
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/get-ai-response', methods=['GET'])
def get_ai_response():
    try:
        # Lấy parameters
        query = request.args.get('query')
        system_prompt = request.args.get('system_prompt')
        his_message = request.args.getlist('his_message')
        es_cloud_id = request.args.get('es_cloud_id')
        es_username = request.args.get('es_username')
        es_password = request.args.get('es_password')
        index = request.args.get('index')

        # Kiểm tra bắt buộc sau khi đã lấy biến
        if not all([query, system_prompt, es_cloud_id, es_username, es_password, index]):
            return jsonify({'error': 'Thiếu tham số bắt buộc'}), 400

        # Gọi hàm xử lý chính
        response = call_agent(
            query=query,
            system_prompt=system_prompt,
            his_message=his_message,
            es_cloud_id=es_cloud_id,
            es_username=es_username,
            es_password=es_password,
            index=index
        )

        return jsonify(response), 200

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500
    

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=False, host='0.0.0.0', port=port)