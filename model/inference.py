from transformers import pipeline

# Load Hugging Face model
classifier = pipeline("sentiment-analysis")

def predict(text):
    result = classifier(text)
    return result[0]['label']  # Returns only the label