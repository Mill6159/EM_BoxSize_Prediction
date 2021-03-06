For questions or issues with the code, please reach out to Rob Miller (rcm347@cornell.edu).

# Predicting the ideal box size for EM structure determination  
* References:   
__(1)__  Rosenthal, Peter B., and Richard Henderson. ‘Optimal determination of particle orientation, absolute hand, and contrast loss in single-particle electron cryomicroscopy.’ Journal of molecular biology 333.4 (2003): 721-745.  
__(2)__  https://www.jiscmail.ac.uk/cgi-bin/webadmin?A2=ccpem;e433702b.1412  
__(3)__  https://math.stackexchange.com/questions/3007527/how-many-squares-fit-in-a-circle

## Summarized derivation 

The box size prediction was derived based on the result from Rosenthal et al., 2003, which states that the optimal box size for cryo electron microscopy 3D particle reconstruction should obey the following relationship:  

<img src="https://latex.codecogs.com/svg.latex?BoxSize&space;\geq&space;ParticleDiameter&space;&plus;&space;2R" title="BoxSize \geq Particlediameter + 2R" /></a>
 
<img src="https://latex.codecogs.com/svg.latex?R&space;=&space;\lambda&space;\Delta&space;f\mu&space;&plus;C{s}&space;\lambda^{3}\mu^{3}" title="R = \lambda \Delta f\mu +C{s} \lambda^{3}\mu^{3}" /></a>  
 
 where R represents the displacement of the most defocused image when the resolution spacing in the reconstruction is at maximum. R is given by two aberration terms: defocus and spherical aberration. The defocus term is expressed by <a href="https://www.codecogs.com/eqnedit.php?latex=\lambda&space;\Delta&space;f\mu" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\lambda&space;\Delta&space;f\mu" title="\lambda \Delta f\mu" /></a>, where <a href="https://www.codecogs.com/eqnedit.php?latex=\lambda" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\lambda" title="\lambda" /></a> is the energy of the electron beam, <a href="https://www.codecogs.com/eqnedit.php?latex=\Delta&space;f" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\Delta&space;f" title="\Delta&space;f" /></a> is defocus, and <img src="https://latex.codecogs.com/svg.latex?\mu&space;=&space;[1/m]" title="\mu = [1/m]" /></a> where m is the highest expected resolution. As a result of defocus, the particle image of resolution m is displaced by a distance of <img src="https://latex.codecogs.com/svg.latex?\lambda&space;\Delta&space;f/m" title="\lambda \Delta f/m" /></a>. The spherical aberration term is given by <img src="https://latex.codecogs.com/svg.latex?C{s}&space;\lambda^{3}\mu^{3}" title="C{s}&space;\lambda^{3}\mu^{3}" /></a>, where <img src="https://latex.codecogs.com/svg.latex?C{s}" title="C{s}" /></a>, the spherical aberration constant, along with wavelength and spatial frequency, accounts for the spatial incoherences of the electron beam due to the objective lens.  
 
      
## Code workflow 

This code was built using object-oriented programming in python3.8.x. Objects are created under two classes: class ```Microscopes``` and class ```BoxSizeCalcs```. The Microscopes class defines objects that contain all information about the microscope. The ```__init__``` constructor defines parameters for the microscope: the type of microscope used, estimated diameter of particles imaged in the microscope, and the lowest and highest defocus values for data collection. The values for these parameters are provided by default for the microscope Arctica and a particle diameter of 15 angstroms, but can be inputted by the user depending on the type of microscope used and other experimental conditions. The ```__init__``` constructor also stores a set of parameters for each microscope: the pixel size, wavelength of the electron beam, spherical aberration constant, and the resolution achieved. Default values for these parameters are stored within a nested dictionary. Finally, the Microscopes class contains a help message to assist with parameter inputs by the user.  

The BoxSizeCalcs class inherits the properties of the Microscopes class to execute box size calculations. In this class, the function ```R``` takes all the inputs inherited from the Microscopes class to calculate a value for R that is given by the wavelength, defocus, resolution, and spherical aberration constant. 
The function ```finalBoxSize``` calculates a box size from R and particle diameter that is then compared with a range of ideal box sizes stored in ```list_of_boxes```. The final box size is determined as an ideal box size from the list that is the closest above the calculated box size. Returned along with the ideal box size are two minimum and maximum suggested box sizes for structure reconstruction.  

An additional function of the BoxSizeCalcs class is ```boxesPerGrid```. Given the known optimal box size and a known size of cryo-EM grids, this function predicts the possible number of particles for one grid that can be used to determine particle density and protein concentration for ideal data collection.  

## Instructions for use

The code can be executed in terminal. To run the code, use the command  
```
python BoxSizeCalculations.py
```
which will give a box size calculation based on default parameters.  

To modify parameter values depending on the type of microscope used and size of particles imaged, input customized parameters at the end of the command. The code accepts the following flags:  

* -h, --help: 'help message' 
* -m, --micro: 'type of microscrope' 
  * (Default: Arctica)  
* -d, --diameter: 'diameter of particle' 
  * (Default: 50 Angstroms)  
* -ld, --lowdefocus: 'low defocus value' 
  * (Default: 1000 nanometers)  
* -hd, --highdefocus: 'high defocus value' 
  * (Default: 2000 nanometers)  
* -hr, --highresolution: 'highest anticipated resolution' 
  * (Defaults: Arctica: 3.5 Angstroms; Krios: 2.0 Angstroms; Polara: 4.0 Angstroms)  


__Example__  

For the microscope Arctica and particle diameter of 55 Angstroms, enter the command  

```bash
python BoxSizeCalculations.py --micro Arctica -d 55
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

* Must have git installed locally  
* Function _git pull_ will allow you to update code as we update it.

```bash
git clone https://github.com/Mill6159/EM_BoxSize_Prediction.git
```

Periodically run the command _git pull_ to update the code from the repository.  

(2) Just install an executable. This makes the box size calculation function universally accessible on your local computer. (i.e. type python BoxSize_exe.py from any directory). 

* This process will only work for MacOS systems.  

```bash

echo "Installing BoxSize_exe.py file separately..." ;

echo "Must have wget installed" ;

wget https://raw.githubusercontent.com/Mill6159/EM_BoxSize_Prediction/main/Scripts/BoxSize_exe.py ;

echo "Dropping BoxSize_exe.py into /usr/local/bin and granting it executable permission" ;

cp BoxSize_exe.py /usr/local/bin ;
chmod u+x /usr/local/bin/BoxSize_exe.py ;

echo "Testing if install worked . . ." ;
echo "If the install works, it should return the help message" ;

BoxSize_exe.py -h ;

```









