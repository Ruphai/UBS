from mrjob.job import MRJob
from mrjob.step import MRStep
import re

class AISGoodData(MRJob):
	def mapper(self, _, line):
		#extract mmsi and time columns
		mmsi, time = re.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", line)[:2]
		yield ((mmsi, time), line)

	def reducer(self, key, value):
		yield key, next(value)

	def mapper_condition(self, key, line):
		time, lat, long = line.split(',')[1:4]

		#check the validity of time, lat and long
		# with specified condition.
		lat_con = eval(lat) > 90 or eval(lat) < -90
		long_con = eval(long)> 180 or eval(long) < -180
		time_con = len(eval(time)) > 25

		condition = lat_con or long_con or time_con

		if not condition:
			yield key, line

	def reducer_condition(self, key, lines):
		for line in lines:
			yield key, line

	def steps(self):
		return [
			MRStep(mapper = self.mapper,
			reducer = self.reducer),
			MRStep(mapper = self.mapper_condition,
			reducer = self.reducer_condition)]

if __name__ == '__main__':
	AISGoodData.run()
