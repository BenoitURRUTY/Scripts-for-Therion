encoding  utf-8

# Licence
#
#<en> Released under a Creative Commons Attribution-ShareAlike-NonCommercial License:
#<fr> Publié sous la licence Creative Commons Attribution-ShareAlike-NonCommercial:
#     <http://creativecommons.org/licenses/by-nc-sa/4.0/>
#
# Written by: / Ecrit par : Benoît Urruty

PATH_SURVEY='/home/urrutyb/Documents/Spéléo/database_speleo/Chartreuse/Réseau_ded/topo_kriska/therion_kriska'

#script permettant de lancer l'ensemble des compilations therion pour un réseau
find $PATH_SURVEY/. -iname "thconfig" | while read line; do
	echo "Processing file '${line::-8}"
	cd "${line::-8}"
	therion thconfig
	#ligne à modifier en fonction de la racine
	cd $PATH_SURVEY
done
