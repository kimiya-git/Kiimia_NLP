from nltk.tokenize import word_tokenize

def measure_length(text):
    return len(word_tokenize(text))

def proportional_length(content_length, style_length, context_window):
    total_length = content_length + style_length
    content_target_length = int((content_length / total_length) * context_window)
    style_target_length = context_window - content_target_length
    return content_target_length, style_target_length

def generate_query(content_summary, style_summary):
    return f"Summarize the following content in the style of the provided text:\n\nContent Summary:\n{content_summary}\n\nStyle Summary:\n{style_summary}"

def load_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def save_text(filepath, text):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
