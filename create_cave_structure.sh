# encoding  utf-8

# Licence
#
#<en> Released under a Creative Commons Attribution-ShareAlike-NonCommercial License:
#<fr> Publié sous la licence Creative Commons Attribution-ShareAlike-NonCommercial:
#     <http://creativecommons.org/licenses/by-nc-sa/4.0/>
#
# Written by: / Ecrit par : Benoît Urruty
#

PATH_TEMPLATE='/home/urrutyb/Documents/therion/Therion_survey'

if [ -z "$1" ]
then
      echo "\$var is empty"
      echo "Give name to your cave system"
      read SN
else
      echo "\$var is NOT empty"
      SN=$1
fi

echo "Your are creating a folder for a whole cave system named : $SN "

#Create the main folder
mkdir $SN
cd $SN
mkdir Outputs
#Create a folder for GIS data
mkdir GIS
#Ask for the name of your first survey in your cave system
echo "name of your first survey"
read FS
#create the folder for the survey
. ${PATH_TEMPLATE}/create_survey.sh $FS
#copy the config file for drawing
cp ${PATH_TEMPLATE}/Therion_files_pattern/config.thc .
#legend folder will contain the entrance coordinate or other information you want to add in legend
mkdir legendes
sed "s/<RESEAUNAME>/$SN/g" ${PATH_TEMPLATE}/Therion_files_pattern/entrances_coordinates.th > legendes/entrances_coordinates.th

#personnal script for running all at once
cp ${PATH_TEMPLATE}/Therion_files_pattern/run_all.sh ../.

#this file will merge the map of the different survey, here you just initiase it with the first survey name
sed -e "s/<RESEAUNAME>/$SN/g" -e "s/<CAVENAME>/$FS/g" ${PATH_TEMPLATE}/Therion_files_pattern/Maps.th > Maps.th

#file for compiling the cave system
sed "s/<RESEAUNAME>/$SN/g" ${PATH_TEMPLATE}/Therion_files_pattern/system.thconfig > thconfig
sed -e "s/<RESEAUNAME>/$SN/g" -e "s/<CAVENAME>/$FS/g" ${PATH_TEMPLATE}/Therion_files_pattern/RESEAUNAME.th > ${SN}.th
sed "s/<RESEAUNAME>/"$SN"/g" ${PATH_TEMPLATE}/Therion_files_pattern/atlas.thconfig > atlas.thconfig
cp ../create_survey.sh .

cd ..