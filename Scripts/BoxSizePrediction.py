# Description
# This is the 'master' script 
# The script will call all others and generate the user interface and outputs

# Modules

from Microscopes import *
import argparse

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


  ## RM! Add init function for super/subclass to better accept command line inputs
  # Fixed with hacky method at the bottom for now

  # def __init__(self, notify=None,
  #              d=None,
  #              micro=None,
  #              lowdefocus=None,
  #              highdefocus=None):
  #   if d is None:
  #     super(BoxSizeCalcs, self).__init__()
  #   # elif notify is None:
  #   #   super(BoxSizeCalcs, self).__init__(d=200,
  #   #                                      micro='Arctica',
  #   #                                      lowdefocus=1000,
  #   #                                      highdefocus=2000)
  #   # elif micro is None:
  #   #   super(BoxSizeCalcs, self).__init__(d=200,
  #   #                                      notify=False,
  #   #                                      lowdefocus=1000,
  #   #                                      highdefocus=2000)
  #   # elif lowdefocus is None:
  #   #   super(BoxSizeCalcs, self).__init__(d=200,
  #   #                                      micro='Arctica',
  #   #                                      notify=False,
  #   #                                      highdefocus=2000)
  #   # elif highdefocus is None:
  #   #   super(BoxSizeCalcs, self).__init__(d=200,
  #   #                                      micro='Arctica',
  #   #                                      notify=False,
  #   #                                      lowdefocus=1000)
  #   else:
  #     super(BoxSizeCalcs, self).__init__(Microscopes)
  #   self.d = d
  #   self.micro = micro
  #   self.lowdefocus = lowdefocus
  #   self.highdefocus = highdefocus

  def calc_dF(self):
    '''
    Description
    From the microscope defocus range, calculate the delta defocus value (dF) in nanometer

    Input/Output:



    '''
    dF = self.highdefocus - self.lowdefocus 

    return dF

  def nyquist_Calc(self):
    '''
    Description
    Calculates Nyquist value in Angstrom as a function of pixel size and bin number

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

  def R(self):
    '''
    doc string
    Description
    Calculates R = lambda * dF * u + Cs * lambda^3 * u^3 in meters
    '''

    dF = self.highdefocus * (10**(-9))# from nanometers to meters
    wavelength = self.micro_dict[self.micro]['lambda'] # in units meters
    u = 1/(3.5 * 10**(-10)) # units meters
    Cs = self.micro_dict[self.micro]['Cs']
    R = (wavelength * dF * u) + (Cs*(wavelength**3)*(u**3))
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

    # return boxSize

    R = self.R() # returns R value
    boxSize = (self.d * 10**(-10)) + 2*(R) # calculates box size from particle diamter and R

    list_of_boxes = [16, 24, 32, 36, 40, 44, 48, 52, 56, 60, 64, 72, 84, 96, 100, 
    104, 112, 120, 128, 132, 140, 168, 180, 192, 196, 208, 216, 220, 224, 240, 256, 
    260, 288, 300, 320, 352, 360, 384, 416, 440, 448, 480, 512, 540, 560, 576, 588, 
    600, 630, 640, 648, 672, 686, 700, 720, 750, 756, 768, 784, 800, 810, 840, 864, 
    882, 896, 900, 960, 972, 980, 1000, 1008, 1024] # ideal box sizes 

    try:
      index=[]
      c=0
      for i in list_of_boxes:
        if i >= boxSize*10**10: # must get box size into Angstrom
          index.append(c)
          break
        c+=1

      self.smallBox = list_of_boxes[c-1]
      self.optimalBox = list_of_boxes[c]
      self.bigBox = list_of_boxes[c+1]

      print('#'*10,'THE FINAL BOX SIZES','#'*10)
      print('The optimal box size is:', self.optimalBox)
      print('The box size below the optimal is:', self.smallBox)
      print('The box size above the optimal is:', self.bigBox)
      print('#'*41)
    except IndexError as error:
      print('*'*65)
      print('Error arose when attempting to calculate ideal box size')
      print('Particle size was likely too small/large... double check inputs')
      print('Error Message:',error)
      print('*'*65)


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



# Building command line arguments

# -----------> <------------ #
## Example for how to add flags to command line arguments
# Define the parser
parser = argparse.ArgumentParser(description='Short sample app',
                                 add_help=False)
# Declare an argument (`--algo`), saying that the 
# corresponding value should be stored in the `algo` 
# field, and using a default value if the argument 
# isn't given
parser.add_argument('-m ','--micro ', action="store", dest='micro', default='Arctica')
parser.add_argument('-d ','--diameter ', action="store", dest='d', default=50) # Angstrom
parser.add_argument('-h','--help', action="store_true", dest='notify') # store_true sets the value to True if the flag is present, and false if not.
parser.add_argument('-ld','--lowdefocus', action="store", dest='ld',default=1000)
parser.add_argument('-hd','--highdefocus', action="store", dest='hd',default=2000)
## Lets add a --info flag that includes microscope/experiment/etc details
# Now, parse the command line arguments and store the 
# values in the `args` variable
args = parser.parse_args()
# Individual arguments can be accessed as attributes...

# print ('ALGO OUTPUT - MICRO: ',args.micro)
# # print ('ALGO OUTPUT - Notify Statement: ',args.notify)
# print ('ALGO OUTPUT - Diameter INPUT: ',args.d)
# print(type(args.d))


test = BoxSizeCalcs(d=float(args.d),
                    notify=args.notify,
                    micro=str(args.micro),
                    lowdefocus=float(args.ld),
                    highdefocus=float(args.hd))

# print(test.d)
# print(test.micro)
# print(test.lowdefocus)

test.finalBoxSize()







