import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Download NLTK resources (run once)
nltk.download('stopwords')
nltk.download('wordnet')

# Load your dataset
df = pd.read_csv(r'C:\Users\Asus\PycharmProjects\NLP_kimia\Kiimia_NLP\data\processed_dataset.csv')

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['processed_text'])

# Optional: Save the matrix and feature names
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
tfidf_df.to_csv(r'C:\Users\Asus\PycharmProjects\NLP_kimia\Kiimia_NLP\data/tfidf_matrix.csv', index=False)

# Print shape and sample
print("TF-IDF matrix shape:", tfidf_matrix.shape)
print(tfidf_df.head())
