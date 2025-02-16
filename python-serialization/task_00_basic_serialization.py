#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Save a dictionary as a JSON file.
    Overwrites the file if it exists.
    """
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def load_and_deserialize(filename):
    """
    Load JSON data from a file into a dictionary.
    """
    with open(filename, "r") as file:
        return json.load(file)
