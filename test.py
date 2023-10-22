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


with open("testdata.json", "+r") as f:
    data = json.load(f)

# initial trained parameters
threshold = 0.4748095893859863
et = 0.00024958481788635257

# returns false (0) is predicted properly
# returns true (1) is predicted improperly
def error(true, predicted):
    return not(true == predicted)

sr = []
for category in data.keys():
    keywords = data[category]["keywords"]
    for good in data[category]["1"]:
        predicted = block(keywords, good, threshold, et)
        sr.append(error(1, predicted))
    for bad in data[category]["0"]:
        predicted = block(keywords, bad, threshold, et)
        sr.append(error(0, predicted))
print(sr)
err = len([pred for pred in sr if pred==1])/len(sr)
print("Error", err)