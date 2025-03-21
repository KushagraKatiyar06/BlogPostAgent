from textblob import TextBlob

class ProofreadingAgent:
    def proofread(self, content):
        print("Proofreading content...")

        blob = TextBlob(content)
        corrected_content = blob.correct()

        return str(corrected_content)
