# File responsible for validating and writing to JSON file

import os
import json

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

# Used to append to file
def append_file(input):
    with open(path, "a") as f:
        json.dump(input, f, indent=4)