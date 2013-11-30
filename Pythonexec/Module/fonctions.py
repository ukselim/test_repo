# -*-coding:Latin-1 -*
import random
from Module.personne import *
#funtion: def, method: class.method()
def lambdaF():  #un moyen plus simple pr definir une fonction a une seule instruction
	ff= lambda x: x*x
	ff(5)
	print("lambda ff(5): ",ff(5))

#boucles et strucutre conditionnelles
def table(nb, max=10):
	"""Fonction affichant la table de multiplication par nb de 1 * nb jusqu'à max * nb """
	print("******les tables******")

	i = 0
	while i < max:
		print(i + 1, "*", nb, "=", (i + 1) * nb)
		i += 1
		if i == 24:
			print("Fin de la boucle, nombre secret")
			break
		elif i==1987:
			print("Fin de la boucle, nombre secret")
			continue # On retourne au while sans exécuter les autres lignes
        
def IsBisextile():
	annee=input("saisir une annee ")
	try: #if(type(annee) != int):
		annee = int(annee)		
		if annee==0:
			raise ValueError("l'année saisie est nulle")
		assert annee >= 0
	except AssertionError: # une assertion est une affirmation, une test d'une condition
    		print("L'année saisie est inférieure à 0.")
	#except NameError as exception_retournee: #as to put the error name into a variable and use it later
		#print("Une variable n'a pas été définie.",exception_retournee)
	except TypeError:
		print("type incompatible avec l'opération.")
	#except ZeroDivisionError:
	#	print("La variable denominateur est égale à 0.")
	else:	#else-> if  no exceptions do this: pour separer ce code du code du bloc try
		if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
			print("L'année saisie est")
		else:
			print("L'année saisie n'est pas")
		chaine = "bissextile"
		for lettre in chaine:
			print(lettre)
	finally: #ceci est executé qu'il y ait eu des erreurs ou non, meme si il y a un return dans l'exception
		print("Fin du programme: Annee Bisexsstile") 
		#pass: est un mot clé pour juste "try" un bloc d instruction mais ne pas capter l'exception
		#pass n'est pas un mot-clé propre aux exceptions : on peut également le trouver dans des conditions ou dans des fonctions que l'on souhaite laisser vides.

