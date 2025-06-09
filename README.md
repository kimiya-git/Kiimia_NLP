Wikipedia Text Classification: Geographic vs Non-Geographic

📌 Project Overview
This project classifies English Wikipedia texts into two categories:

Geographic (e.g., articles about countries, cities, rivers)

Non-Geographic (e.g., articles about people, events, concepts)

The pipeline combines NLP techniques and machine learning models to automate this classification.

🧠 Problem Statement
Given a Wikipedia article (English text), the system predicts its category:

Class 1: Geographic

Class 2: Non-Geographic

Key challenges include feature extraction, handling noisy text, and model interpretability.

🛠️ Technologies Used
Python 3.10+

NLTK – Tokenization, stopwords, stemming/lemmatization

scikit-learn – Naive Bayes, Logistic Regression, TF-IDF

Wikipedia API – Data collection

WordNet/Snowball – Text normalization

🔁 Pipeline Overview
1. Data Collection
Fetch articles using the MediaWiki API.

Manual labeling for training data.

2. Text Preprocessing
Tokenization, stopword removal , lemmatization.

3. Feature Extraction
TF-IDF representations.

4. Model Training

Logistic Regression

5. Evaluation
Metrics: Accuracy, Precision, Recall, F1-score.

Output: confusion_matrix.png for visualization.

6. Deployment
GitHub-hosted code with modular scripts (see Project Structure).

Klimia_NLP/  
├── data/                    # Raw and processed datasets  
├── configs/  
│   └── preprocessing_config.yaml  # Configuration for text cleaning  
├── src/  
│   ├── data.py             # Data loading/utils  
│   ├── preprocessing.py    # Text normalization  
│   ├── feature_extraction.py  # BoW/TF-IDF implementation  
│   ├── model.py            # ML models (Naive Bayes)  
│   ├── prediction_pipeline.py  # End-to-end inference  
│   └── utils.py            # Helper functions  
├── model.pkl               # Serialized trained model  
├── main.py                 # Entry point for training/evaluation  
└── requirements.txt        # Dependencies (pip install -r requirements.txt)

Task 2: Extended Assignment
Klimia_NLP/assignment2/     # Additional experiments or secondary tasks  

🚀 Getting Started
1. Install dependencies:
pip install -r requirements.txt  

2. Run the pipeline:

python main.py  # preprocess the input files

python model.py   # Trains model and saves outputs 

python prediction_pipeline.py   # given a sample text if classifies
