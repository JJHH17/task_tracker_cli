# File responsible for validating and writing to JSON file

import os
import json
from pathlib import Path

# Checking whether file exists or not
path = "./tasks.json"

# Used to check if file exists
def check_file():
    if not os.path.exists(path):
        with open(path, "w") as f:
            pass  # Creates the file
        print("File created.")

# Used to write to file
def write_file(input):
    with open(path, "w") as f:
        f.write(input)

# Used to read file
def read_file():
    with open(path, "r") as f:
        print(f.read())

# Parses file into list
def feed_file():
    path = Path("tasks.json") # File path for JSON

    if not path.exists() or path.stat().st_size == 0:
        return []  # Return empty list if file doesn't exist or is empty

    try:
        with path.open("r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Warning: JSON file is corrupt or empty. Starting fresh.")
        return []


# Used to append to file
def append_file(input):
    with open(path, "w") as f:
        json.dump(input, f, indent=4)