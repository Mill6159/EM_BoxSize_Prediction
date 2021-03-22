# Predicting the ideal box size for EM structure determination  
* References:   
__(1)__  Rosenthal, Peter B., and Richard Henderson. ‘Optimal determination of particle orientation, absolute hand, and contrast loss in single-particle electron cryomicroscopy.’ Journal of molecular biology 333.4 (2003): 721-745.  
__(2)__  https://www.jiscmail.ac.uk/cgi-bin/webadmin?A2=ccpem;e433702b.1412  
__(3)__  https://math.stackexchange.com/questions/3007527/how-many-squares-fit-in-a-circle

## Summarized derivation (low priority)   

## Code workflow  (high priority)  

This code was built using object-oriented programming in python. Objects are created under two classes: class ```Microscopes``` and class ```BoxSizeCalcs```. The Microscopes class defines objects that contain all information about the microscope. The ```__init__``` constructor defines parameters for the microscope: the type of microscope used, estimated diameter of particles imaged in the microscope, and the lowest and highest defocus values for data collection. The values for these parameters are provided by default for the microscope Arctica and a particle diameter of 15 angstroms, but can be inputted by the user depending on the type of microscope used and other experimental conditions. The ```__init__``` constructor also stores a set of parameters for each microscope: the pixel size, wavelength of the electron beam, spherical aberration constant, and the resolution achieved. Default values for these parameters are stored within a nested dictionary. Finally, the Microscopes class contains a help message to assist with parameter inputs by the user.  

The BoxSizeCalcs class inherits the properties of the Microscopes class to execute box size calculations. In this class, the function ```R``` takes all the inputs inherited from the Microscopes class to calculate a value for R that is given by the wavelength, defocus, resolution, and spherical aberration constant. 
The function ```finalBoxSize``` calculates a box size from R and particle diameter that is then compared with a range of ideal box sizes stored in ```list_of_boxes```. The final box size is determined as an ideal box size from the list that is the closest above the calculated box size. Returned along with the ideal box size are two minimum and maximum suggested box sizes for structure reconstruction.  

An additional function of the BoxSizeCalcs class is ```boxesPerGrid```. Given the known optimal box size and a known size of cryo-EM grids, this function predicts the possible number of particles for one grid that can be used to determine particle density and protein concentration for ideal data collection.  

## Instructions for use (high priority)

The code can be executed in terminal. To run the code, use the command  
```
python BoxSizeCalculations.py
```
which will give a box size calculation based on default parameters.  

To modify parameter values depending on the type of microscope used and size of particles imaged, input customized parameters at the end of the command. The code accepts the following flags:  

* --micro 'type of microscrope' (Default: Arctica)  
* --d 'diameter of particle' (Default: 150 Angstroms)  


__Example__  

For the microscope Arctica and particle diameter of 55 Angstroms, enter the command  

```bash
python BoxSizeCalculations.py --micro Arctica --d 55
```

Based on input parameters, the code will return an output displaying parameters used, calculated box sizes, and a boxes per grid calculation that predicts the total number of particles in a grid of a given size.  

__Example__  
```
############### Input Parameters ###############
Particle Diameter (Angstrom): 55.0
Microscope: Arctica
Maximum defocus value (nm): 2000.0
Maximum anticipated resolution (Angstrom): 3.50
################################################

############# THE FINAL BOX SIZES ##############
The optimal box size is: 384
The box size below the optimal is: 360
The box size above the optimal is: 416
################################################

########## Boxes Per Grid Calculation ##########
Assumes a circle that is 10X the box size
Possible number of boxes per grid: 56.0
################################################
```

For assistance with default and input parameters, access the help message with the following commmand:  
```
python EM_BoxCalculations.py -h
```

## Instructions for download

Two options:  

(1) Clone entire GitHub repository:  

SHOW  

(2) Just install an executable (a bit easier)  

```bash

echo "Installing BoxSize_exe.py file separately..." ;

echo "Must have wget installed" ;

wget https://raw.githubusercontent.com/Mill6159/EM_BoxSize_Prediction/main/Scripts/BoxSize_exe.py ;

echo "Dropping BoxSize_exe.py into /usr/local/bin and granting it executable permission" ;

cp BoxSize_exe.py /usr/local/bin ;
chmod u+x /usr/local/bin/BoxSize_exe.py ;

echo "Testing if install worked . . ." ;
echo "If the install works, it should return the help message!" ;

BoxSize_exe.py -h ;

```

## Log File (low priority - fun challenge or Rob will show you how)

**PS - Add this feature**

* Insert an image for the project (low priority but looks fancy)

```bash
![title](Images/example.png)
```
