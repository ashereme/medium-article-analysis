import sys
import requests
import string
import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

def getContent():
	
	try:
		r = requests.get(sys.argv[1]) #Request for user specific web page
	except:
		print("This script requires a medium article URL!")
		sys.exit(1)
	
	soup = BeautifulSoup(r.content,features="html5lib") #BeautifulSoup used for scraping text from HTML

	#Need to clean the content
	article = [''.join(s.findAll(text=True)) for s in soup.findAll('p')]
	article = ''.join(article)

	#Remove punctuation and tokenize
	onlyWords = removePunctuation(article)

	#Possible part of speech tags for each part of speech
	nouns = ['NN','NNP','NNS','NNPS']
	adj = ['JJ','JJR','JJS']
	verbs = ['VB,VBD','VBD','VBG','VBN','VBP','VBZ']

	#Will analyze and display various observations
	displayStopWords(onlyWords)
	displayPartOfSpeech(onlyWords,nouns,'nouns')
	displayPartOfSpeech(onlyWords,adj,'adjs')
	displayPartOfSpeech(onlyWords,verbs,'verbs')

def displayStopWords(words):
	allStopwords = set(stopwords.words('english'))
	stopwordsUsed = [w for w in words if w in allStopwords]
	
	most_common = wordFrequency(stopwordsUsed,5) 
	print('Most used stopwords :', most_common)

def displayPartOfSpeech(words,pos_types,pos_type):
	results = []

	for word, pos in nltk.pos_tag(words):
		for p_t in pos_types:
			if (pos==p_t):
				results.append(word)

	most_common = wordFrequency(results,10)
	print('Most used ',pos_type,':',most_common)

#Tokenizes the words in article and removes punctuation
def removePunctuation(article):
	words = nltk.word_tokenize(article)
	words = [word.lower() for word in words if word.isalpha()]
	return words

#Will display the top x most frequent words
def wordFrequency(words,top_x): 
	fdist = nltk.FreqDist(words)
	table = {}
	for word,frequency in fdist.most_common(top_x):
		table[word] = frequency

	return table

getContent()