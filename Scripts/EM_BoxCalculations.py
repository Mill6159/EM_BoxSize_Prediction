# General description
# Authors: Rob Miller & Peiwen Shi
# Report issues to the GitHub issues page or rcm347@cornell.edu
#
# Short script was developed to calculate the ideal box size for 
# particle picking in the processing of cryo-EM data.
# Calculations may be performed for various experimental conditions and
# types of microscopes.
# Users can input parameter values or select those provided by default.
# Parameters for ideal box size calculation include diameter of particle 
# imaged, lowest and highest defocus, pixel size, electron beam wavelength, 
# spherical aberration constant, and resolution achieved.
# Default values are provided for microscopes Arctica, Krios, and Polara.
# Based on user's inputs or default selections, an optimal box size will be 
# generated along with two box sizes above and below the optimal.
# Using the optimal box size
 
# Modules
import argparse
import os
import numpy as np 
import sys

# User inputs

# micro_input = input('Type of microscope (default Arctica): ')
# diameter_input = input('Diameter of particle in Angstrom (default 50): ')
# low_defocus_input = input('Low defocus value in nanometer (default 1000): ')
# high_defocus_input = input('High defocus value in nanometer (default 2000): ')

# Microscope Class


class Microscopes:
  """
  Description
  Defines objects that contain all microscope information
  """

  def __init__(self,
    notify=False,
    micro='Arctica',
    d=200,
    lowdefocus=1000,
    highdefocus=2000,
    u=None):
    '''
    Description
    Defines inputs given by the microscope:
    notify: If true, a message prints into the terminal indicating the class has been initiated.
    micro: The type of microscope used for data collection. Default: Arctica
    d: Estimated diameter of the molecule imaged in the microscope. Default: 150 Angstroms
    lowdefocus: lowest defocus value for data collected at input in units nanometer
    highdefocus: highest defocus value for data collected at input in units nanometer

    Workflow explanation
    micro_dict: nested dictionary containing default values
    For each microscope a set of parameters are stored.
    (1) pixel_size: size of pixel in angstrom
    (2) lambda: electron beam wavelength in meter
    (3) Cs: spherical aberration constant in meter
    (4) u: resolution achieved in meter

    '''

    self.micro = micro
    self.lowdefocus = lowdefocus
    self.highdefocus = highdefocus
    self.d = d
    self.u = u

    self.micro_dict = {
    'Arctica': {
    'pixel_size': 0.505,
    'lambda': 2.50795*10**-12,
    'Cs':0.0027,
    'u':(1/(3.5 * 10**(-10)))},

    'Krios': {
    'pixel_size': 0.505,
    'lambda': 1.96876*10**-12,
    'Cs':0.0027,
    'u':(1/(2.0 * 10**(-10)))},
    
    'Polara':{
    'pixel_size':0.505,
    'lambda':1.96876*10**-12,
    'Cs':0.00226,
    'u':(1/(4.0 * 10**(-10)))}}

    self.notify = notify
    if self.notify == True:
      self.help_message()
      sys.exit()


  def help_message(self):
    '''
    Generates a help message when a user passes the -h flag in the terminal
    '''
    print('#'*90)
    print('#'*90)
    print('#'*32,'EM Box Size Calculations','#'*32)
    print('Inputs, Defaults, and Descriptions:')
    print('\t-m , --micro: the type of microscope\t')
    for key in self.micro_dict:
      print('\t\t\t+',key)
    print('\t-d , --diameter: the estimated diameter of the particle in Angstroms')
    print('\t\t+ Default is 50 angstroms')
    print('\t-ld , --lowdefocus: the low defocus value')
    print('\t-hd , --highdefocus: the high defocus value')
    print('\t-hr , --highresolution: the highest anticipated resolution in Angstrom')
    print('\t\tDefault for each microscope currently:')
    for key in self.micro_dict:
      print('\t\t\t+',key)
      print('\t\t\t\t+',1/(self.micro_dict[str(key)]['u']*10**(-10)))

    print('#'*90)
    print('#'*90)

