from .constants import BACKEND_ROOT
from .utils import display_fatal_error
from yaml import safe_load
from typing import TypedDict

config_path = BACKEND_ROOT / "config.yml"

if not config_path.exists():
    display_fatal_error(f"Config file does not exist! Make sure {config_path.absolute()} exists.")

try:
    with open(config_path) as f:
        config_text = f.read()
except Exception as e:
    display_fatal_error(f"Error reading config file: {e}. Make sure that the executing user has the permissions to read the config file.")

class ConfigStructure(TypedDict):
    """The structure of the config."""
    db: str

config: ConfigStructure = safe_load(config_text)