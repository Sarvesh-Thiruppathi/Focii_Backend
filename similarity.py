import torch

class Similarity():
    '''
    Takes in two word embedding tensors and calculates the cosine similarity score
    between them.
    '''
    def __init__(self):
        print("Calculating similarity")
    # Given an average of all word embeddings for website and user keywords
    # compare the similarity average embedding representation
    def calculate(self, tensor1: torch.Tensor, tensor2: torch.Tensor) -> torch.Tensor:
        similarity = torch.cosine_similarity(tensor1, tensor2, dim=0)
        return similarity