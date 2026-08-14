from pathlib import Path
import tomllib

PROJECT_ROOT = Path(__file__).resolve().parents[1]  # resolve resolves all the ..
DB_PATH = PROJECT_ROOT / "data" / "tables.db"
CONFIG_PATH = PROJECT_ROOT / "config.toml"

with open(CONFIG_PATH, "rb") as f:  # with is a context manager it ensures it gets closed even with error
    config = tomllib.load(f)

RED = config['colors']['RED'].encode().decode('unicode_escape')
GREEN = config['colors']['GREEN'].encode().decode('unicode_escape')
RESET = config['colors']['RESET'].encode().decode('unicode_escape')