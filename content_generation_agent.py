import os
import requests
from dotenv import load_dotenv

load_dotenv("deepseek.env") 
load_dotenv("serpapi.env")   

class ContentGenerationAgent:
    def __init__(self):
        self.api_key = os.getenv("DEEPSEEK_API_KEY")

        if not self.api_key:
            raise ValueError("No API key found for DeepSeek. Check your .env file!")

    # Calls deepseek api to take in a prompt
    def generate_content(self, prompt):
        print(f"Generating content for: {prompt}...")

        url = "https://api.deepseek.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {
            "model": "deepseek-chat",
            "messages": [{"role": "system", "content": prompt}],
            "temperature": 0.7
        }

        response = requests.post(url, json=data, headers=headers)
        if response.status_code != 200:
            raise Exception(f"DeepSeek API request failed! Status: {response.status_code}")

        content = response.json()["choices"][0]["message"]["content"]
        return content
