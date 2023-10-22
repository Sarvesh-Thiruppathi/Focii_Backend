import numpy as np

class Check():
    '''
    ## Check if a webpage should be blocked.

    ### Inputs
    -----------
    cossim (list): list of cosine similarity scores
    threshold (int): threshold to block webpage
    '''
    def __init__(self, cossim: list, threshold: int):
        self.cossim = cossim
        self.threshold = threshold
        print("Checking if webpage is good")
    def check(self) -> bool:
        cossim = np.array(self.cossim)
        print("Cossim: ", np.mean(cossim))
        if np.mean(cossim) > self.threshold:
            return True
        return False