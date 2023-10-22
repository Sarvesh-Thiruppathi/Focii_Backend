from embeddings import Embeddings
from similarity import Similarity
from check import Check
import numpy as np

def block(keywords: list, site: list, threshold=0.00024951171875, et=0.47490234374999996) -> bool:
    # Get embeddings
    embed = Embeddings("sentence-transformers/all-mpnet-base-v2")

    similarity = Similarity()

    # # Method 1: double iterate
    # print("\nMethod 1\n---------------------\n")
    # keyword1 = embed.getEmbeddings1(keywords)
    # site1 = embed.getEmbeddings1(site)

    # # Get similarity scores
    # cossim1 = similarity.calculate1(keyword1, site1)

    # # Check if webpage is good
    # isGood = Check(cossim1, threshold).check()

    # print(isGood)
   
    # Method 2: average word embeddings
    keyword = embed.getEmbeddings2(keywords, et)
    site = embed.getEmbeddings2(site, et)

    # Get similarity scores
    cossim = similarity.calculate2(keyword, site)

    # Check if webpage is good
    isGood = Check(cossim, threshold).check()

    return isGood