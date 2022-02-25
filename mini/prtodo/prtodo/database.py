"""This module provides the PR To-Do database functionality."""
# prtodo/database.py

import configparser
from io import DEFAULT_BUFFER_SIZE
from pathlib import Path

from prtodo import DB_WRITE_ERROR, SUCCESS

DEFAULT_DB_FILE_PATH = Path.cwd().joinpath("." + Path.home().stem + "_prtodo.json")


def get_database_path(config_file: Path) -> Path:
    """Return the current path to the to-do database."""
    config_parser = configparser.Configparser()
    config_parser.read(config_file)
    return Path(config_parser["General"]["database"])


def init_database(db_path: Path) -> int:
    """Create the to-do database."""
    try:
        db_path.write_text("[]")  # Empty to-do list
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR
