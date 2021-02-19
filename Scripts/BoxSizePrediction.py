# Description
# This is the 'master' script 
# The script will call all others and generate the user interface and outputs

# Modules

from Microscopes import *
import argparse # module for passing flags into the command line

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

  # def __init__(self):
  #   '''

  #   '''

  #   # RM! Maybe put default diamter and defocus values in this class? It isn't really a function of the microscope. 

  def __init__(self, 
    d=150, 
    lowdefocus=1000, 
    highdefocus=2000):
    '''
    Description
    Defines inputs:
    d: estimated diameter of the molecule imaged in the microscope. Default: 150 Angstroms
    lowdefocus: lowest defocus value data collected at input. Default: 1000 nanometers
    highdefocus: highest defocus value data collected at input. Default: 2000 nanometers

    '''

    self.d = d
    self.lowdefocus = lowdefocus
    self.highdefocus = highdefocus

  def nyquist_Calc(self):
    '''
    Description
    Calculates Nyquist value in Angstrom as a function of pixel size and bin number
    Input/Output:
    bin#
    pixel_size

    What is the Nyquist?
      What do the bins mean?
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
    dF = self.highdefocus * 10**(9) # how is this dF?!
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


    return r_vals # R value as a function of bin #  # not really used




  def R(self):
    '''
    Description
    Calculates R = lambda * dF * u + Cs * lambda^3 * u^3 in meters

    '''

    wavelength = self.micro_dict[self.micro]['lambda'] # in units meters
    dF = self.highdefocus * (10**(-9)) # from nanometers to meters
    Cs = self.micro_dict[self.micro]['Cs'] # in units meters
    u = 1/(3.5 * 10**(-10)) # in units meters
    R = (wavelength * dF * u) + (Cs*(wavelength**3)*(u**3)) # in units meters

    return R


  def finalBoxSize(self):
    '''
    Description
    Given all other inputs, this returns the minimum, optimum, and largest suggested box sizes for
    structure reconstruction
    '''

    # self.smallBox = 1
    # self.optimalBox = 2
    # self.bigBox = 3

    # r_vals = self.calcR()

    # c=1
    # boxSize ={}
    # for key,value in r_vals.items():
    #   boxSize['bin%s'%str(c)] = self.d * 10**(-12) + 2 * value
    #   c+=1

    # print(boxSize) # not correct values...

    R = self.R() # returns R value
    boxSize = (self.d * 10**(-10)) + 2*(R) # calculates box size from particle diamter and R
    
    list_of_boxes = [16, 24, 32, 36, 40, 44, 48, 52, 56, 60, 64, 72, 84, 96, 100, 
    104, 112, 120, 128, 132, 140, 168, 180, 192, 196, 208, 216, 220, 224, 240, 256, 
    260, 288, 300, 320, 352, 360, 384, 416, 440, 448, 480, 512, 540, 560, 576, 588, 
    600, 630, 640, 648, 672, 686, 700, 720, 750, 756, 768, 784, 800, 810, 840, 864, 
    882, 896, 900, 960, 972, 980, 1000, 1008, 1024] # ideal box sizes 

    for box in range(len(list_of_boxes)):
      if list_of_boxes[box] >= boxSize:
        new_list = list_of_boxes[box-1:]
        self.smallBox = new_list[0]
        self.optimalBox = new_list[1]
        self.bigBox = new_list[2]

    self.smallBox = smallBox
    self.optimalBox = optimalBox
    self.bigBox = bigBox

    return boxSize

    print('The optimal box size is', optimalBox)
    print('The box size below the optimal is', smallBox)
    print('The box size above the optimal is', bigBox)



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



# RM!
# Now we need to create a list of "good box sizes"
# then take our calculated box size, and find the closest value that is larger than our calculated box size
# and print a good box size above and below that

# example
# FFT Box Sizes
# Box Sizes
# 2
# 4
# 8
# .....
# 256
# 316
#

# once we have this list it will be a simple function to write that scans the list and finds the closest value to final box size that is larger

# if >= final size:
#


list_of_boxes = [16, 24, 32, 36, 40, 44, 48, 52, 56, 60, 64, 72, 84, 96, 100, 
104, 112, 120, 128, 132, 140, 168, 180, 192, 196, 208, 216, 220, 224, 240, 256, 
260, 288, 300, 320, 352, 360, 384, 416, 440, 448, 480, 512, 540, 560, 576, 588, 
600, 630, 640, 648, 672, 686, 700, 720, 750, 756, 768, 784, 800, 810, 840, 864, 
882, 896, 900, 960, 972, 980, 1000, 1008, 1024] # ideal box sizes 

#https://blake.bcm.edu/emanwiki/EMAN2/BoxSize

boxTest = BoxSizeCalcs(Microscopes(notify=False))

print('TESTS BELOW \n')
# print('Class Microscope Default micro: ',boxTest.micro)

# print('Calculating dF: ',boxTest.calc_dF())

# print('Nyquist values as a function of bin #: ',boxTest.nyquist_Calc())

print('Final Box Size')

print(boxTest.finalBoxSize()*10**10)

print('box size above')












































# -----------> <------------ #
## Example for how to add flags to command line arguments

# Define the parser
parser = argparse.ArgumentParser(description='Short sample app',
                                 add_help=False)

# Declare an argument (`--algo`), saying that the 
# corresponding value should be stored in the `algo` 
# field, and using a default value if the argument 
# isn't given
parser.add_argument('-m','--micro', action="store", dest='micro', default='Arctica')
parser.add_argument('-d','--diameter', action="store", dest='d', default=50) # Angstrom
parser.add_argument('-h','--help', action="store_true", dest='notify') # store_true sets the value to True if the flag is present, and false if not.

## Lets add a --info flag that includes microscope/experiment/etc details

# Now, parse the command line arguments and store the 
# values in the `args` variable
args = parser.parse_args()

# Individual arguments can be accessed as attributes...
print ('ALGO OUTPUT - MICRO: ',args.micro)
print ('ALGO OUTPUT - Notify Statement: ',args.notify)
print ('ALGO OUTPUT - Diameter INPUT: ',args.d)

boxTest = BoxSizeCalcs(Microscopes(notify=args.notify, # this is how to use the command line inputs to build the class
                                   micro=args.micro,
                                   d=args.d))





