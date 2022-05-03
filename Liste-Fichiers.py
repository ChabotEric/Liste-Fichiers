# -*-coding:utf-8  -*
# Version 1.0
# Auteur: Eric Chabot
# Programme pour lister les fichiers contenus dans un répertoire.
# La liste est écrite dans un fichier: "Liste_des_Fichiers.txt".
# Copier ListDir.exe dans le répertoire à lister et l'exécuter.

import os

# Écris la liste dans la variable fichier.
fichier = os.listdir()

# Supprime  "ListDir.exe" de la liste.
if "ListDir.exe" in fichier:
	fichier.remove("ListDir.exe")

# Ouvre un fichier texte et y inscrit chacun des fichiers du répertoire	
mon_fichier = open("Liste_des_Fichiers.txt", "w")
for i in fichier:
	if os.path.isfile(i):
		mon_fichier.write(i + "\n")

# ferme le fichier texte		
mon_fichier.close()
