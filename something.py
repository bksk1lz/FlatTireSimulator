import numpy as np

class ridesim:

	def __init__(self, sim_length):
		self.ride = np.randvar.uniform(0, 1, npoints)
		
	def getintervals(self, indprob, depprob):
		
		i = 0
		interlist = []
		
		for sample in self.ride:
			if i < 200:
				flatprob = depprob
			else:
				flatprob = indprob
			
			if sample < flatprob:
				interlist.append(i)
		
		self.intervals = interlist

	def getintersum(self, intersize):
		self.intersum = [sum(self.intervals[i:intersize]) 
						 for i in np.arange(len(self.intervals))]