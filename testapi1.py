import requests

LLM_BASE_URL = "http://mini.local:1234" # replace with your server address

# # Fetch available models
# response = requests.get(f"{LLM_BASE_URL}/v1/models")
# if response.status_code == 200:
#     models = response.json()
#     print("Available Models:", models)
# else:
#     print(f"Failed to fetch models: {response.status_code} - {response.text}")

payload = {
    "model": "qwen2.5-7b-instruct-1m", # "deepseek-r1-distill-qwen-7b",  # Replace with your desired model name
    "prompt": "Construct a fake news headline from the future including a time of 2:30",
    "max_tokens": 100,
    "temperature": 0.7
}

# Send the request
response = requests.post(f"{LLM_BASE_URL}/v1/completions", json=payload)

if response.status_code == 200:
    data = response.json()
    print("Completion Response:")
    print(data.get("choices", [{}])[0].get("text", "No response"))
else:
    print(f"Error: {response.status_code} - {response.text}")