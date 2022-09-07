# stop words remover
# create a function to remove stop words from a corpus of text
# and compute the most frequent word in the dictionary.

# import the PySpark Library
import sys
import re
from pyspark import SparkContext
import subprocess

WORD_RE = re.compile(r"[\w']{2,}")

def removeStopWords():
	sc = SparkContext(appName = "SparkRemoveStopWords")
	files = sc.textFile("s3://ubs-cde/gutenberg/Zane_Grey___Wildfire.txt")
	
	# map word count information
	words= files.flatMap(lambda line: WORD_RE.findall(line)) 	
	
	# lower the words 
	lowered_words = words.map(lambda word: word.lower())
	
	# remove stop words
	stopwords = sc.textFile("s3://ubs-cde/stop-words/stop-words-english4.txt")
	no_stop_words = lowered_words.subtract(stopwords)
	
	# extract key value pairs
	pairs = no_stop_words.map(lambda word: (word, 1))
	
	# word count
	counts = pairs.reduceByKey(lambda x, y: x + y)
					
	new_words = counts.map(lambda count: (count[1], count[0]))
	
	# select the top ten most frequent words
	top_word = new_words.sortByKey(ascending =False).take(10)
	
	for (word, count) in top_word:
		print(word, ":", count)
		
	sc.stop()


if __name__ == '__main__':
	removeStopWords()
