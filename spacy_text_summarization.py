import spacy

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# The text to summarize
text = """
    Natural Language Processing (NLP) is a field of artificial intelligence that focuses on the interaction between 
    computers and humans through natural language. The ultimate goal of NLP is to enable computers to understand, 
    interpret, and generate human language in a way that is both meaningful and useful.
"""

# Process the text with spaCy
doc = nlp(text)

# Extract the most important sentences based on sentence length (a simple heuristic)
summary = sorted(doc.sents, key=lambda sent: len(sent), reverse=True)[0].text

print("Summary:")
print(summary)
