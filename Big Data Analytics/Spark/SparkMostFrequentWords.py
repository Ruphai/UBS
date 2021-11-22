# import the PySpark Library
import sys
from pyspark import SparkContext, SparkConf

def frequentWord():
  sc = SparkContext(appName = "FrequentWords")
  lines = sc.textFile("s3://ubs-cde/gutenberg/Zane_Grey___Wildfire.txt")
  line_len = lines.map(lambda x: len(x))
  # line_len.persist()

  doc_len = line_len.reduce(lambda x, y:x+y)
  print(doc_len)
  df = spark.createDataFrame(data = lines, schema = columns)
  df.show(10)
  
  #doc_len.saveAsTextFile("spark_output/WordCount")
 

  if __name__ == '__main__':
    frequentWord()
