echo "Installing BoxSize_exe.py file separately..." ;

echo "Must have wget installed" ;

wget https://raw.githubusercontent.com/Mill6159/EM_BoxSize_Prediction/main/Scripts/BoxSize_exe.py ;

echo "Dropping BoxSize_exe.py into /usr/local/bin and granting it executable permission" ;

cp BoxSize_exe.py /usr/local/bin ;
chmod u+x /usr/local/bin/BoxSize_exe.py ;

echo "Testing if install worked . . ." ;
echo "If the install works, it should return the help message!" ;

BoxSize_exe.py -h ;
