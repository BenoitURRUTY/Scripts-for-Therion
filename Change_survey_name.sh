if [ -z "$1" ]
then
      echo "\$var is empty"
      echo "Old name"
      read OLDNAME 
else
      echo "\$var is NOT empty"
      OLDNAME=$1
fi
if [ -z "$2" ]
then
      echo "\$var is empty"
      echo "Give name to your survey"
      echo "New name"
      read NEWNAME
else
      echo "\$var is NOT empty"
      NEWNAME=$2
fi

for f in *.th; do mv -- "$f" "${f//$OLDNAME/$NEWNAME}";done 
sed -i "s/$OLDNAME/$NEWNAME/g" *.th
sed -i "s/$OLDNAME/$NEWNAME/g" thconfig
cd Data
for f in *; do mv -- "$f" "${f//$OLDNAME/$NEWNAME}";done 
#sed -i "s/$OLDNAME/$NEWNAME/g" *
cd ..
