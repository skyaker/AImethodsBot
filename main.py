from transformers import pipeline

# Создание пайплайна для анализа тональности с использованием DistilBERT
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Пример использования
result = sentiment_analyzer("I love this product!")
print(result)
