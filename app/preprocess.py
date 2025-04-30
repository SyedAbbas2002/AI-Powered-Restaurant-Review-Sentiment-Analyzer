import re

def preprocess_text(text):
    # Basic preprocessing (customize as needed)
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text.strip()
