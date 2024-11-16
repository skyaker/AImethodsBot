import os
from typing import Optional

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
TRAIN_DATA_PATH = os.path.join(DATA_DIR, 'train_data.json')
TEST_DATA_PATH = os.path.join(DATA_DIR, 'test_data.json')

MODEL_PATH: str = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
USE_GPU: bool = False

BATCH_SIZE: int = 16
EPOCHS: int = 3
LEARNING_RATE: float = 2e-5

MAX_SEQ_LENGTH: int = 128

# BOT_TOKEN: str = 

# LOGGING_LEVEL: str = "INFO"
# LOG_FILE