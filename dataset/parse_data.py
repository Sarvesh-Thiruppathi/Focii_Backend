import json
import os
from ast import literal_eval

root = "./"

dir = os.listdir("./")

files = {}
data = {}

for i in range(1,8):
    files[i] = os.listdir(root+f"{i}/")
    data[i] = {"keywords":[], "1":[], "0":[]}

for i in files.keys():
    for file in files[i]:
        with open(f'{i}/{file}') as f:
            lines = []
            for line in f:
                line = literal_eval(line)
                data[i]["keywords"] = line["keywordInput"]
                if file == "good.txt":
                    data[i]["1"].append(line["keywordWebsite"])
                if file == "bad.txt":
                    data[i]["0"].append(line["keywordWebsite"])

with open("traindata.json", "w") as f:
    json.dump(data, f)