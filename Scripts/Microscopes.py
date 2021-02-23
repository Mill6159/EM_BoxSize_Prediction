# Description
# This code was built by Robert Miller and Peiwen Shi
# Was developed for use by the Ando lab etc etc

# Modules

import os
import numpy as np 
import sys

# Classes

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
    highdefocus=2000):
    '''
    Description
    Defines inputs given by the microscope:
    notify: If true, a message prints into the terminal indicating the class has been initiated.
    micro: The type of microscope used for data collection. Default: Arctica

    Workflow explanation
    micro_dict: nested dictionary
    For each microscope a set of parameters are stored.
    (1) pixel_size: in angstroms
    (2) lambda: electron beam wavelength in meters
    (3) Cs: corrector for spherical aberration in meters

    '''

    # As we build, we should set micro to None and allow the user to choose each time?

    self.micro = micro
    self.lowdefocus = lowdefocus
    self.highdefocus = highdefocus
    self.d = d

    self.micro_dict = { # make the dictionary a property of the class.
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
    if self.notify == True: # write to the terminal
      self.help_message()
      sys.exit()
    # else: # or don't
    #   pass

    # print(self.micro,self.micro_dict[self.micro]['pixel_size']) # example of how to access values within the dictionary


  def help_message(self):
    '''
    Generates a help message when a user passes the -h flag in the terminal
    '''
    print('#'*63)
    print('#'*63)
    print('Microscopes class has been called')
    print('This class accepts the following arguments:')
    print('PROVIDE BRIEF DESCRIPTION OF EACH')
    print('\t-micro: the type of microscope\t')
    for key in self.micro_dict:
      print('\t\t\t+',key)
    print('\t-d: the estimated diameter of the particle in Angstroms')
    print('\t\t+ Default is 50 angstroms')
    print('#'*63)
    print('#'*63)

    

# testClass = Microscopes(notify=True)

# print(testClass.micro)

# testClass.micro = "Krios"

# print(testClass.micro)

# print(testClass.micro_dict)





  # """
  # Description
  # Defines objects that contain all microscope information
  # """

  # def __init__(self,
  #   notify=False,
  #   micro='Arctica',
  #   d=200,
  #   lowdefocus=1000,
  #   highdefocus=2000):
  #   '''
  #   docstring

  #   Inputs:
  #   notify: If true, a message prints into the terminal indicating the class has been initiated.
  #     Is the purpose of notify to generate the help message? RM: For the user to understand the code inputs
  #     Is the user going to decide true or false / Do we always want a help message to be generated? RM: Only if user indicates --h
  #   micro: The type of microscope used for data collection. Default: Arctica
  #   d: Estimated diameter of the molecule imaged in the microscope. Default: 150 Angstroms
  #   lowdefocus: lowest defocus value data was collected at input in units nanometer
  #   highdefocus: highest defocus value data was collected at input in units nanometer
  #     Are these values entered by the user every time? RM: They do not have to be but it will then use the defaults
  #     (Is the defocus range fixed for a microscope?) RM: No but we will provide defaults for the user if they do not provide this info each time
  #   Cs:
  #   lamdba:


  #   workflow explanation:
  #   micro_dict: nested dictionary
  #   For each microscope a set of parameters are stored.
  #   (1) pixel_size:
  #   (2) lambda: electron beam wavelength in meters

  #   '''

  #   # As we build, we should set micro to None and allow the user to choose each time?

  #   self.micro = micro
  #   self.d = d
  #   self.highdefocus = highdefocus
  #   self.lowdefocus = lowdefocus

  #   self.micro_dict = { # make the dictionary a property of the class. RM! add default u value for each microscope.
  #   'Arctica': {
  #   'pixel_size': 0.505,
  #   'lambda': 2.50795*10**-12,
  #   'Cs':0.0027,
  #   'u':(1/(3.5 * 10**(-10)))}, #RM! Need to the same for Krios and other microscopes

  #   'Krios': {
  #   'pixel_size': 0.505,
  #   'lambda': 1.96876*10**-12,
  #   'Cs':0.0027}}

  #   '''
  #   Generally, why are we treating micro, d, lowdefocus, highdefocus differently from pixel_size, lambda and Cs?
  #   (Why not include all in the nested dictionary?) RM: d, low/highdefocus are experiment specific

  #   The idea I am getting is that the nested dictionary associates certain values for parameters in each microscope
  #   (so that the user does not need to enter the default values every time?)
  #   Will these values remain constant in different measurements? RM: Exactly! and yes, these will be constant for every experiment
  #   '''

  #   self.notify = notify
  #   if self.notify == True: # write to the terminal
  #     self.help_message()
  #     sys.exit() # RM! kill the code after printing the help message - not working
  #   else: # or don't
  #     pass

  #   # print(self.micro,self.micro_dict[self.micro]['pixel_size']) # example of how to access values within the dictionary


  # def help_message(self):
  #   '''
  #   Generates a help message when a user passes the -h flag in the terminal
  #   '''
  #   print('#'*50)
  #   print('#'*50)
  #   print('Microscopes class has been called')
  #   print('THIS IS THE HELP MESSAGE')
  #   print('This class accepts the following arguments:')
  #   print('PROVIDE BRIEF DESCRIPTION OF EACH')
  #   print('\t-micro: the type of microscope\t')
  #   for key in self.micro_dict:
  #     print('\t\t\t+',key)
  #   print('\t-d: the estimated diameter of the particle in Angstroms')
  #   print('\t\t+ Default is 50 angstroms')
  #   print('#'*50)
  #   print('#'*50)

    

# testClass = Microscopes(notify=True)

# print(testClass.micro)

# testClass.micro = "Krios"

# print(testClass.micro)

# print(testClass.micro_dict)












