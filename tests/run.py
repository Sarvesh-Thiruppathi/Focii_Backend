import sys
sys.path.append('../')
from src.block import block

keywords = ["economics", "graphs", "budget line", "constraint", "dead-weight loss"]
badkeywords = ["bed", "mattress", "sleep", "number", "beds"]
site = ["economics", "courses", "financial", "theory", "Babson"]

print(block(keywords, site))