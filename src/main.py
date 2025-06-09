import os
from preprocessing import TextPreprocessor
from utils import load_config, batch_preprocess
import pandas as pd


def main():

    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


    config_path = os.path.join(PROJECT_ROOT,'src', 'configs', 'preprocessing_config.yaml')
    input_path = os.path.join(PROJECT_ROOT, 'data', 'wikipedia_dataset.csv')
    output_path = os.path.join(PROJECT_ROOT, 'data', 'processed_dataset.csv')


    os.makedirs(os.path.dirname(output_path), exist_ok=True)


    config = load_config(config_path)


    preprocessor = TextPreprocessor()


    df = pd.read_csv(input_path)


    df['processed_text'] = batch_preprocess(df['text'].tolist(), preprocessor)


    df.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")


if __name__ == "__main__":
    main()