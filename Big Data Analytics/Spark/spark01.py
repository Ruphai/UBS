from pyspark import SparkContext

"""
QUESTION 1: In this file, the unique data in the AIS data are filtered out assuming the condition that Duplicate data have the same TIME and MMSI. 
"""

# set data path -- can be changed to AWS or DMIS filepath
dataPath = "/content/drive/MyDrive/UBS/HPC for Big Data/Spark/small_ais_data.csv"
# initiate spark context
sc = SparkContext(appName = "PySpark")

# UTILITY FUNCTIONS
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
    

# SPARK FILTER FUNCTION
def FilterData():
    """
    Function prints out unique data in the AIS data provided 
    """
    # map columns of text file
    rdd_init = split_rdd()
    rdd_split = rdd_init.map(lambda k: ( clean_key(k[0], k[1]), format(k) ) ) 
    rdd_split.distinct()
    uniq = rdd_split.distinct().take(1000) # test for the first 1000 lines
    printer(uniq)

#RUN SCRIPT
if __name__ == "__main__":
    FilterData()