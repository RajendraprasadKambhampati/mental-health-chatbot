# preprocess.py
import re
import string
import nltk

# Uncomment if you haven't downloaded these
# nltk.download('punkt')
# nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Set of English stopwords
stop_words = set(stopwords.words('english'))

def clean_text(text):
    """
    Function to preprocess text:
    - Lowercase
    - Remove punctuation
    - Remove extra spaces
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def tokenize_text(text):
    """
    Function to tokenize text and remove stopwords
    """
    # Tokenize
    tokens = word_tokenize(text)
    
    # Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]
    
    return tokens

# Example usage
if __name__ == "__main__":
    sample_text = "I’m feeling very anxious about my exams!"
    cleaned = clean_text(sample_text)
    tokens = tokenize_text(cleaned)
    
    print("Original:", sample_text)
    print("Cleaned:", cleaned)
    print("Tokens:", tokens)
