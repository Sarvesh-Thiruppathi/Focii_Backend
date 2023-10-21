import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from nltk.probability import FreqDist
import urllib.request

def tagVisible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True
def textFromHTML(url):
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)
    soup = BeautifulSoup(html, 'html.parser')
    texts = soup.findAll(text=True)
    visibletext = filter(tagVisible, texts)
    return u" ".join(t.strip() for t in visibletext)

url = 'https://classful.com/what-is-math-is-fun/'  # Replace with the URL of the webpage you want to scrape
response = requests.get(url)

if response.status_code == 200:
    html = response.text
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)

soup = BeautifulSoup(html, 'html.parser')

# Example: Extract text from all <p> elements
paragraphs = soup.findAll('p')
text = "\n".join([p.get_text() for p in paragraphs])

# Define a string containing all the punctuation marks
punctuation = string.punctuation

# Clean the text by removing punctuation
cleaned_text = ''.join([char for char in text if char not in punctuation])

# Tokenize the cleaned text
words = word_tokenize(cleaned_text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]

# Calculate word frequencies
fdist = FreqDist(filtered_words)
keywords = fdist.most_common(50)  # Get the top 10 keywords

print(keywords)


print(textFromHTML('https://classful.com/what-is-math-is-fun/'))

