

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

print('hello')

def r_val():
  values = {
  'bin1':2,
  'bin2':4,
  'bin3':8,
  'bin4':16
  }
  return values
def calcR_perBin():
  data = r_val()
  # print(data)
  return data
test = calcR_perBin()
x=[]
for key,value in test.items():
  x.append(value*2)
R = x
# print(R)
finalBoxSize={}
c=1
for i in R:
  finalBoxSize['bin#%s'%str(c)]=i*2/8
  c+=1
print(finalBoxSize)


