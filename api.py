import requests

url = "https://api.perplexity.ai/chat/completions"
headers = {
    "accept": "application/json",
    "authorization": "Bearer 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",
    "content-type": "application/json"
}
data = {
    "model": "pplx-70b-online",
    "messages": [
        {
            "content": "How many people in USA have a driving license?",
            "role": "user"
        }
    ],
    "max_tokens": 0,
    "temperature": 1,
    "top_p": 1,
    "top_k": 0,
    "stream": False,
    "presence_penalty": 0,
    "frequency_penalty": 1
}

response = requests.post(url, headers=headers, json=data)

print(response.json())