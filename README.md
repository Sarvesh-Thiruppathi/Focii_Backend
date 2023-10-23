# Focii Backend
Backend for Focii: An Anti-Procrastination Chrome Extension.

## Requirements
* SciPy
* Transformers
* Flask
* NumPy
* PyTorch

## Installation

> pip install -r requirements.txt

## Usage

### Using with a server

We use these scripts on a VPS for the backend. Running the main.py script will start a Flask app that listens for a post request with two lists on the server, and returns a 1 or 0 depending on whether a website should be blocked.

### Using without a server
If you wish to run this without a server and flask, you can run block.py (or any other file) directly.
1. Create a new python file
2. Import block from block.py
3. Call block, you can exclude threshold, errorterm, and weight if you wish to use our optimized parameters 
    > block(list1, list2, threshold, errorterm, weight)

