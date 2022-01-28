from mrjob.job import MRJob
from mrjob.step import MRStep
from datetime import datetime
import re

# time converter
def time_converter(time):
	epoch = datetime.utcfromtimestamp(0)
	dt = datetime.strptime(time, "%Y-%m-%d %H:%M:%S GMT")
	delta = dt - epoch
	return int(delta.total_seconds())

class AISTimeFilter(MRJob):
	def mapper(self, _, line):
		# Get the time and MMSI columns data
		mmsi, time = re.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", line)[:2]

		# convert time to UNIX time stamp
		unix_time = time_converter(eval(time))
		yield ((mmsi, unix_time), line)

	def reducer(self, key, value):
		yield key, next(value)

	def mapper_cond(self, key, line):
		time, lat, long = re.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", line)[1:4]

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
		# extract the time and mmsi columns data
		columns = re.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", line)
		columns[1] = time_converter(eval(columns[1]))
		yield key, ", ".join([str(i) for i in columns])

	def mapper_utc(self, key, line):
		# extract the time and mmsi columns data
		columns = re.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", line)
		time = datetime.fromtimestamp(eval(columns[1]))

		# remove seconds from the date
		utc_time = time_converter(time.strftime("%Y-%m-%d %H:%M:00 GMT"))
		# Create new ID
		mmsi = columns[0]
		yield ((mmsi, utc_time), line)

	def steps(self):
		return [
			MRStep(mapper=self.mapper,
				combiner=self.reducer,
				reducer=self.reducer),
			MRStep(mapper=self.mapper_cond,
				reducer=self.reducer_cond),
			MRStep(mapper=self.mapper_time),
			MRStep(mapper=self.mapper_utc,
				reducer=self.reducer)
		]

if __name__ == '__main__':
	AISTimeFilter.run()
