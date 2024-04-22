import os
import glob
from pathbuilder_dict import get_character
import json

path = "test_data\\characters"

data = []

for filename in glob.glob(os.path.join(path, "*.txt")):
    with open(os.path.join(os.getcwd(), filename), "r") as f:
        stats = f.read()
        stats = json.loads(stats)
        print(type(stats))
        char = get_character(stats)
        data.append(char)

print(data)
