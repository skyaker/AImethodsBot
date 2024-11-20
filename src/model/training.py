import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset, DatasetDict
import json
import os
import sys

sys.path.append(os.path.dirname(__file__))

from config_loader import load_config

config = load_config()

def load_data():
  """
  Loads training data

  :return: DatasetDict with splitted train and test data
  """
  train_data = config["data"]["train_data_path"]
  with open(train_data, "r", encoding="utf-8") as file:
    parsed_data = json.load(file)

  dataset = Dataset.from_dict(parsed_data)

  dataset = dataset.train_test_split(test_size=0.2)
  return dataset

def train_model(dataset):
  """
  Training model, creates tuned model

  :param output_dir: path for new model
  """
  model_name = config["model"]["pretrained"]["model_path"]
  output_dir = config["model"]["tuned"]["model_path"]

  tokenizer = AutoTokenizer.from_pretrained(model_name)
  model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)

  def tokenize_function(examples):
    return tokenizer(examples["texts"], padding="max_length", truncation=True, max_length=128)

  tokenized_dataset = dataset.map(tokenize_function, batched=True)

  tokenized_dataset = tokenized_dataset.rename_column("labels", "label")
  tokenized_dataset.set_format("torch")

  training_args = TrainingArguments(
    output_dir=output_dir,
    eval_strategy=config["training"]["eval_strategy"],
    save_strategy=config["training"]["save_strategy"],  
    learning_rate=config["training"]["learning_rate"],
    per_device_train_batch_size=config["training"]["per_device_train_batch_size"],
    per_device_eval_batch_size=config["training"]["per_device_eval_batch_size"],
    num_train_epochs=config["training"]["num_train_epochs"],
    weight_decay=config["training"]["weight_decay"],
    save_total_limit=config["training"]["save_total_limit"],
    logging_dir=config["training"]["logging_dir"],
    load_best_model_at_end=True,
  )

  trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["test"],
  )

  trainer.train()

  model.save_pretrained(output_dir)
  tokenizer.save_pretrained(output_dir)

if __name__ == "__main__":
  dataset = load_data()
  train_model(dataset)
  print(f"New model saved in {config["model"]["tuned"]["model_path"]}")