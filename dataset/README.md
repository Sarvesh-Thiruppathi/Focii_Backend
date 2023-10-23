# Dataset

## "faux" files

All of the files prefixed with "faux" were ChatGPT generated files which were used for the initial optimization of our algorithm parameters.

## 1-7 data folders

One of our team members manually went through multiple "good" and "bad" sites in order to scrape keywords from the site as training data. He went through 7 different "categories" of browsing, and put the bad and good sites into 7 different folders.

## parse_data.py

This is the file that we used in order to parse the 1-7 folders and output to traindata.json. In traindata.json, for each different category (1-7), "1" corresponds to good site keywords, and "0" corresponds to bad site keywords.
