import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

def get_average_sentence_length(text):
    sentences = sent_tokenize(text)
    total_length = sum(len(word_tokenize(sentence)) for sentence in sentences)
    return total_length / len(sentences)

def get_frequent_content_words(text, top_n=50):
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    content_words = [word for word in words if word.isalnum() and word not in stop_words]
    word_freq = Counter(content_words)
    return [word for word, freq in word_freq.most_common(top_n)]
