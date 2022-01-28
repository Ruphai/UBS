"""
03. Convert the field TIME: from the ISO format to the Unix format
"""
from pyspark import SparkContext
from datetime import datetime

# set data path -- can be changed to AWS or DMIS filepath
dataPath = "/content/drive/MyDrive/UBS/HPC for Big Data/Spark/small_ais_data.csv"
# initiate spark context
sc = SparkContext(appName = "PySpark")


# UTILITY FUNCTIONS

# load and split data
def split_rdd():
  # open file as RDD
  rdd = sc.textFile(dataPath)
  return rdd.map(lambda line: line.split(",")) # split into columns

# time converter function
def time_converter(time):
  timestamp = datetime.utcfromtimestamp(0)
  dt = datetime.strptime(eval(time), "%Y-%m-%d %H:%M:%S GMT")
  delta = dt - timestamp
  seconds = int(delta.total_seconds())
  seconds = str(seconds)
  return seconds

# define printing function
def printer(val):
  for v in val:
    print(v)

# SPARK CONVERT TIME
def GoodTime():
  columns = split_rdd()
  keys = columns.map(lambda k: ( (k[0], time_converter(k[1]), str(k) ) ) )
  keys.distinct()
  k = keys.take(10)

  printer(k)


#RUN SCRIPT
if __name__ == "__main__":
    GoodTime()