def Roulette():
		miseCl = input("Misez sur un nombre de 0 a 49: ")
		try:
			miseCl = int(miseCl)
		except ValueError as exception_retournee:
			print("Type saisie inconnue:",exception_retournee)
			
		while(type(miseCl) != int or miseCl<0 or miseCl>49):
			miseCl = input("Entree non de type entier ou hors intervalle, Misez sur un nombre de 0 a 49: ")
			try:
				miseCl = int(miseCl)
			except ValueError as exception_retournee:
				print("Type saisie inconnue:",exception_retournee)		
	
		mise = input("Combien payer vous en dallar? : ")
		try:
			mise = int(mise)
		except ValueError as exception_retournee:
			print("Type saisie inconnue:",exception_retournee)			
		while(type(mise) != int or mise<0):
			mise = input("Entree non de type entier, entrer la samme a miser: ")
			try:
				mise = int(mise)
			except ValueError as exception_retournee:
				print("Type saisie inconnue:",exception_retournee)	
				
		NBWinner = random.randint(1,100)
		print("random:",NBWinner)
		if NBWinner == miseCl:
			print("You won ",mise*2)
		elif ((NBWinner % 2 == 0 and miseCl % 2 == 0) or (NBWinner % 2 != 0 and miseCl % 2 != 0)):
			print("You won ",mise//2)
		else:
			print("You lost your ",mise,"$")

def affiche(prenom,nom,age):	
	print(" vous etes {0} et {1}, {3} !! vous avez {2} ans ".format(prenom, nom, age, nom.upper()))
	
	
#listes et chaines:

def Concat():
	nb=24031987
	chaine0 = str()
	chaine1 = str()
	chaine2 = str() # Crée une chaîne vide
	# On aurait obtenu le même résultat en tapant chaine = ""
	chaine1 = input("Inserrer une chaine1: ")
	chaine2 = input("Inserrer une chaine2: ")
	chaine3 = chaine1+" "+chaine2+" "+str(nb)
	print("chaine resultat",chaine3)
	
def string():
	print("******les chaines de caracteres******")
	chaine = str()
	chaine = input("Inserrer une chaine: ")
	i = 0 # On appelle l'indice 'i' par convention
	print("***boucle wile utilisant len et l'indexation [x]***")
	while i < len(chaine):
		print(chaine[i]) # On affiche le caractère à chaque tour de boucle
		i+=1
	print("***index introuvable***")
	try:
		chaine[i]
	except IndexError as exception:
		print("chaine[",i,"]: index introuvable: ",exception)
		
	print("chaine[0:len(chaine)-1]= ",chaine[0:len(chaine)-1])
	print("***replacement d'un element de la chaine***")
	chaine = "S" + chaine[1:]
	print("chaine = \"S\" + chaine[1:]= ",chaine)
	print("count str occurences in chaine:chaine.count(str)= ",chaine.count("e"))
	print("count str occurences in chaine:chaine.find(str)= ",chaine.find("e",4))
	print("count str occurences in chaine:chaine.replace(str)= ",chaine.replace("e","i"))

def leslistes():
	print("******les listes******")
	ma_liste1 = [1,2,3,4,5,6,[]]
	ma_liste1.append(56)
	ma_liste1.insert(1, 'c')
	ma_liste2=[7,8,9]
	ma_liste1.extend(ma_liste2)
	ma_liste3=[10]
	ma_liste1 += ma_liste3
	del ma_liste3
	del ma_liste2
	ma_liste1.remove('c')
	ma_liste1.remove(56)
	del ma_liste1[6]
	for i,element in enumerate(ma_liste1): #enumerate return two variables: position and value
		print(" element {} = {}".format(i,element))
	for element in enumerate(ma_liste1):
		print(element)

#tuples:


def tuples(): #À la différence des listes, les tuples, une fois créés, ne peuvent être modifiés : on ne peut plus y ajouter d'objet ou en retirer.
	print("******les tuples******")
	tuple_non_vide = (1, 3, 5)
	print("tuple_non_vide:",tuple_non_vide)

def afficher_flottant(nbr):
	if(type(nbr)==float):
		L  = str(nbr).split(".") #split gives back a  list
		L.append(L[1][:3])		
		del L[1]
		print(",".join(L)) # join renvoie une chaine str et la liste L doit absolument avoir que des chaines de caracteres
	else:
		print("donner un float")

def fonction_ParamNommée1(*parametres):   #python place les parametres dans un tuple
	print("J'ai reçu : {}.".format(parametres)) #every paramter
	
def fonction_ParamNommée2(nom, prenom, *commentaires,age=24):
	print("J'ai reçu comme parametre multiples : {}.".format(commentaires)) #every parameter but!! age, nom, prenom
	print("J'ai reçu parametre nommé age : ",age)
	print("J'ai reçu parametre nommé nom : ",nom)
	print("J'ai reçu parametre nommé  prenom: ",prenom)
	
def fonction_ParamNommée3(*en_liste, **en_dictionnaire):
	print("J'ai reçu comme parametre multiples : {}.".format(en_liste))
	print("J'ai reçu comme parametre multiples : {}.".format(en_dictionnaire))
	
def print2(commentaires1="",commentaires2="",*commentaires,sep=":", limit="******" ): # la variable commentaires avec * est un tuple (x parametres)
	# pour convertir le tuple en liste pour pouvoir faire des modifs 
	parametres = [commentaires1] 
	parametres.append(commentaires2)
	parametres.extend(list(commentaires))
	for i, parametre in enumerate(parametres): #convertir tous les elements de la liste en str
		parametres[i] = str(parametre)
	separator= " "+ sep + " "
	print(limit,separator.join(parametres),limit)
	#liste_des_parametres = [1, 4, 9, 16, 25, 36]
	#print(liste_des_parametres) # -> liste
	#print(*liste_des_parametres) # -> avec * ici, veux dir tout les elements d'entrée liste_des_parametres
	
#filtrage:Les compréhensions de liste:un moyen de filtrer ou modifier une liste très simplement
#il a une synthaxe bien définie

def inventaire():
	print("******les listes******")
	inventaire = [("pommes", 22),("melons", 4),("poires", 18),("fraises", 76),("prunes", 51)]
	#this way
	inventaire_2 = [(nbr,fruit) for fruit,nbr in  inventaire ]
	liste_triee0 = [(fruit,nbr) for nbr,fruit in sorted(inventaire_2,reverse=True) ]
	#OR this way
	liste_triee = sorted(inventaire,key=lambda student: student[1],reverse=True)
	print(liste_triee0)
	print(liste_triee)	
#sorting is done on first element of the list
#sort and sorted:La fonction retourne la liste triée sans modifier celle passée en paramètre
#Les parenthèses délimitent les tuples, les crochets délimitent les listes et les accolades {} délimitent les dictionnaires.

def dictionary_Functionnalities():
	print("******les dictionnaires******")
	mon_dictionnaire = dict()
	print(type(mon_dictionnaire))
	# ou bien mon_dictionnaire2 = {}
	mon_dictionnaire["mot de passe"] = "*"	
	mon_dictionnaire["pseudo"] = "6pri1"
	mon_dictionnaire["mot de passe"]	
	print("mon_dictionnaire[\"mot de passe\"]=",mon_dictionnaire["mot de passe"])
	mon_dictionnaire2 = {}
	mon_dictionnaire2[0] = "a"	
	mon_dictionnaire2[1] = "b"
	mon_dictionnaire2[2] = [1,2,3,4,5,6,[]]	
	mon_dictionnaire2[3] = ({1:"selim",2:24},"d","e")
	print("Dictionnaire a different type:",mon_dictionnaire2)
	try:
		print(mon_dictionnaire["passe"])
	except KeyError: #exception rises for invalid key used
		print("Clé invalide dans le dictionnaire")
	unset = {'pseudo', 'mot de passe'}
	undict = {'pseudo':3, 'mot de passe':5,"age":24}
	undict = {'pseudo':3, 'mot de passe':5,"age":24}
	undict2 = dict(pseudo=3, mot_de_passe=5, age=24) #  créer un dict en passant en paramètre de dict les clés et valeurs associées, sous la forme de paramètres nommés
	print("unset = {'pseudo', 'mot de passe'} est de : ",type(unset))
	print("undict = {'pseudo':3, 'mot de passe':5} est de : ",type(undict))
	print("undict2 = {'pseudo':3, 'mot de passe':5} est de : ",type(undict2))
	del undict["pseudo"]
	print(undict)
	print("suppresion du mod de passe qui est:",undict.pop("mot de passe"),",dictionnaire restant:",undict)
	for cle in mon_dictionnaire2.keys():
		print(cle)
	for Val in mon_dictionnaire2.values():
		print(Val)	
	print("Liste keys:",mon_dictionnaire2.keys())
	print("List values",mon_dictionnaire2.values())
	print("parcourir les elements du dic en mm tmp:")
	for i,j in mon_dictionnaire2.items():
		print("element {} = {} ".format(i,j))
import os
import pickle

def les_fichiers():
	print("******les fichiers******")
	print(os.getcwd())
	with open("module/fichier.txt", "r") as mon_fichier: #w, a for append, b: binaire, r+b, write in some position "file.seek"
		print(type(mon_fichier))
		contenu = mon_fichier.read()
		print(contenu)	
	with open("module/fichier.txt", "w") as mon_fichier:
		mon_fichier.write(str(1)+"abcs")
	print(mon_fichier.closed)
	with open('module/donnees', 'wb') as fichier:
		mon_pickler = pickle.Pickler(fichier)
		score = {"joueur 10":    5,"joueur 2":   35,"joueur 3":   20,"joueur 4":    2}
		mon_pickler.dump(score)
	with open('module/donnees','rb') as fichier:
		mon_unpickler = pickle.Unpickler(fichier)
		scorerecup = mon_unpickler.load() # on appelle load autant qu'on a d'objets dans le fichier, ici c'est un seul dictionnaire
	print(scorerecup)
	
def portabilite_referencement(a,b=[]):
	"""Fonction nous permettant de tester la portée des variables
	définies dans notre corps de fonction"""
	print("******la portée des variables******")
# On essaye d'afficher la variable var, si elle existe
# espace(set_var) appartient a l'espace(main) mais pas le contraire
# on ne peux jamais affecter une nouvelle valeur a un object mais on peut utiliser ses methodes pour modifier ses attributs.

# si l'object est un entier,string.. type simple! il ne peux pas etre modifié 
# en le passant par parametre a une fonction car ce sont des types immutables.
# pour le faire, on doit l'incruster dans une liste
	
	try:
		print("Avant l'affectation, notre variable var vaut {0}.".format(var))
	except NameError:
		print("La variable var n'existe pas encore.")
	var = a
	print("Après l'affectation, notre variable var vaut {0}.".format(var))
	
	
	ma_liste1 = [1, 2, 3]
	ma_liste2 = ma_liste1 #cela revient a referencer le meme object list [1,2,3]
	ma_liste3 = list(ma_liste1) # Cela revient à copier le contenu de ma_liste1
	ma_liste2.append(4)
	print(ma_liste1)
	print(ma_liste2)
	print(ma_liste3)

	ma_liste4 = [1, 2]
	ma_liste5 = [1, 2]
	if ma_liste4 == ma_liste5: # On compare le contenu des listes
		print("meme contenue de chaine",ma_liste5,ma_liste5)
	if ma_liste4 is not ma_liste5: # On compare leur référence
		print("la reference de {} et de {} est differente".format(ma_liste4,ma_liste5))		
	#modifier a et b et voir le resultat
	a=10
	b.append(6)
	del b[0]
		
def lesClasses():
	print("******les Classes******")
	TableauNoir.combien()
	a = TableauNoir()
	a.combien()
	
	print("tab.surface:",a.surface)
	a.ecrire("Coooool ! Ce sont les vacances !")
	print("tab.surface:",a.surface)
	TableauNoir.ecrire(a, "essai") #self<-l'objet
	print("tab.surface:",a.surface)
	a.afficher() # TableauNoir.afficher()
	print("\nToutes les methodes(d'instance,de classe et statiques) et attributs(d'instance et de classe):",dir(a)) #affiche les methodes et attributs d'une classe
	print("\n les valeurs des attibuts d'instance dans un dictionnaires:\n",a.__dict__)
	
	a.__dict__["surface"] = "XXXXXXXX" #en modifiant le dictionnaire de la classe, on modifie les objets
	print("tab.surface:",a.surface)
	print("//----------Accesseur mutateur------")
	print("a.lieu_residence",a.lieu_residence)
	a.lieu_residence = "Berlin"
	print("a.lieu_residence:",a.lieu_residence)
	print("definition de l'objet a=TableauNoir::",a) #meme methode que repr
	print("repr(a):",repr(a))
	print("a.lieu_residence:",a.lieu_residence) #l'appel des getters and setters speciaux se fait normalement, object.Attribute
	print("a.surface:",a.surface)
	print("a.e:",a.e)
	print(hasattr(a,"lieu_residence"))
	
def LesSurcharges():
	"""Les méthodes spéciales:
	Sont toutes entourées de deux signes « souligné » (_).
	__getattr__, __setattr__ et __delattr__ contrôlent l'accès aux attributs de l'instance.
	__getitem__, __setitem__ et __delitem__ surchargent l'indexation ([]).
	__add__, __sub__, __mul__… surchargent les opérateurs mathématiques.
	__eq__, __ne__, __gt__… surchargent les opérateurs de comparaison.
	"""
	print("******la surcharge avec des methodes speciales******")
	ZD = ZDict()
	ZD[1]="jdidi"
	ZD[2]="selim"
	ZD[3]="24"
	print("ZDict[\"1\"]=",ZD[1])
	del ZD[1]
	print("ZD=",ZD)
	print(type(ZD))
	print("ZD[\"0\"]: {}".format(ZD[0]))
	print("24 in ZD:","24" in ZD)
	print("length of ZD=",len(ZD))

	d=Duree(3,5)
	print(d)
	print("duree+ 4 seconde=",d+121)
	print("4 seconde+  duree =",121+d)
	
def heritage():
	"""On peut accéder aux méthodes de la classe mère directement via la syntaxe : ClasseMere.methode(self).
	raise ErreurAnalyseFichier("plop.conf", 34,
	"Il manque une parenthèse à la fin de l'expression")
	class MaClasseHeritee(MaClasseMere1, MaClasseMere2): la recherche d'une methode se fait ainsi:
	La methode est cherché dans MaClasseHeritee, puis dans MaClasseMere1, puis ses classes méres puis MaClasseMere2 puis ses classes meres
	"""
	agent = AgentSpecial("Fisher", "18327-121")
	print(agent)
	print(agent.prenom)
	print("issubclass(AgentSpecial, Personne)=",issubclass(AgentSpecial, Personne))
	print("issubclass(AgentSpecial, object)=",issubclass(AgentSpecial, object))
	print("issubclass(Personne, AgentSpecial)=",issubclass(Personne, AgentSpecial))
	print("isinstance(agent, AgentSpecial)=",isinstance(agent, AgentSpecial))
	print("isinstance(agent, Personne)=",isinstance(agent, Personne))
	er = ErreurAnalyseFichier("FixOrder.map","543"," duplicated function")
	print(er)