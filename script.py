
import requests
import string
import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

r = requests.get('https://medium.com/@jalajpunn/the-struggle-against-the-present-8a3b0a6123c8')
soup = BeautifulSoup (r.content,features="html5lib")

text = [''.join(s.findAll(text=True)) for s in soup.findAll('p')]
s = ''.join(text)

stopwords = set(stopwords.words('english'))

words = nltk.word_tokenize(s)
words = [word.lower() for word in words if word.isalpha()]

noStopWords = [w for w in words if not w in stopwords]

print(noStopWords)