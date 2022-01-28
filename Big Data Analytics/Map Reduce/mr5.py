from mrjob.job import MRJob
import re

class AISShipList(MRJob):
	"""
	Builds the AIS Ship List.
	"""

	def mapper(self, _, line):
		columns = re.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", line)
		mmsi = columns[0]
		ship_name = columns[9]

		if ship_name ==" \"\"":
			ship_name = "NO_NAME"
		yield "Ship name", ship_name

if __name__ == '__main__':
	AISShipList.run()
