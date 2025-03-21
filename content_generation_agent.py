import os
import requests
from dotenv import load_dotenv
import random

load_dotenv("deepseek.env") 
load_dotenv("serpapi.env")   

class ContentGenerationAgent:
    def __init__(self):
        self.api_key = os.getenv("DEEPSEEK_API_KEY")

        if not self.api_key:
            raise ValueError("No API key found for DeepSeek. Check your .env file!")

    # Calls deepseek api to take in a prompt
    def generate_content(self, topic):
        print(f"Generating content for: {topic}...")

        # Adding more context to the prompt to make responses more varied
        prompt_variations = [
            f"Write a fresh and unique blog post about {topic}. Include recent trends and insights.",
            f"Generate a well-structured article about {topic}, covering the latest developments in 2025.",
            f"Provide a research-backed blog post on {topic}, including expert opinions and case studies.",
            f"Create a conversational and engaging blog post about {topic}, making it easy for readers to understand.",
            f"Write a professional, SEO-optimized article on {topic} with actionable advice."
        ]
        
        prompt = random.choice(prompt_variations)  # Pick a random prompt for variation

        url = "https://api.deepseek.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {
            "model": "deepseek-chat",
            "messages": [{"role": "system", "content": prompt}],
            "temperature": 0.9,  # Increased randomness
            "top_p": 0.95,  # More diversity in word choice
        }

        response = requests.post(url, json=data, headers=headers)
        if response.status_code != 200:
            raise Exception(f"DeepSeek API request failed! Status: {response.status_code}")

        content = response.json()["choices"][0]["message"]["content"]
        return content
