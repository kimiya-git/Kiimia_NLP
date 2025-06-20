import string
import pickle
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from preprocessing import TextPreprocessor


with open(r'C:\Users\Asus\PycharmProjects\NLP_kimia\Kiimia_NLP\src\model.pkl', 'rb') as f:
    model = pickle.load(f)


vectorizer = TfidfVectorizer()
vectorizer.fit(pd.read_csv(r'C:\Users\Asus\PycharmProjects\NLP_kimia\Kiimia_NLP\data\tfidf_matrix.csv').columns)


preprocessor = TextPreprocessor()


def predict(text):
    processed = preprocessor.full_preprocess(text)
    vectorized = vectorizer.transform([processed])
    prediction = model.predict(vectorized)
    return 'Geographic' if prediction[0] == 1 else 'Non-Geographic'


if __name__ == "__main__":
    sample_text = "The Amazon River flows through South America."
    print("Prediction:", predict(sample_text))






