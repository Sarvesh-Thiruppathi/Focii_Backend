# TESTNG FOR WORD SIMILARITY
import sys
sys.path.append('../')
from src.block import block
import json

with open("../dataset/faux_testdata_sep-words.json", "+r") as f:
    data = json.load(f)

# initial trained parameters
# threshold = 0.4748095893859863
# et = 0.00024958481788635257

# second trained parameters
# threshold = 0.6648632812500004
# et = 0.00020565223693847659

# # # third train parameters
# threshold = 0.6647705268859867
# et = 0.00020584716796875002
# weight = 1

# # fourth train parameters ("testdata_sep-words.json")
# threshold = 0.5750976562499998
# et = -0.000375
# weight = 1

# threshold = 0.7
# et = 0

# et = 0.0002138523356119792
# # et = 0
# threshold = 0.5946003046035769
# # threshold = 0.64
# weight = 1.036111111111111
# weight = 1

# fifth train parameters (combined.json)
# et = -1.6289437585733984e-06
# threshold = 0.6080418381344306
# weight = 0.9576646090534982
# et = 0
# threshold = 0.5
# weight = 1

# sixth train parameters (traindata.json) --> TOP PICK
et = 0.0001475765889346136
threshold = 0.6110711019661632
weight = 0.8563443072702338

# returns false (0) is predicted properly
# returns true (1) is predicted improperly
def error(true, predicted):
    return not(true == predicted)

sr = []
for category in data.keys():
    keywords = data[category]["keywords"]
    for good in data[category]["1"]:
        predicted = block(keywords, good, threshold, et, weight)
        sr.append(error(1, predicted))
    for bad in data[category]["0"]:
        predicted = block(keywords, bad, threshold, et, weight)
        sr.append(error(0, predicted))
print(sr)
err = len([pred for pred in sr if pred==1])/len(sr)
print("Error", err)