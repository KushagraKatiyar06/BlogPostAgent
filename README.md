# BlogPostAgent

Multi-Agent SEO Blog Generator
🚀 A Python-based multi-agent system that generates a high-quality, SEO-optimized blog post on trending HR topics using AI.

📝 Table of Contents
📌 Project Overview
🛠️ Features
⚙️ System Architecture
🔄 Workflow
🛠️ Installation
🚀 Usage
📂 File Structure
📌 Technologies Used
👨‍💻 Author
📜 License

📌 Project Overview
The Multi-Agent SEO Blog Generator is a Python-based AI system that autonomously:
✅ Finds trending HR topics
✅ Generates a structured blog outline
✅ Creates high-quality content
✅ Optimizes for SEO
✅ Proofreads & improves readability

🛠️ Features
✔ Automated Topic Research – Uses SerpAPI to find trending HR topics
✔ Dynamic Blog Outline – Generates adaptive sections based on topic relevance
✔ AI Content Generation – Uses DeepSeek AI to write the blog
✔ SEO Optimization – Implements keyword usage, meta descriptions
✔ Grammar & Proofreading – Enhances readability using language_tool

⚙️ System Architecture
The project follows a modular agent-based design:

1️⃣ Research Agent → Finds trending HR topics 📊
2️⃣ Content Planning Agent → Creates a dynamic outline 📝
3️⃣ Content Generation Agent → Writes the blog using AI 🤖
4️⃣ SEO Optimization Agent → Enhances content for SEO 🔍
5️⃣ Proofreading Agent → Fixes grammar & readability issues ✅

🔄 Workflow
Step 1: ResearchAgent finds trending HR topics.
Step 2: ContentPlanningAgent generates a dynamic outline.
Step 3: ContentGenerationAgent writes the blog post.
Step 4: SEOAgent optimizes content for search engines.
Step 5: ProofreadingAgent checks for grammar mistakes.
Step 6: Final blog is saved in output/ folder.

🛠️ Installation

🔹 1. Clone the Repository

git clone https://github.com/your-username/BlogPostAgent.git
cd BlogPostAgent

🔹 2. Install Dependencies

pip install -r requirements.txt

🔹 3. Set Up API Keys
Create a .env file and add your API keys:

SERPAPI_KEY=your-serpapi-key
DEEPSEEK_API_KEY=your-deepseek-key

🚀 Usage
Run the blog_generator.py script to generate a blog post:

python blog_generator.py

The blog post will be saved as output/blog.md.

Technologies Used
✅ Python – Main programming language
✅ DeepSeek API – AI-powered content generation
✅ SerpAPI – Web search & research
✅ LangChain – Multi-agent orchestration
✅ BeautifulSoup – Web scraping
✅ LanguageTool – Grammar & proofreading

👨‍💻 Kushagra Katiyar
📧 Email: k.katiyar2006@gmail.com
🔗 GitHub: KushagraKatiyar06

📜 License
MIT License - Free to use, modify, and distribute.

Let me know if you want any modifications! 🚀😊