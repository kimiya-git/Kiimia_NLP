
# Wikipedia Text Classification: Geographic vs Non-Geographic

## 📌 Project Overview

This project addresses the task of classifying English Wikipedia texts into two categories:
- **Geographic**
- **Non-Geographic**

The classification is based on natural language processing (NLP) techniques and machine learning models. The goal is to build a pipeline that can automatically determine whether a given Wikipedia article is related to geographic content.

## 🧠 Problem Statement

Given a text input (in English), the system must assign it to one of two classes:
- `Geographic`
- `Non-Geographic`

The classification is based on features extracted from the text, which may include annotated keywords, linguistic patterns, and statistical representations.

## 🛠️ Technologies Used

- **Python 3.10+**
- **NLTK** – for tokenization, stopword removal, stemming, and lemmatization
- **SpaCy** – for advanced NLP tasks (optional)
- **scikit-learn** – for machine learning models (Naive Bayes, Logistic Regression)
- **Wikipedia API** – for collecting and parsing Wikipedia articles
- **WordNet** – for lemmatization
- **Snowball** – for stopword filtering

## 🔁 Pipeline Overview

1. **Data Collection**
   - Fetch Wikipedia articles using the MediaWiki API
   - Label articles as geographic or non-geographic

2. **Text Preprocessing**
   - Tokenization
   - Stopword removal (Snowball)
   - Stemming (Porter) or Lemmatization (WordNet)

3. **Feature Extraction**
   - Bag of Words (BoW)
   - TF-IDF (optional)

4. **Model Training**
   - Naive Bayes
   - Logistic Regression (optional)

5. **Evaluation**
   - Accuracy, Precision, Recall, F1-score

6. **Deployment**
   - Code and documentation hosted on GitHub
   - Project description and pipeline included in this README

## 🚀 Getting Started

### Prerequisites

Install the required packages:

```bash
pip install -r requirements.txt
