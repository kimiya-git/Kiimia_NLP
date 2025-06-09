import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from nltk.corpus import wordnet as wn

nltk.download('punkt')
nltk.download('stopwords')

def measure_length(text):
    return len(word_tokenize(text))

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

def score_sentences(text, avg_sentence_length, frequent_words):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalnum() and word not in stop_words]
    word_freq = Counter(words)
    sentence_scores = {}
    for sentence in sentences:
        sentence_words = word_tokenize(sentence.lower())
        length_score = 1 - abs(len(sentence_words) - avg_sentence_length) / avg_sentence_length
        word_score = sum(word_freq[word] for word in sentence_words if word in word_freq)
        content_word_score = sum(1 for word in sentence_words if word in frequent_words)
        total_score = length_score + word_score + content_word_score
        sentence_scores[sentence] = total_score
    return sentence_scores

def summarize_text(text, avg_sentence_length, frequent_words, max_sentences=5):
    scores = score_sentences(text, avg_sentence_length, frequent_words)
    top_sentences = sorted(scores, key=scores.get, reverse=True)[:max_sentences]
    return ' '.join(top_sentences)

def hierarchical_summarization(text, avg_sentence_length, frequent_words, context_window=4000):
    tokens = word_tokenize(text)
    if len(tokens) <= context_window:
        return summarize_text(text, avg_sentence_length, frequent_words)
    chunks = [' '.join(tokens[i:i+context_window]) for i in range(0, len(tokens), context_window)]
    summaries = [summarize_text(chunk, avg_sentence_length, frequent_words) for chunk in chunks]
    return summarize_text(' '.join(summaries), avg_sentence_length, frequent_words)

def proportional_length(content_length, style_length, context_window):
    total_length = content_length + style_length
    content_target_length = int((content_length / total_length) * context_window)
    style_target_length = context_window - content_target_length
    return content_target_length, style_target_length

def generate_query(content_summary, style_summary):
    return f"Summarize the following content in the style of the provided text:\n\nContent Summary:\n{content_summary}\n\nStyle Summary:\n{style_summary}"

# Example usage
with open(r"C:\Users\Asus\PycharmProjects\NLP_kimia\Kiimia_NLP\assignment2\data_assignment2\content_text.txt", "r") as f:
    content_text = f.read()

with open(r"C:\Users\Asus\PycharmProjects\NLP_kimia\Kiimia_NLP\assignment2\data_assignment2\style_text.txt", "r") as f:
    style_text = f.read()

content_length = measure_length(content_text)
style_length = measure_length(style_text)
context_window = 4000

content_target_length, style_target_length = proportional_length(content_length, style_length, context_window)

avg_sentence_length = get_average_sentence_length(style_text)
frequent_words = get_frequent_content_words(style_text)

content_summary = hierarchical_summarization(content_text, avg_sentence_length, frequent_words, content_target_length)
style_summary = hierarchical_summarization(style_text, avg_sentence_length, frequent_words, style_target_length)

query = generate_query(content_summary, style_summary)

with open("content_summary2.txt", "w") as f:
    f.write(content_summary)

with open("style_summary2.txt", "w") as f:
    f.write(style_summary)

with open("query2.txt", "w") as f:
    f.write(query)

print("Summaries and query saved to content_summary.txt, style_summary.txt, and query.txt")

