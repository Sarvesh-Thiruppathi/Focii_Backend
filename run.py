from block import block

# initial trained parameters
threshold = 0.4748095893859863
et = 0.00024958481788635257

keywords = ["economics", "graphs", "budget line", "constraint", "dead-weight loss"]
badkeywords = ["bed", "mattress", "sleep", "number", "beds"]
site = ["economics", "courses", "financial", "theory", "Babson"]
summary = []

print(block(keywords, site, threshold, et))