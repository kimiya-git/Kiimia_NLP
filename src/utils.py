import yaml
from typing import List

def load_config(config_path: str) -> dict:
    """Load preprocessing configuration"""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def batch_preprocess(texts: List[str], preprocessor) -> List[str]:
    """Process a batch of texts"""
    return [preprocessor.full_preprocess(text) for text in texts]