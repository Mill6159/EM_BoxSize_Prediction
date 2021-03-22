# Predicting the ideal box size for EM structure determination  
* References:   
__(1)__  
__(2)__  two undescores = bolded

_(3)_ one underscore = italics

## Summarized derivation (low priority)   

## Code workflow  (high priority)  

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

To trouble shoot, access the help message with the following commmand:
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
