# Predicting the ideal box size for EM structure determination  
* References:   
__(1)__  
__(2)__  two undescores = bolded

_(3)_ one underscore = italics

## Summarized derivation (low priority)   

## Code workflow  (high priority)  

## Instructions for use (high priority)

The code accepts the following flags:  

* --micro 'type of microscrope' (Default: Arctica)  
* --d 'diameter of particle' (Default: 150 Angstroms)  

to run the code do x,y, and sometimes z



__Example__  

```bash
python BoxSizePrediction.py --micro Arctica --d 55
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
