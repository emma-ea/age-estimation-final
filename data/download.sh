# run to download dataset if it isn't local on machine

#!/bin/sh

!wget http://158.109.8.102/AppaRealAge/appa-real-release.zip
!mkdir data_dir 
!unzip appa-real-release.zip -d data_dir

