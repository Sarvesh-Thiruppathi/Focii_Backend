# Source files

## block.py

This file concatenates the word embedding, similarity calculation, and threshold check.

Big thanks to Huggingface and sentence-transformers for providing all-mpnet-base-v2.

## embeddings.py

In this file, we take in some list of keywords or phrases and output a single tensor representing all embeddings of these keywords/phrases (averaging + linear transformation).

## similarity.py

This file takes in both the averaged embedding tensors representing the website keywords and the user keywords, and gets the cosine-similarity metric between them.

## check.py

This file checks if a webpage should be blocked given the outputted cosine-similarity metric from similarity.py and the blocking threshold.