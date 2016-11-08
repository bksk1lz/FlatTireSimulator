import numpy as np

def ridegen(npoints):
	
	ride = np.randvar.uniform(0, 1, npoints)
	
	return ride

	
def getintervals(ride, interval_size, indprob, depprob):
	
	i = 0
	interval1 = []
	intervaln = []
	
	for sample in ride:
		if i < 200:
			flatprob = depprob
		else:
			flatprob = indprob
			
		if sample < flatprob:
			interval1.append(i)
			intervaln.append(int(np.cumsum(interval_list[-interval_size:])[-1:]))
			i = 0
		
		i += 1
		
	return intervaln