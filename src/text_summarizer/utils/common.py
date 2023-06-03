import os

from box.exceptions import BoxException
import yaml
from text_summarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def readyaml(path_to_yaml : Path) -> ConfigBox:
    """Reads yaml file"""
    try:
        with open(path_to_yaml, 'r') as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        raise BoxException(f"File {path_to_yaml} not found")
    except yaml.YAMLError as e:
        raise BoxException(f"Error reading file {path_to_yaml}: {e}")
    return ConfigBox(config)