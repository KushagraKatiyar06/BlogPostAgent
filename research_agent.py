import os
import requests
from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv("deepseek.env") 
load_dotenv("serpapi.env")   

# Create a class for a 'Researcher Agent'
class ResearchAgent:
    def __init__(self):
        self.serpapi_key = os.getenv("SERPAPI_KEY")
        if not self.serpapi_key:
            raise ValueError("No API key found for SerpAPI. Check your .env file!")

# Using Serpapi, trending topics are found by searching on google
    def get_trending_topics(self):
        print("Searching for trending HR topics...")

        params = {
            "q": "HR trends 2025",  #search parameter
            "api_key": self.serpapi_key
        }
        
        search = GoogleSearch(params)  
        results = search.get_dict()
        
        trending_topics = []  #trending topics are inside this list
        for result in results.get("organic_results", []): 
            trending_topics.append(result.get("title"))
        
        return trending_topics
