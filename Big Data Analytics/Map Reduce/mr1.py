from mrjob.job import MRJob
from mrjob.step import MRStep
import re

class FilterUniqCount(MRJob):
	"""
	Filter unique data with the criteria that duplicates would have the same time and mmsi. 
	At a later step, it compute the total number of lines and the number of unique lines. 
	"""
	def mapper_filter(self, _, line):
	# split the lines by the comma
		mmsi, time = line.split(',')[:2]
	# select the first two columns: MMSI and TIME to create unique key combination.
		yield ((mmsi, time), line)

	def reducer_filter(self, uniq_key, value):
	# select only the first line of the value pair with the unique key
		yield (uniq_key, next(value))

	def mapper_count_all(self, key, value):
		yield "key", 1

	def reducer_count_all(self, key, value):
		yield 1, sum(value)
	
	def steps(self):
		return [
			MRStep(mapper = self.mapper_filter,
			reducer = self.reducer_filter),

			MRStep(mapper = self.mapper_count_all,
			reducer = self.reducer_count_all)
			]

if __name__ == '__main__':
	FilterUniqCount.run()
