from transformers import pipeline

# Load a pre-trained model for summarization
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Provide text to summarize
text = """
Large language models (LLMs) are a type of deep learning model that are trained on vast amounts of text data. These models...
"""

# Generate a summary
summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
print(summary)
