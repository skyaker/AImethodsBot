import json
from model import SentimentModel 
from sklearn.metrics import classification_report
from config_loader import load_config

def load_test_data(file_path):
  """
  Загружает тестовый датасет из файла JSON.
  :param file_path: Путь к тестовому файлу.
  :return: Список примеров с текстом и метками.
  """
  with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)
  return data

def evaluate_model(model, test_data):
  """
  Тестирует модель на заданном наборе данных и выводит результаты.
  """
  true_labels = []
  predicted_labels = []

  label_translation = {
    "позитивный": "positive",
    "нейтральный": "neutral",
    "негативный": "negative"
  }

  for example in test_data:
    text = example["text"]
    true_label = example["label"]
    
    if true_label not in label_translation:
      print(f"Unknown true label: {true_label}")
      continue
    
    true_labels.append(true_label)
    
    result = model.analyze_sentiment(text)
    if result and "label" in result[0]:
      predicted_labels.append(result[0]["label"])
    else:
      print(f"No prediction for text: {text}")
  
  if not true_labels or not predicted_labels:
    print("No data for evaluation. Check your test dataset or model predictions.")
    return

  print("\nClassification Report:")
  print(classification_report(
    true_labels,
    predicted_labels,
    labels=["позитивный", "нейтральный", "негативный"],
    target_names=["позитивный", "нейтральный", "негативный"],
    zero_division=1
  ))


if __name__ == "__main__":
  config = load_config()

  test_data_path = config["data"]["test_data_path"]

  test_data = load_test_data(test_data_path)

  sentiment_model = SentimentModel()

  evaluate_model(sentiment_model, test_data)