class BoxSizeCalcs(Microscopes):
  '''
  Description of the class
  This class inherits the properties of the Microscopes() class
  '''


  def calc_dF(self):
    '''
    Description
    From the microscope defocus range, calculate the delta defocus value (dF) in nanometer

    Inputs:
    lowdefocus: lowest defocus value for data collected at input in units nanometer
    highdefocus: highest defocus value for data collected at input in units nanometer

    This function is not used in the current version of box size calculation

    '''

    dF = self.highdefocus - self.lowdefocus 

    return dF

  def nyquist_Calc(self):
    '''
    Description
    Calculates Nyquist value in Angstrom as a function of pixel size and bin number

    Inputs:
    bin#: bin number
    pixel_size: size of pixel in angstrom


    This function is not used in the current version of box size calculation

    '''


    bin1 = 2 * self.micro_dict[self.micro]['pixel_size']
    bin2 = 4 * self.micro_dict[self.micro]['pixel_size']
    bin3 = 8 * self.micro_dict[self.micro]['pixel_size']
    bin4 = 16 * self.micro_dict[self.micro]['pixel_size']

    return bin1, bin2, bin3, bin4

  def calcR(self):
    '''
    Description
    Calculates R = lambda * dF * u + Cs * lambda^3 * u^3
    
    Inputs:
    u: resolution achieved in 1/m
    ubin#: bin number
    dF: defocus given by the highest defocus value in nanometer

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

    if self.u == None:
      self.u = self.micro_dict[self.micro]['u']
    else:
      self.u = 1/(float(self.u)*10**(-10)) # converting user input from Angstrom to 1/meters

    dF = self.highdefocus * (10**(-9))# from nanometers to meters
    wavelength = self.micro_dict[self.micro]['lambda'] # in units meters
    print('TEST: ', self.u)
    u = self.u # units meters
    print('TEST2: ', u)
    Cs = self.micro_dict[self.micro]['Cs']
    R = (wavelength * dF * u) + (Cs*(wavelength**3)*(u**3))
    dF = self.highdefocus * (10**(-9)) # from nanometers to meters
    Cs = self.micro_dict[self.micro]['Cs'] # in units meters
    R = (wavelength * dF * u) + (Cs*(wavelength**3)*(u**3)) # in units meters

    return R

  def finalBoxSize(self):
    '''
    Description
    Given all other inputs, returns the minimum, optimum, and largest suggested box sizes for
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
    882, 896, 900, 960, 972, 980, 1000, 1008, 1024, 1050, 1080, 1120, 1134, 1152, 1176, 
    1200, 1250, 1260, 1280, 1296, 1344, 1350, 1372, 1400, 1440, 1458, 1470, 1500, 1512, 
    1536, 1568, 1600, 1620, 1680, 1728, 1750, 1764, 1792, 1800, 1890, 1920, 1944, 1960, 
    2000, 2016, 2048, 2058, 2100, 2160, 2240, 2250, 2268, 2304, 2352, 2400, 2430, 2450, 
    2500, 2520, 2560, 2592, 2646, 2688, 2700, 2744, 2800, 2880, 2916, 2940, 3000, 3024, 3072, 
    3136, 3150, 3200, 3240, 3360, 3402, 3430, 3456, 3500, 3528, 3584, 3600, 3750, 3780, 3840, 
    3888, 3920, 4000, 4032, 4050, 4096] # ideal box sizes 

    try:
      index=[]
      c=0
      for i in list_of_boxes:
        if i >= boxSize*10**10:
          index.append(c)
          break
        c+=1

      self.smallBox = list_of_boxes[c-1]
      self.optimalBox = list_of_boxes[c]
      self.bigBox = list_of_boxes[c+1]

      print('#'*15,'Input Parameters','#'*15)
      print('Particle Diameter (Angstrom):',self.d)
      print('Microscope:',self.micro)
      print('Maximum defocus value (nm):', self.highdefocus)
      print('Maximum anticipated resolution (Angstrom):','%.2f'%(1/self.u*10**10))
      print('#'*48)
      print('')

      print('#'*13,'THE FINAL BOX SIZES','#'*14)
      print('The optimal box size is:', self.optimalBox)
      print('The box size below the optimal is:', self.smallBox)
      print('The box size above the optimal is:', self.bigBox)
      print('#'*48)
      print('')
    except IndexError as error:
      print('*'*65)
      print('Error arose when attempting to calculate ideal box size')
      print('Particle size was likely too small/large... double check inputs')
      print('Error Message:',error)
      print('*'*65)
      sys.exit()


    return boxSize


  def boxesPerGrid(self):
    '''
    Description
    Given a known box size AND a known size of grid holes on the cyro-EM grids
    one can predict the total number of particles per grid hole for ideal data collection
    (i.e. particle density, i.e. protein concentration)
    
    '''

    print('#'*10,'Boxes Per Grid Calculation','#'*10)
    print('Assumes a circle that is 10X the box size')

    d_circle = (self.optimalBox*10) # arbitrary diameter of circle
    r_circle = d_circle/2 # radius of circle
    c_circle = np.pi*d_circle # circumference of circlee
    a_circle = np.pi*(r_circle)**2 # area of circle
    l_box = self.optimalBox # length of box edge
    a_box = l_box **2 # area of box
    boxes_per_grid = a_circle/a_box - np.sqrt(1/2)*(c_circle / l_box)

    ## Add in round down to nearest whole integer

    print('Possible number of boxes per grid:', np.floor(boxes_per_grid))
    print('#'*48)



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
parser.add_argument('-hr','--highresolution', action="store", dest='hr',default=None) # in meters

## Lets add a --info flag that includes microscope/experiment/etc details
# Now, parse the command line arguments and store the 
# values in the `args` variable
args = parser.parse_args()

# Individual arguments can be accessed as attributes...

# -----> Run script

calcs = BoxSizeCalcs(d=float(args.d),
                    notify=args.notify,
                    micro=str(args.micro),
                    lowdefocus=float(args.ld),
                    highdefocus=float(args.hd),
                    u=args.hr)


calcs.finalBoxSize()
calcs.boxesPerGrid()



    