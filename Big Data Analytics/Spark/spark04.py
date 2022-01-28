"""
04. Sub-sample the data: filter the data by keeping only one signal per minute for each transmitting station.
"""
from pyspark import SparkContext
from datetime import datetime
import re


# set data path -- can be changed to AWS or DMIS filepath
dataPath = "/content/drive/MyDrive/UBS/HPC for Big Data/Spark/small_ais_data.csv"
# initiate spark context
sc = SparkContext(appName = "PySpark")

#UTILITY FUNCTIONS
def format(x):
  return ','.join(x)

def clean_key(id1, id2):
  return id1 + " " + id2.replace('"', '').replace("'", '')

def split_rdd():
  # open file as RDD
  rdd = sc.textFile(dataPath)
  return rdd.map(lambda line: line.split(",")) # split into columns

# define printing function
def printer(val):
  for v in val:
    print(v)

# define time converter
def time_converter(time):
  timestamp = datetime.utcfromtimestamp(0)
  try:
    dt = datetime.strptime(time, "%Y-%m-%d %H:%M:%S GMT")
  except:
    dt = datetime.strptime(eval(time), "%Y-%m-%d %H:%M:%S GMT")
  # dt = datetime.strptime(eval(time), "%Y-%m-%d %H:%M:%S GMT")
  delta = dt - timestamp
  seconds = int(delta.total_seconds())
  seconds = str(seconds)
  return seconds


def NewData():
  # map columns of text file
  columns = split_rdd()
  # check for good data
  mmsi_time = columns.filter(lambda x: len(str(x[0])) != 0 and len(str(x[1])) != 0) # mmsi and time not null
  lat_lon = mmsi_time.filter(lambda x: float(x[2]) != 0 and float(x[3]) != 0) # lat and long not null
  #lat long in the range
  in_range = lat_lon.filter(lambda x: float(x[2]) >- 90 and float(x[2]) <90 and float(x[3]) >-180 and float(x[3]) < 180)
  #check for time
  correct_time = in_range.filter(lambda x: len(x[1]) == 25)
  
  m = correct_time.map( lambda x: (time_converter(x[1]), x) )
  printer(m.collect())


#RUN SCRIPT
if __name__ == "__main__":
    NewData()