# import the PySpark Library
import sys
from pyspark import SparkContext, SparkConf

def wordcount():
  sc = SparkContext(appName = "SparkWordCount")
  files = sc.textFile("s3://ubs-cde/gutenberg/Zane_Grey___Wildfire.txt")
  
  # map word count information
  
  words= files.flatMap(lambda line: line.split(" ")) \
						.map(lambda word: (word, 1)) \
						.reduceByKey(lambda x, y: x + y)

  word_count = words.collect()
  words.saveAsTextFile("spark_output/WordCount")
  
  for (word, count) in word_count:
	  print(word, ": ", count)	  
 
 if __name__ == '__main__':
	 wordcount()
