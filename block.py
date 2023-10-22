from embeddings import Embeddings
from similarity import Similarity
from check import Check
import numpy as np

def block(input, keywords, threshold) -> bool:
    # Get embeddings
    embed = Embeddings("sentence-transformers/all-mpnet-base-v2")

    similarity = Similarity()

    # Method 1: double iterate
    print("\nMethod 1\n---------------------\n")
    input1 = embed.getEmbeddings1(input)
    keyword1 = embed.getEmbeddings1(keywords)

    # Get similarity scores
    cossim1 = similarity.calculate1(input1, keyword1)

    # Check if webpage is good
    isGood = Check(cossim1, threshold).check()

    print(isGood)
   
    # Method 2: average word embeddings
    print("\nMethod 2\n---------------------\n")
    input2 = embed.getEmbeddings2(input)
    keyword2 = embed.getEmbeddings2(keywords)

    # Get similarity scores
    cossim2 = similarity.calculate2(input2, keyword2)

    # Check if webpage is good
    isGood = Check(cossim2, threshold).check()

    print(isGood)

    return isGood