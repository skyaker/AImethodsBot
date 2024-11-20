from pathlib import Path
import yaml

BASE_DIR = Path(__file__).resolve().parent
CONFIG_FILE = BASE_DIR / "config.yaml"    

def load_config():
  """
  yaml configuration load
  """
  with CONFIG_FILE.open("r") as f:
    config = yaml.safe_load(f)

  if "data" in config:
    for key, value in config["data"].items():
      if isinstance(value, str) and not Path(value).is_absolute():
        config["data"][key] = str(BASE_DIR / value)

  return config