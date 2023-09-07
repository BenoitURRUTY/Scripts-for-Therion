# encoding  utf-8

# Licence
#
#<en> Released under a Creative Commons Attribution-ShareAlike-NonCommercial License:
#<fr> Publié sous la licence Creative Commons Attribution-ShareAlike-NonCommercial:
#     <http://creativecommons.org/licenses/by-nc-sa/4.0/>
#
# Written by: / Ecrit par : Benoît Urruty

PATH_TEMPLATE='/home/urrutyb/Documents/therion/Script_Therion'

if [ -z "$1" ]
then
      echo "\$var is empty"
      echo "Give name to your survey"
      read S
else
      echo "\$var is NOT empty"
      S=$1
fi

echo "Creating survey folder for : $S"
mkdir $S
cd $S
mkdir Outputs
mkdir Data

sed "s/<CAVENAME>/$S/g" ${PATH_TEMPLATE}/Therion_files_pattern/CAVENAME-maps.th > ${S}-maps.th
sed "s/<CAVENAME>/$S/g" ${PATH_TEMPLATE}/Therion_files_pattern/CAVENAME-tot.th > ${S}-tot.th
sed "s/<CAVENAME>/$S/g" ${PATH_TEMPLATE}/Therion_files_pattern/thconfig > thconfig

touch Data/${S}-coupe.th2
touch Data/${S}-plan.th2
cd ..
