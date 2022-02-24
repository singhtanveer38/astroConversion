import os
from astropy.time import Time
import pandas as pd

class fits2jd(object):
	def init(directory):
		self.directory = directory
	
	def transform(self):
		fileNames = os.listdir(self.directory)
		