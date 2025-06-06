import os
from preprocessing import TextPreprocessor
from utils import load_config, batch_preprocess
import pandas as pd


def main():
    # Get the project root directory
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Define paths using os.path.join for cross-platform compatibility
    config_path = os.path.join(PROJECT_ROOT,'src', 'configs', 'preprocessing_config.yaml')
    input_path = os.path.join(PROJECT_ROOT, 'data', 'wikipedia_dataset.csv')
    output_path = os.path.join(PROJECT_ROOT, 'data', 'processed_dataset.csv')

    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Load configuration
    config = load_config(config_path)

    # Initialize preprocessor with config
    preprocessor = TextPreprocessor()

    # Load data
    df = pd.read_csv(input_path)

    # Process text data
    df['processed_text'] = batch_preprocess(df['text'].tolist(), preprocessor)

    # Save processed data
    df.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")


if __name__ == "__main__":
    main()