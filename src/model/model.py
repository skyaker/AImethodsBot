from transformers import pipeline
import os
import sys

sys.path.append(os.path.dirname(__file__))

from config_loader import load_config

config = load_config()

class SentimentModel:
  def __init__(self):
    """
    Model initialization
    """

    if config["model"]["use_gpu"]:
      device = 0
    else:
      device = -1

    if config["model"]["use_tuned"]:
      MODEL_PATH = config["model"]["tuned"]["model_path"]
    else:
      if config["model"]["use_ru"]:
        MODEL_PATH = config["model"]["ru_model"]["model_path"]
      else:
        MODEL_PATH = config["model"]["pretrained"]["model_path"]

    self.pipeline = pipeline("sentiment-analysis", model = MODEL_PATH, tokenizer = MODEL_PATH, device = device)
    
  def analyze_sentiment(self, text: str):
    """
    Analyze sentiment by entered text

    :param text: input text
    :return: result of analyze with translated labels
    """

    result = self.pipeline(text)
    label_translation = {
      "positive": "позитивный",
      "neutral": "нейтральный",
      "negative": "негативный"
    }

    for res in result:
      res["label"] = label_translation.get(res["label"], res["label"])

    return result