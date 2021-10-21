import pandas as pd
import numpy as np

"""
Anomaly detction with IQR and Z-scores
"""

def get_bounds(ser, k=1.5):
	"""Calculate upper and lower bounds of a series.
	
	Args:
		ser (series): numeric data
		k (float): IQR multiplier
	Returns:
		float: upper bound
		float: lower bound
	"""
	q1, q3 = ser.quantile([.25,.75])
	iqr = q3-q1

	return q3 + k*iqr, q1 - k*iqr


def get z_scores(ser, stdev=2.):
	"""Calculate z-scores of a series.
	
	Args:
		ser (series): numeric data
		stdev (float): standard deviations cutoff
	Returns:
		ser (series): z-scores
	"""
	pd.Series((ser-ser.mean())/ser.std())

	return ser[zscores.abs()>=stdev]


 if __name__ == "__main__":

 	ser = pd.read_csv('lemonade.csv')

 	print(get_bounds(ser))
 	print(get_bounds(ser, k=2))
 	print(get z_scores(ser))
 	print(get z_scores(ser, stdev=3))





