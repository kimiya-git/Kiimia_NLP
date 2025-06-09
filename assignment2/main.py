from summarizer.utils import (
    measure_length, proportional_length, generate_query,
    load_text, save_text
)
from summarizer.preprocess import get_average_sentence_length, get_frequent_content_words
from summarizer.summerize import hierarchical_summarization

def main():
    content_text = load_text(r"C:\Users\Asus\PycharmProjects\NLP_kimia\Kiimia_NLP\assignment2\data_assignment2\content_text.txt")
    style_text = load_text(r"C:\Users\Asus\PycharmProjects\NLP_kimia\Kiimia_NLP\assignment2\data_assignment2\style_text.txt")

    content_length = measure_length(content_text)
    style_length = measure_length(style_text)
    context_window = 4000

    content_target_length, style_target_length = proportional_length(content_length, style_length, context_window)

    avg_sentence_length = get_average_sentence_length(style_text)
    frequent_words = get_frequent_content_words(style_text)

    content_summary = hierarchical_summarization(content_text, avg_sentence_length, frequent_words, content_target_length)
    style_summary = hierarchical_summarization(style_text, avg_sentence_length, frequent_words, style_target_length)

    query = generate_query(content_summary, style_summary)

    save_text(r"C:\Users\Asus\PycharmProjects\NLP_kimia\Kiimia_NLP\assignment2\data_assignment2\content_summary2.txt", content_summary)
    save_text(r"C:\Users\Asus\PycharmProjects\NLP_kimia\Kiimia_NLP\assignment2\data_assignment2\style_summary2.txt", style_summary)
    save_text(r"C:\Users\Asus\PycharmProjects\NLP_kimia\Kiimia_NLP\assignment2\data_assignment2\query2.txt", query)

    print("Summaries and query saved to data/")

if __name__ == "__main__":
    main()
