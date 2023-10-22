import torch

class Similarity():
    '''
    Takes in two word embedding tensors and calculates the cosine similarity score
    between them.
    '''
    def __init__(self):
        print("Calculating similarity")
    # Method 1: Calculate the cosine similarity score between the two embedding tensors
    #           for each word embedding
    def calculate1(self, tensor1: torch.Tensor, tensor2: torch.Tensor) -> torch.Tensor:
        similarity = []
        for item in tensor1:
            for otheritem in tensor2:
                similarity.append(torch.cosine_similarity(item, otheritem, dim=0))

        return similarity
    # Method 2: Given an average of all word embeddings for website and user keywords
    #           compare the similarity average embedding representation
    def calculate2(self, tensor1: torch.Tensor, tensor2: torch.Tensor) -> torch.Tensor:
        similarity = torch.cosine_similarity(tensor1, tensor2, dim=0)
        return similarity