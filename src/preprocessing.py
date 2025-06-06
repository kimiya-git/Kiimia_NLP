import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download required NLTK data
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')


class TextPreprocessor:
    def __init__(self):
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    def clean_text(self, text):
        """Basic text cleaning"""
        # Convert to lowercase
        text = text.lower()

        # Remove URLs
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

        # Remove HTML tags
        text = re.sub(r'<.*?>', '', text)

        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))

        # Remove numbers
        text = re.sub(r'\d+', '', text)

        # Remove extra whitespace
        text = ' '.join(text.split())

        return text

    def remove_stopwords(self, text):
        """Remove stop words from text"""
        words = nltk.word_tokenize(text)
        filtered_words = [word for word in words if word not in self.stop_words]
        return ' '.join(filtered_words)

    def stem_text(self, text):
        """Apply stemming to text"""
        words = nltk.word_tokenize(text)
        stemmed_words = [self.stemmer.stem(word) for word in words]
        return ' '.join(stemmed_words)

    def lemmatize_text(self, text):
        """Apply lemmatization to text"""
        words = nltk.word_tokenize(text)
        lemmatized_words = [self.lemmatizer.lemmatize(word) for word in words]
        return ' '.join(lemmatized_words)

    def full_preprocess(self, text, stem=False, lemma=True):
        """Complete preprocessing pipeline"""
        text = self.clean_text(text)
        text = self.remove_stopwords(text)

        if stem:
            text = self.stem_text(text)
        elif lemma:
            text = self.lemmatize_text(text)

        return text