# SuMi is a niche library, and I'll assume we're using a fictional API here as SuMi is not widely documented.

from sumi import SuMiSummarizer

# Initialize the SuMi summarizer
summarizer = SuMiSummarizer()

# The text to summarize
text = """
    Natural Language Processing (NLP) is a field of artificial intelligence that focuses on the interaction between 
    computers and humans through natural language. The ultimate goal of NLP is to enable computers to understand, 
    interpret, and generate human language in a way that is both meaningful and useful.
"""

# Generate the summary
summary = summarizer.summarize(text)

print("Summary:")
print(summary)
