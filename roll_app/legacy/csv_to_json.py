import json

filepath = "../test_data/modifier_keyes.csv"

with open(filepath, "r") as f:
    data = f.readlines()

data = data[1:]

for index, i in enumerate(data):
    i = i.split(",")
    i[1].strip("\n")
    i[0], i[1] = int(i[0]), int(i[1])
    data[index] = i


data = dict(data)

with open("../test_data/modifier_keyes.json", "w") as f:
    json.dump(data, f)

print(data)
