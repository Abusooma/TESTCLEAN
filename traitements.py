from pathlib import Path
import re


def cleaner(char):
    return re.sub(r'[^a-zA-Z\s]', "", char)


def read_name(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]


def write_clean_names(output_file, names):
    with open(output_file, "w") as f:
        return f.write("\n".join(names))
