import json
import os
import sys

sys.path.append(os.path.dirname(__file__))

from config_loader import load_config

config = load_config()

def parse_training_data(sentiment_map):
  """
  Parsing training data

  :param sentiment_map: dictionary with sentiment num equalation
  """
  input_file = config["data"]["preparsed_data_path"]
  output_file = config["data"]["train_data_path"]

  with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)

  texts = [entry["text"] for entry in data]
  labels = [sentiment_map[entry["sentiment"]] for entry in data]

  parsed_data = {"texts": texts, "labels": labels}

  with open(output_file, "w", encoding="utf-8") as outfile:
    json.dump(parsed_data, outfile, ensure_ascii=False, indent=4)

if __name__ == "__main__":
  sentiment_map = {"negative": 0, "neutral": 1, "positive": 2}

  parse_training_data(sentiment_map)
  print(f"Parsed data saved in {config["data"]["train_data_path"]}")