from src.embeddings import Embeddings
from src.similarity import Similarity
from src.check import Check

def block(keywords: list, site: list, threshold=0.6110711019661632, et=0.0001475765889346136, weight=0.8563443072702338) -> bool:
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