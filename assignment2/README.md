# Assignment 2 – Context-Aware Summarization with Style Transfer

## 📚 Project Overview

This project implements a summarization pipeline that generates a summary of a content document in the **style of another document**. The summarization is performed using a hierarchical approach when the input exceeds the context window limit. The implementation is done in **Python** using **NLTK**.

## 🧠 Objective

Given two input texts:
- **Content Text**: the document to be summarized.
- **Style Text**: the document whose writing style should be mimicked.

The system:
1. Summarizes both documents proportionally based on their lengths.
2. Generates a query that instructs a language model to summarize the content in the style of the second document.

## 🛠️ Technologies Used
- Python 3.x
- NLTK (Natural Language Toolkit)

## 📁 Project Structure

NLP_kimia/ │ 
├── Kiimia_NLP/ │ └── assignment2/ │ ├── data_assignment2/ │ │ ├── content_text.txt │ │ ├── style_text.txt │ │ ├── content_summary2.txt │ │ ├── style_summary2.txt │ │ └── query2.txt │ │ │ ├── summarizer/ │ │
├── preprocess.py │ │ 
├── summerize.py │ │ 
├── summerize - Copy.py │ │
└── utils.py │ │ │ └── main.py │ 
├── data/ │ 
├── processed_dataset.csv │ 
├── tfidf_matrix.csv │ 
└── wikipedia_dataset.csv │ 
└── src/ 
├── configs/ 
│ 
├── confusion_matrix.png │ 
└── feature_extraction.py 
├── main.py 
├── model.pkl 
└── prediction_pipeline.py

## 🔄 Pipeline Steps

1. **Load Input Texts** from the `data/` folder.
2. **Measure Lengths** of both documents.
3. **Compute Target Lengths** proportionally based on a context window (default: 4000 tokens).
4. **Extract Style Features** from the style text (average sentence length and frequent words).
5. **Summarize Both Texts** using a hierarchical summarization strategy.
6. **Generate a Query** that combines both summaries.
7. **Save Outputs** to the `data_assignment2/` folder.

## ▶️ How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
