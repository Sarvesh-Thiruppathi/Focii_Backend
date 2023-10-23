# Testing files

## optimize.py

We collected training data so that we could utilize **supervised learning** on the dataset and optimize our blocking threshold and the parameters of the linear transformation (weight and error term). 

Within SciPy, we use the **Nelder-Mead optimization method** (since we didn't have access to gradients), with our objective function being to minimize the amount of error with blocking classification. We found that by averaging the word embeddings, and optimizing the weight, error term, and blocking threshold on our training data, we were able to **reduce our classification error by 75%**.

### Usage

If you wish to optimize the parameters and threshold on your own training data, put your data in the format that we are using in dataset/traindata.json and replace "./dataset/traindata.json" in optimize.py with your data. You can choose the initial parameter values, or just leave at the default options. Then just run the optimize.py script and wait until it is finished.

## test.py

Used for testing our optimized parameters against the datasets.

## run.py

Used for testing our optimized parameters against specific keyword lists.