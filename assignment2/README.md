# Text Style-Adaptive Summarization System

A Python-based NLP system that generates summaries of content text while adapting to the writing style of a provided style text. The system implements hierarchical summarization to handle texts longer than the context window limit.

## Features

- **Style Analysis**: Extracts writing style characteristics (sentence length, vocabulary, POS patterns)
- **Adaptive Summarization**: Produces content summaries that match the style text's characteristics
- **Hierarchical Processing**: Handles long documents through recursive summarization
- **Query Generation**: Creates prompts 
- 
## File Structure

NLP_kimia/
│
├── venv/ # Virtual environment (should be in .gitignore)
│
├── Kiimia_NLP/
│ └── assignment2/
│ ├── data_assignment2/ # Additional data files
│ ├── content_text.txt # Input content text
│ ├── style_text.txt # Input style text
│ ├── styled_summary.txt # Generated output
│ └── query.txt # Generated LLM query
│
└── summarizer/ # Main code package
├── init.py # Package initialization
├── preprocess.py # Text preprocessing
├── summarize.py # Summarization algorithms
├── utils.py # Utility functions
└── main.py # Main execution script

## Usage :
Place your input files in Kiimia_NLP/assignment2/:

content_text.txt: Text to summarize

style_text.txt: Style to emulate

Run the summarizer:

python -m summarizer.main

Output files will be created in the data_assigment2 directory:

styled_summary.txt: Style-adapted summary

query.txt: Formatted  prompt

## Configuration
Edit these files as needed:

summarizer/main.py: Change context window size (default: 4000 tokens)

summarizer/summarize.py: Adjust summary length parameters


## Example Workflow :
Add your content to Kiimia_NLP/assignment2/content_text.txt

Add style reference to Kiimia_NLP/assignment2/style_text.txt

Run the program

Check results in:

styled_summary.txt

query.txt