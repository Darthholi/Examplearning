
# https://openrouter.ai/models/openchat/openchat-7b:free


import requests
import json

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer TODO",
    #"HTTP-Referer": f"{YOUR_SITE_URL}", # Optional, for including your app on openrouter.ai rankings.
    #"X-Title": f"{YOUR_APP_NAME}", # Optional. Shows in rankings on openrouter.ai.
  },
  data=json.dumps({
    "model": "openchat/openchat-7b:free", # Optional
    "messages": [
      { "role": "user", "content": "What is the meaning of life?" }
    ]
  })
)
print(response.json())