from transformers import pipeline
from src.model.model import SentimentModel

def main():
  model = SentimentModel()
  text = "фджлывджфлыажфдылва"
  sentiment = model.analyze_sentiment(text)
  print(f"{sentiment}")

if __name__ == "__main__":
  main()