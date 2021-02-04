# Description

# Modules

# Classes

class Microscopes:

	def __init__(self,notify=False,
	             micro='Arctica',d=150,
	             lowdefocus=1000,
	             highdefocus=2000):
		'''
		docstring

		Inputs:
		notify: If true, a message prints into the terminal indicating the class has been initiated.
		micro: The type of microscope used for data collection. Default: Arctica
		d: Estimated diameter of the molecule imaged in the microscope. Default: 150 Angstroms
		lowdefocus: lowest defocus value data was collected at input in units nanometer
		highdefocus: highest defocus value data was collected at input in units nanometer
		
		micro_dict: nested dictionary
		For each microscope a set of parameters are stored.
		(1) pixel_size:
		(2) lambda: electron beam wavelength in meters

		'''

		# As we build, we should set micro to None and allow the user to choose each time?

		self.micro = micro
		self.d = d

		self.notify = notify
		if self.notify == True: # write to the terminal
			print('#'*10)
			print('Microscopes class has been called')
			print('#'*10)
		else: # or don't
			pass

		self.micro_dict = { # make the dictionary a property of the class.
		'Arctica': {
		'pixel_size': 0.505,
		'lambda': 2.50795*10**-12,
		'Cs':0.0027},

		'Krios': {
		'pixel_size': 0.505,
		'lambda': 1.96876*10**-12,
		'Cs':0.0027}}

		print(self.micro,self.micro_dict[self.micro]['pixel_size']) # example of how to access values within the dictionary
			


testClass = Microscopes(notify=True)

print(testClass.micro_dict)
