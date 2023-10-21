from embeddings import Embeddings
from similarity import Similarity
from check import Check

def main() -> bool:
    print("Hello")

    # Get embeddings
    embed = Embeddings("sentence-transformers/all-mpnet-base-v2")
    input = embed.getEmbeddings(["seventeen"])
    keyword = embed.getEmbeddings(["calculus", "math", "vector", "beach", "david"])
    print(input.shape)
    print(keyword.shape)

    # Get similarity scores
    similarity = Similarity()
    cossim = similarity.calculate(input, keyword)

    # Check if webpage is good
    threshold = 0.4
    isGood = Check(cossim, threshold).check()

    return isGood

if __name__ == "__main__":
    main()