# import the PySpark Library
import sys
from pyspark import SparkContext, SparkConf

def frequentWord():
  sc = SparkContext(appName = "FrequentWords")
  files = sc.textFile("s3://ubs-cde/gutenberg/Zane_Grey___Wildfire.txt")
  # map word count information
  words= files.flatMap(lambda line: line.split(None)) \
						.map(lambda word: (word, 1)) \
						.reduceByKey(lambda x, y: x + y)
  
  words = words.map(lambda word: (words[1], word[0]))
  
  # select the top ten most frequent words
  top_word = words.sortByKey(ascending =False).take(10)
  
  for (word, count) in top_word:
	  print(word, ":", count))

if __name__ == '__main__':
	frequentWord()
