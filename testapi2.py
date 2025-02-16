# Define the prompt and parameters
payload = {
    "model": "deepseek-r1-distill-qwen-7b",  # Replace with your desired model name
    "prompt": "What are the key benefits of local LLM systems?",
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