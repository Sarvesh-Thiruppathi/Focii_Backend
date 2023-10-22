import json
from block import block
from random import random
from scipy import optimize

with open("traindata.json", "+r") as f:
    data = json.load(f)

# returns false (0) is predicted properly
# returns true (1) is predicted improperly
def error(true, predicted):
    return not(true == predicted)

def run(params):
    sr = []
    et, threshold = params
    print("et: ", et, "threshold: ", threshold)
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
    return err

initial_guess = [0.00024951171875, 0.47490234374999996]
result = optimize.minimize(run, initial_guess, method='Nelder-Mead')

if result.success:
    optimized_parameters = result.x[0]
    min_error = result.fun
    print(f"Optimized Parameter: {optimized_parameters}")
    print(f"Minimum Error: {min_error}")
else:
    print("Optimization failed.")

result = optimize.minimize(run, initial_guess, method='L-BFGS-B')

if result.success:
    optimized_parameters = result.x[0]
    min_error = result.fun
    print(f"Optimized Parameter: {optimized_parameters}")
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
    
