from transformers import pipeline

# Load a pre-trained model for summarization
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Provide text to summarize
text = """
LLMs are the core technology that powers many NLP tasks. They are trained on vast datasets and can generate or understand human language. NLP is the broader field that involves all techniques and tasks related to processing and analyzing language data. LLaMA is a specific implementation of an LLM developed by Meta, highlighting advancements in efficiency and scalability in the field of language models.Imagine you are building a virtual assistant. You'd use an LLM (like GPT or LLaMA) to understand and generate responses to user queries. The LLM would be part of an NLP system that also includes tasks like speech recognition, sentiment analysis, and translation to ensure the assistant can interact naturally with users.
"""

# Generate a summary
summary = summarizer(text, max_length=16, min_length=30, do_sample=False)
print(summary)
