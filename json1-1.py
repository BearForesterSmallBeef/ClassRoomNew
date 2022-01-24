import json
import pprint

name = "scoring.json"
dict_1 = dict()
with open(name) as json_file:
    for i in json.load(json_file)["scoring"]:
        for j in i["required_tests"]:
            dict_1[j] = i['points'] / len(i['required_tests'])
pprint.pprint(dict_1)
s = 0
for i in range(1, int(max(dict_1.keys())) + 1):
    test = input()
    if test.strip() == "ok" and i in dict_1.keys():
        s += dict_1[i]
print(int(s))