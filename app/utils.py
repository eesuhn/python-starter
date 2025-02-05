import json
import inspect
import csv

from colorama import Back
from pathlib import Path
from datetime import datetime


def get_package_root() -> Path:
    return Path(__file__).parent


def get_current_time() -> str:
    """
    Returns the current time in the format `MMDD_HHMMSS`
    """
    return datetime.now().strftime("%m%d_%H%M%S")


def print_json(
    data: dict
) -> None:
    print(json.dumps(data, indent=2))


def log_json(
    data: dict,
    filename: str,
    dest: str = "logs"
) -> None:
    path = get_package_root() / dest
    filename = f"{filename}_{get_current_time()}.json"
    with open(path / f"{filename}", "w", encoding="utf-8") as f:
        f.write(json.dumps(data, indent=2))
    print_success(f"Logged to {path / filename}")


def log_csv(
    data: list,
    filename: str,
    dest: str = "logs"
) -> None:
    path = get_package_root() / dest
    filename = f"{filename}_{get_current_time()}.csv"
    with open(path / f"{filename}", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print_success(f"Logged to {path / filename}")


def open_json(
    filename: str,
    dest: str = "logs"
) -> dict:
    path = get_package_root() / dest
    with open(path / f"{filename}", "r", encoding="utf-8") as f:
        return json.load(f)


def open_csv(
    filename: str,
    dest: str = "logs"
) -> list:
    path = get_package_root() / dest
    with open(path / f"{filename}", "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        return list(reader)


def get_func_name() -> str:
    return inspect.currentframe().f_back.f_code.co_name


def print_error(
    m: str
) -> None:
    print(f"{Back.RED}ERROR{Back.RESET} {m}")


def print_warning(
    m: str
) -> None:
    print(f"{Back.YELLOW}WARNING{Back.RESET} {m}")


def print_success(
    m: str
) -> None:
    print(f"{Back.GREEN}SUCCESS{Back.RESET} {m}")


def print_info(
    m: str
) -> None:
    print(f"{Back.MAGENTA}INFO{Back.RESET} {m}")
