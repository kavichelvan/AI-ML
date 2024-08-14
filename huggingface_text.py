from transformers import pipeline
import tensorflow as tf

print(tf.__version__)

# Load the summarization pipeline
summarizer = pipeline("summarization")

# The text to summarize
text = """
    LLMs are the core technology that powers many NLP tasks. They are trained on vast datasets and can generate or understand human language. NLP is the broader field that involves all techniques and tasks related to processing and analyzing language data. LLaMA is a specific implementation of an LLM developed by Meta, highlighting advancements in efficiency and scalability in the field of language models.Imagine you are building a virtual assistant. You'd use an LLM (like GPT or LLaMA) to understand and generate responses to user queries. The LLM would be part of an NLP system that also includes tasks like speech recognition, sentiment analysis, and translation to ensure the assistant can interact naturally with users.
"""

# Generate the summary
summary = summarizer(text, max_length=50, min_length=25, do_sample=False)

print("Summary:")
print(summary[0]['summary_text'])
