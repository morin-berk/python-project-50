import json
import os
import yaml


def parse_file(file):
    file_extension = os.path.splitext(file)[1]
    file_path = os.path.abspath(file)
    if file_extension == ".yml" or file_extension == ".yaml":
        file_data = parse_yaml_files(file_path)
        lowered_data = to_lower(file_data)
        return lowered_data
    elif file_extension == ".json":
        file_data = parse_json_files(file_path)
        lowered_data = to_lower(file_data)
        return lowered_data
    else:
        raise ValueError("File extension should be .yaml, .yml or .json")


def parse_yaml_files(file_path):
    with open(file_path) as file:
        return yaml.safe_load(file)


def parse_json_files(file_path):
    with open(file_path) as file:
        return json.load(file)


def to_lower(data):
    lowered_values = {k: str(v).lower() for k, v in data.items()}
    return lowered_values
