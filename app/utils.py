import sys
import json

from pathlib import Path


def get_root() -> Path:
    """Get the root directory of the project."""
    return Path(__file__).parent.parent


def get_package_root() -> Path:
    """Get the root directory of the package."""
    return Path(__file__).parent


def get_venv_root() -> Path:
    """Get the root directory of the virtual environment."""
    return Path(sys.executable).parent
