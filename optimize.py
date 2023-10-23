import json
from block import block
from random import random
from scipy import optimize

with open("combined.json", "+r") as f:
    data = json.load(f)

# returns false (0) is predicted properly
# returns true (1) is predicted improperly
def error(true, predicted):
    return not(true == predicted)

def run(params):
    sr = []
    et, threshold, weight = params
    print("et: ", et, "threshold: ", threshold, "weight: ", weight)
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
    return err

# initial_guess = [0.0002138523356119792, 0.5946003046035769, 1.036111111111111]
initial_guess = [0, 0.5, 1]
result = optimize.minimize(run, initial_guess, method='Nelder-Mead')
# Results on traindata.json
# et: 0.00020584716796875002
# threshold:  0.6647705268859867
# Minimum Error: 0.017857142857142856

# with weight (traindata)
# et:  0.0002058572190999985 threshold:  0.6647380673876035 weight:  1.000048828125

# with weight (testdata_sep_words)
#Error 0.0625
# Optimized Parameter:  [0.0002138523356119792, 0.5946003046035769, 1.036111111111111]

if result.success:
    optimized_parameters = result.x
    min_error = result.fun
    print(f"Optimized Parameter: ", [parameter for parameter in optimized_parameters])
    print(f"Minimum Error: {min_error}")
else:
    print("Optimization failed.")

# i = 0
# while (i < iterations or error > 0.1):
#     i += 1
#     print("iteration: ", i)
#     print("et", et)
#     for category in data.keys():
#         keywords = data[category]["keywords"]
#         for good in data[category]["1"]:
#             predicted = block(keywords, good, 0.5, et)
#             sr.append(error(1, predicted))
#         for bad in data[category]["0"]:
#             predicted = block(keywords, bad, 0.5, et)
#             sr.append(error(0, predicted))
#     curr_err = len([pred for pred in sr if pred==1])/len(sr)
#     print("Error: ", curr_err)
#     et += lr
    
