import torch

class Similarity():
    '''
    Takes in two word embedding tensors and calculates the cosine similarity score
    between them.
    '''
    def __init__(self):
        print("Calculating similarity")
    # Calculate the cosine similarity score between the two embedding tensors
    def calculate(self, tensor1: torch.Tensor, tensor2: torch.Tensor) -> torch.Tensor:
        similarity = torch.cosine_similarity(tensor1, tensor2)
        return similarity
