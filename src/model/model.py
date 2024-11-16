from transformers import pipeline
from config import MODEL_PATH, USE_GPU

class SentimentModel:
  def __init__(self):
    """
    Инициализация модели и токенизатора
    """

    if USE_GPU:
      device = 0
    else:
      device = -1

    self.pipeline = pipeline("sentiment-analysis", model = MODEL_PATH, tokenizer = MODEL_PATH, device = device)
    
  def analyze_sentiment(self, text: str):
    """
    Выполняет анализ тональности для заданного текста

    :param test: Входной текст для анализа
    :return: Результаты анализа
    """

    result = self.pipeline(text)

    return result