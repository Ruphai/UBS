from mrjob.job import MRJob
from mrjob.step import MRStep
from datetime import datetime
import re

def time_converter(time):
	timestamp = datetime.utcfromtimestamp(0)
	dt = datetime.strptime(eval(time), "%Y-%m-%d %H:%M:%S GMT")
	delta = dt - timestamp
	seconds = int(delta.total_seconds())
	return seconds

class ConvertTime(MRJob):
	"""
	This MapReduce function converts the field time from the ISO format to the UNIX format. 
	Additional Python Module: DateUtil. 
	"""
	def mapper(self, _, line):
		#split based on commas
		mmsi, time = re.split(",", line)[0:2]
		unix_time = time_converter(time)
		yield ((mmsi, unix_time), line)

	def reducer(self, key, value):
		# return only the first value
		yield key, next(value)

	def mapper_cond(self, key, line):
		# extract the columns
		time, lat, long = re.split(",(?=(?:[^\"]*\")*[^\"]*$)", line)[1:4]

		#check for the validity of the time, latitude and longitude column
		lat_cond = eval(lat) > 90 or eval(lat) < -90
		long_cond = eval(long) > 180 or eval(long) < -180
		time_cond = len(eval(time)) >= 25
		condition = lat_cond or long_cond or time_cond
		if not condition:
			yield key, line

	def reducer_cond(self, key, lines):
		for line in lines:
			yield key, line

	def mapper_time(self, key, line):
        # Get the time and MMSI columns data
		columns = re.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", line)
		columns[1] = time_converter(eval(columns[1]))
		yield key, ", ".join([str(i) for i in columns])

	def steps(self):
		return [
			MRStep(mapper = self.mapper,
				combiner = self.reducer,
				reducer = self.reducer),
			MRStep(mapper = self.mapper_cond,
				reducer = self.reducer_cond),
			MRStep(mapper = self.mapper_time)]

if __name__ == '__main__':
	ConvertTime.run()
