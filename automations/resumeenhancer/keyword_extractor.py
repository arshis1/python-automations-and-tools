import re #regular expressions
import string 
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from url_to_text_extractor import extract_all_meta_from_url

# Make sure you have NLTK resources
import nltk
#nltk.download('punkt')
#nltk.download('stopwords')

def extract_keywords(text, top_n=10):
    # Lowercase the text
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize
    words = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    keywords = [word for word in words if word not in stop_words and word.isalpha()]
    
    # Get the most common keywords
    most_common = Counter(keywords).most_common(top_n)
    
    return [word for word, freq in most_common]

# Example usage
#sample_text = " AI SQL Data Skills"
#keywords = extract_keywords(sample_text)
#print("Keywords:", keywords)