# Open AI API key is stored in config.py
import config

import openai


openai.api_key = config.OPEN_AI_API_KEY


response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a Genius coder ."},
        {"role": "user", "content": "write me code to center a div"},
    ]
)

print(response["choices"][0]["message"]["content"])