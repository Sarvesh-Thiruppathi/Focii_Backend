# TESTNG FOR WORD SIMILARITY
from block import block
import json

# testkeywords = [["math", "site", "class", "examples", "quiz"],
#                     ["beach", "volleyball", "sports", "among us"],
#                     ["soccer", "messi", "fifa", "score", "goals", "crowd", "brazil"]]
# testinputs = [["calculus", "math", "vector", "derivatives", "parametric equations"],
#               ["soccer", "sports", "shot", "nike", "home"]]

# for inputs in testinputs:
#     for keywords in testkeywords:
#         print("Testing for \n", inputs, keywords)
#         block(inputs, keywords, threshold=0.5)


with open("data.json", "+r") as f:
    data = json.load(f)

threshold = 0.5
et = 0

for category in data.keys():
    keywords = data[category]["keywords"]
    for good in data[category]["1"]:
        block(keywords, good, threshold, et)
    for bad in data[category]["0"]:
        block(keywords, bad, threshold, et)