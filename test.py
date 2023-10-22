# TESTNG FOR WORD SIMILARITY
from block import block

testkeywords = [["math", "site", "class", "examples", "quiz"],
                    ["beach", "volleyball", "sports", "among us"],
                    ["soccer", "messi", "fifa", "score", "goals", "crowd", "brazil"]]
testinputs = [["calculus", "math", "vector", "derivatives", "parametric equations"],
              ["soccer", "sports", "shot", "nike", "home"]]

for inputs in testinputs:
    for keywords in testkeywords:
        print("Testing for \n", inputs, keywords)
        block(inputs, keywords, threshold=0.5)