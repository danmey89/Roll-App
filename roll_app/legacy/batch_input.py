import os
import glob
from functions import parse_character
import json

SOURCE = "data/characters"


def update_characters(source=SOURCE):
    data = []

    for filename in glob.glob(os.path.join(source, "*.txt")):
        with open(os.path.join(os.getcwd(), filename), "r") as f:
            stats = f.read()
            stats = json.loads(stats)
            char = parse_character(stats)
            data.append(char)

    with open("../data/all_characters.json", "w") as f:
        json.dump(data, f)
