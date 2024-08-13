from transformers import pipeline
import tensorflow as tf

print(tf.__version__)

# Load the summarization pipeline
summarizer = pipeline("summarization")

# The text to summarize
text = """
    Natural Language Processing (NLP) is a field of artificial intelligence that focuses on the interaction between 
    computers and humans through natural language. The ultimate goal of NLP is to enable computers to understand, 
    interpret, and generate human language in a way that is both meaningful and useful.
"""

# Generate the summary
summary = summarizer(text, max_length=50, min_length=25, do_sample=False)

print("Summary:")
print(summary[0]['summary_text'])
