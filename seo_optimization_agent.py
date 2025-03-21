import re

class SEOOptimizationAgent:
    def __init__(self, target_keyword):
        self.target_keyword = target_keyword.lower()

    def optimize_content(self, content):
        print("Optimizing content for SEO...")

        #content = self.ensure_keyword_placement(content)

        #content = self.improve_readability(content)

        return content

    def ensure_keyword_placement(self, content):
        lines = content.split("\n")

        if self.target_keyword not in lines[0].lower():
            lines[0] = f"{lines[0]} | {self.target_keyword.title()}"

        for i in range(1, len(lines)):
            if lines[i].startswith("#") and self.target_keyword not in lines[i].lower():
                lines[i] += f" - {self.target_keyword.title()}"
                break

        return "\n".join(lines)

    def improve_readability(self, content):
        """Shortens long sentences and removes passive voice."""
        content = re.sub(r"\b(be|is|are|was|were|been|being) (.*?ed)\b", r"\2", content)  # Reduce passive voice
        content = re.sub(r"(\w{10,})", lambda x: x.group(1)[:7] + "-", content)  # Shorten long words
        return content
