import toml
from pathlib import Path

def load_config():
    config_dir = Path(__file__).parent.parent
    return toml.load(config_dir / "config.toml")
