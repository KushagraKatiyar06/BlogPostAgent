from content_generation_agent import ContentGenerationAgent
from research_agent import ResearchAgent
from seo_optimization_agent import SEOOptimizationAgent
from proofreading_agent import ProofreadingAgent
import random


class BlogGenerator:
    def __init__(self):
        self.research_agent = ResearchAgent()
        self.generation_agent = ContentGenerationAgent()
        self.proofreading_agent = ProofreadingAgent()

    def generate_blog(self):
        print("Searching for trending HR topics...")

        # Researcher Agent finds trending topics.
        trending_topics = self.research_agent.get_trending_topics()

        if not trending_topics:
            print("No trending topics found.")
            return

        selected_topic = random.choice(trending_topics)
        print(f"Selected Topic: {selected_topic}")

        #Uses generation agent to generate material for the blog.
        blog_content = self.generation_agent.generate_content(selected_topic)

        # Optimizes generated content with SEO
        seo_agent = SEOOptimizationAgent(selected_topic)
        blog_content = seo_agent.optimize_content(blog_content)

        # Proofreads Blog 
        blog_content = self.proofreading_agent.proofread(blog_content)

        # Saves the file
        filename = f"generated_blog_{selected_topic.replace(' ', '_')}.md"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"# {selected_topic}\n\n{blog_content}")

        print(f"Blog generated and saved as {filename}!")

generator = BlogGenerator()
generator.generate_blog()
