import json


name = "scoring.json"
with open(name) as json_file:
    print(json.load(json_file))
