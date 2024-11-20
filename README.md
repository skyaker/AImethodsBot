# Requirements

Conda - [installation guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

# How to Use

1. **Initialize Environment:** Follow the steps in "Launch" to set up the environment.
2. **Prepare Data:** Place your dataset in `src/model/data/` and preprocess it with `src/model/preprocessing.py`.
3. **Tune the Model (Optional):** If you need to fine-tune the model, run `src/model/training.py`.
4. **Run the Bot:** Use `python main.py` to launch the bot.

# Preparation

1. Conda environment initialization
```shell
chmod +x ./init_conda.sh && ./init_conda.sh
```

2. Terminal restart
```shell
exec zsh
```

3. Environment activation and dependancies installation
```shell
conda activate bot_venv

chmod +x ./build.sh && ./build.sh
```

4. Place the .env file with token in `src/bot`
```
BOT_TOKEN = here_is_bot_token
```

# Model tuning

Bot based on multilingual XLM-roBERTa-base model.

## Required data structure:
```json
{
  "text": ["I love this product!", "This is the worst experience ever.", "It was okay, nothing special."],
  "label": [2, 0, 1]
}
```
Where: 0 - negative, 1 - neutral, 2 - positive.

## Tuning start

```shell
python src/model/training.py
```

## Data preprocessing

The parser expects data in the following format:

```json
[
  {
    "text": "I hate this product!", 
    "id": 1945, 
    "sentiment": "negative"
  },
  {
    "text": "I love this product!", 
    "id": 1957, 
    "sentiment": "positive"
  },
  {
    "text": "It was okay, nothing special.", 
    "id": 1967, 
    "sentiment": "positive"
  }
]
```

Place your dataset file in the `src/model/data/` directory under the name **preparsed_train_data.json**.

To preprocess this file into the format required by the Hugging Face framework, run:

```shell
python src/model/preprocessing.py
```

The output file will be saved as **train_data.json** in the same directory.