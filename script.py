import sys
import requests
import string
import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

def getContent():
	r = requests.get(sys.argv[1]) #Request for user specific web page
	soup = BeautifulSoup(r.content,features="html5lib") #BeautifulSoup used for scraping text from HTML

	#Need to clean the content

	article = [''.join(s.findAll(text=True)) for s in soup.findAll('p')]
	article = ''.join(article)

	#Will analyze and display various observations

	displayStopWords(article)

def displayStopWords(article):
	allStopwords = set(stopwords.words('english'))

	#Tokenizing the words present in article/removing punctuation
	words = nltk.word_tokenize(article)
	words = [word.lower() for word in words if word.isalpha()]

	stopwordsUsed = [w for w in words if w in allStopwords]
	fdist = nltk.FreqDist(stopwordsUsed)
	

getContent()