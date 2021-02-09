# Description
# This is the 'master' script 
# The script will call all others and generate the user interface and outputs

# Modules

from Microscopes import *

# Classes

# micros = Microscopes(notify=True)

# User inputs

# micro_input = input('Type of microscope (default Arctica): ')
# diameter_input = input('Diameter of particle in Angstrom (default 50): ')
# low_defocus_input = input('Low defocus value in nanometer (default 1000): ')
# high_defocus_input = input('High defocus value in nanometer (default 2000): ')

# Also need to build the code such that if 
# python BoxSizePrediction.py -h 
# is issued in the terminal it shifts notify = True

# Calculations

# this should generate an output log file (maybe build that into Microscopes.py)

class BoxSizeCalcs(Microscopes):
	'''
	Description of the class
	This class inherits the properties of the Microscopes() class
	'''


	def calc_dF(self):
		'''
		Description
		From the microscope defocus range, calculate the delta defocus value (dF) in nanometer

		Input/Output:



		'''
		dF = self.highdefocus - self.lowdefocus 

		return dF

	def finalBoxSize(self):
		'''
		Description
		Given all other inputs, this returns the minimum, optimum, and largest suggested box sizes for
		structure reconstruction
		'''

		self.smallBox = 1
		self.optimalBox = 2
		self.bigBox = 3

		return self.smallBox, self.optimalBox, self.bigBox


	def boxesPerGrid(self):
		'''
		Description
		Given a known box size AND a known size of grid holes on the cyro-EM grids
		one can predict the total number of particles per grid hole for ideal data collection
		(i.e. particle density, i.e. protein concentration)

		Resource: https://math.stackexchange.com/questions/466198/algorithm-to-get-the-maximum-size-of-n-squares-that-fit-into-a-rectangle-with-a
		'''

		a,b,c = self.finalBoxSize()

		return a,b,c



boxTest = BoxSizeCalcs(Microscopes(notify=True))

print('TEST')
print(boxTest.micro)

print(boxTest.calc_dF())

print(boxTest.boxesPerGrid())

