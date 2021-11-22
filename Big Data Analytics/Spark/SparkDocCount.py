# import the PySpark Library
import sys
from pyspark import SparkContext, SparkConf

def doccount():
  sc = SparkContext(appName = "SparkDocCount")
  lines = sc.textFile("s3://ubs-cde/gutenberg/Zane_Grey___Wildfire.txt") # double check
  line_len = lines.map(lambda x: len(x))
  #line_len.collect()
  doc_len = line_len.reduce(lambda x, y:x+y)
  print(doc_len)
  
  #doc_len.saveAsTextFile("spark_output/WordCount")
  
  if __name__ == '__main__':
    doccount()
