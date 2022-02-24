from astropy.time import Time
import pandas as pd

class fits2jd(object):
	def __init__(self, inputFilename):
		self.inputFilename = inputFilename
	
	def transform(self):
		df = pd.read_csv(self.inputFilename, header=None)
		fits = list(df.iloc[:,0].values)
		t = Time(fits, format='isot', scale='utc')

		return t.jd