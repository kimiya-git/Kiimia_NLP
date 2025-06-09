from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
from nltk.corpus import stopwords

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
