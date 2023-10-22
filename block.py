from embeddings import Embeddings
from similarity import Similarity
from check import Check
import numpy as np

def block(keywords, site, threshold, et) -> bool:
    print("Site keywords", site, "User Keywords", keywords, "Threshold", threshold)
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
    keyword2 = embed.getEmbeddings2(keywords, et)
    site2 = embed.getEmbeddings2(site, et)

    # Get similarity scores
    cossim2 = similarity.calculate2(keyword2, site2)

    # Check if webpage is good
    isGood = Check(cossim2, threshold).check()

    return isGood