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


