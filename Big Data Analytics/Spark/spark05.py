"""
05. Make a list of ships: build a list of all the ships (MMSI, name) detected by AISHUB
"""

#UTILITY FUNCTIONS
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
    


# SPARK BUILD SHIP LIST FUNCTION
def ShipList():
  # map columns of text file
  rdd_init = split_rdd()
  rdd_split = rdd_init.map(lambda k: ( clean_key(k[0], k[9]) ) ) 
  rdd_split.distinct()
  uniq = rdd_split.take(10)

  printer(uniq)


if __name__ == "__main__":
    ShipList()