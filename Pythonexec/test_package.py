# -*-coding:Latin-1 -*
#*********************Importations***********************
import os
#from Module.fonctions import IsBisextile
#from Module.fonctions import table
from Module.fonctions import *
#import Module.fonctions
import math as mathematiques


#********************************************************
#print(help("sorted"))
#it's better to define a class with attribute to make some variable global
#and not using 'golbal' 
def inc_i():
	"""Fonction charg?e d'incr?menter i de 1"""
	global i # Python recherche i en dehors de l'espace local de la fonction
	i += 1
	
	
FonctionsSiteDuZero = dict()
FonctionsSiteDuZero["lambdaF"]=lambdaF
#fonctions.table(6)
#mathematiques.table(7)
FonctionsSiteDuZero["IsBisextile"]=IsBisextile
FonctionsSiteDuZero["table"]=table #(5,100)
FonctionsSiteDuZero["table"]=table #(6)
FonctionsSiteDuZero["Roulette"]=Roulette
FonctionsSiteDuZero["affiche"]=affiche #("selim","jdidi",21)
FonctionsSiteDuZero["Concat"]=Concat
FonctionsSiteDuZero["string"]=string
FonctionsSiteDuZero["leslistes"]=leslistes
FonctionsSiteDuZero["tuples"]=tuples
FonctionsSiteDuZero["afficher_flottant"]=afficher_flottant #(4879.100008)
#parametres nommé, (x=valeur)
FonctionsSiteDuZero["fonction_ParamNommée1"]=fonction_ParamNommée1 #("selim","jdidi","lim","sl","fc") ->n'accepte pas les parametres nommé
FonctionsSiteDuZero["fonction_ParamNommée2"]=fonction_ParamNommée2 #("selim","jdidi","lim","sl","fc",age=25) ->les parametres nommé doivent etre specifié!
FonctionsSiteDuZero["fonction_ParamNommée3"]=fonction_ParamNommée3 #accepte tout type de parametres (nommé, non nommé)
liste_des_parametres = [1, 4, 9, 16, 25, 36]
FonctionsSiteDuZero["print2"]=print2 #("resultat:",*liste_des_parametres)
#dict_to_param_nommé = {"sep":" :: ", "limit":"*******\n"}
#FonctionsSiteDuZero["print2"]("selim","jdidi",**dict_to_param_nommé)
FonctionsSiteDuZero["inventaire"]=inventaire
FonctionsSiteDuZero["dictionary_Functionnalities"]=dictionary_Functionnalities
FonctionsSiteDuZero["les_fichiers"]=les_fichiers
a = 5 #portabilité
b=[5] #liste contenant un entier
FonctionsSiteDuZero["portabilite_referencement"]=portabilite_referencement #("selim")
i=1 # inc_i
FonctionsSiteDuZero["inc_i"]=inc_i
FonctionsSiteDuZero["lesClasses"]=lesClasses
FonctionsSiteDuZero["LesSurcharges"]=LesSurcharges
FonctionsSiteDuZero["heritage"]=heritage
heritage
#************Executer unve fonction du dictionnaire************

try:
	FonctionsSiteDuZero["heritage"]()
	print("")	
	#print("nouvelle a=",a)	
	#print("nouvelle b=",b[0])	
	#print("inc_i, i=",i)
except KeyError: #exception rises for invalid key used
	print("Fonction Inconnue")


#**************************Les classes************************


		

os.system("pause")