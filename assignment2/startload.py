import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

def measure_length(text):
    return len(word_tokenize(text))

def score_sentences(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalnum() and word not in stop_words]
    word_freq = Counter(words)
    sentence_scores = {}
    for sentence in sentences:
        sentence_words = word_tokenize(sentence.lower())
        score = sum(word_freq[word] for word in sentence_words if word in word_freq)
        sentence_scores[sentence] = score
    return sentence_scores

def summarize_text(text, max_sentences=5):
    scores = score_sentences(text)
    top_sentences = sorted(scores, key=scores.get, reverse=True)[:max_sentences]
    return ' '.join(top_sentences)

def hierarchical_summarization(text, context_window=4000):
    tokens = word_tokenize(text)
    if len(tokens) <= context_window:
        return summarize_text(text)
    chunks = [' '.join(tokens[i:i+context_window]) for i in range(0, len(tokens), context_window)]
    summaries = [summarize_text(chunk) for chunk in chunks]
    return summarize_text(' '.join(summaries))

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

content_summary = hierarchical_summarization(content_text, content_target_length)
style_summary = hierarchical_summarization(style_text, style_target_length)

query = generate_query(content_summary, style_summary)

with open("content_summary.txt", "w") as f:
    f.write(content_summary)

with open("style_summary.txt", "w") as f:
    f.write(style_summary)

with open("query.txt", "w") as f:
    f.write(query)

print("Summaries and query saved to content_summary.txt, style_summary.txt, and query.txt")

