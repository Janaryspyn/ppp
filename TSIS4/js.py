import json
with open("sample-data.json", "r") as json_file:
    x = json.load(json_file)
print(x)