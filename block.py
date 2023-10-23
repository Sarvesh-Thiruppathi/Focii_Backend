from embeddings import Embeddings
from similarity import Similarity
from check import Check
import numpy as np

def block(keywords: list, site: list, threshold=0.6647705268859867, et=0.00020584716796875002, weight=1) -> bool:
    # Get embeddings
    embed = Embeddings("sentence-transformers/all-mpnet-base-v2")
   
    #Get average word embeddings
    keyword = embed.getEmbeddings(keywords, et, weight)
    site = embed.getEmbeddings(site, et, weight)

    # Get similarity scores
    similarity = Similarity()
    cossim = similarity.calculate(keyword, site)

    # Check if webpage is good
    isGood = Check(cossim, threshold).check()

    return isGood