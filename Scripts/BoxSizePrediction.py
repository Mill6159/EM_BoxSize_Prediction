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
		highdefocus
		lowdefocus


		'''
		dF = self.highdefocus - self.lowdefocus 

		return dF

	def nyquist_Calc(self):
		'''
		Description
		Calculates Nyquist value in Angstrom as a function of pixel size and bin number
		Input/Output:
		bin#
		pixel_size

		What is the Nyquist?
		'''


		bin1 = 2 * self.micro_dict[self.micro]['pixel_size'] # nyquist in Angstrom
		bin2 = 4 * self.micro_dict[self.micro]['pixel_size']
		bin3 = 8 * self.micro_dict[self.micro]['pixel_size']
		bin4 = 16 * self.micro_dict[self.micro]['pixel_size']

		return bin1, bin2, bin3, bin4

	def calcR(self):
		'''
		Description
		Calculates R = lambda * dF * u + Cs * lambda^3 * u^3
		
		Inputs/Outputs:
		u = [1/m]
		ubin#:
		dF:

		'''

		u_bin1, u_bin2, u_bin3, u_bin4 = self.nyquist_Calc()
		u_bin1, u_bin2, u_bin3, u_bin4 = u_bin1*10**(-10), u_bin2*10**(-10), u_bin3*10**(-10), u_bin4*10**(-10) # convert to meters
		# dF = self.calc_dF()
		# print('dF',dF)
		dF = self.highdefocus * 10**(-9) # how is this dF?!
		# dF = dF * 10**(-9) # convert to meters
		Cs = self.micro_dict[self.micro]['Cs']
		wavelength = self.micro_dict[self.micro]['lambda']
		# print(wavelength, Cs, dF)

		u_vals = [u_bin1, u_bin2, u_bin3, u_bin4]
		c=1
		r_vals = {}
		for j in u_vals:
			r_vals['bin%s'%str(c)] = ((wavelength * dF)/j) + ((Cs * wavelength**3)/j**3)
			c+=1


		return r_vals # R value as a function of bin # 

	def finalBoxSize(self):
		'''
		Description
		Given all other inputs, this returns the minimum, optimum, and largest suggested box sizes for
		structure reconstruction
		'''

		self.smallBox = 1
		self.optimalBox = 2
		self.bigBox = 3

		r_vals = self.calcR()

		c=1
		boxSize ={}
		for key,value in r_vals.items():
			boxSize['bin%s'%str(c)] = self.d * 10**(-12) + 2 * value
			c+=1

		print(boxSize) # not correct values...

		return boxSize


	def boxesPerGrid(self):
		'''
		Description
		Given a known box size AND a known size of grid holes on the cyro-EM grids
		one can predict the total number of particles per grid hole for ideal data collection
		(i.e. particle density, i.e. protein concentration)

		Resource: https://math.stackexchange.com/questions/466198/algorithm-to-get-the-maximum-size-of-n-squares-that-fit-into-a-rectangle-with-a
		'''

		# a,b,c = self.finalBoxSize()

		# return a,b,c



boxTest = BoxSizeCalcs(Microscopes(notify=True))

print('TEST')
print(boxTest.micro)

print(boxTest.calc_dF())

print(boxTest.boxesPerGrid())

print(boxTest.nyquist_Calc())

boxTest.finalBoxSize()

