from mrjob.job import MRJob
class Count(MRJob):
	def mapper(self, key, value):
		yield "id", 1
	def reducer(self, key, value):
		yield 1, sum(value)

if __name__ == '__main__':
	Count.run()
