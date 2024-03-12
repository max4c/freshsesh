import requests
import json

url = "http://localhost:11434/api/generate"

data = {
    "model": "llama2",
    "prompt": "What's temperature usually in utah in march? Respond in one to two short sentences.",
    "stream": False
}

response = requests.post(url, data=json.dumps(data))
response_json = response.json()
response_value = response_json['response']

print(response_value)
