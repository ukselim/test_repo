# -*-coding:Latin-1 -*
class TableauNoir:

	objets_crees= 0 #attribut de classe, identique a tout les objets de la classe
	def __init__(self): 	#Constructeur: il n'est pas vraiment obligatoire.
		#chaque fonction speciale a deux tiret bas, celle ci sert a definir les attributs
		"""� chaque fois qu'on cr�e un objet,
		on incr�mente le compteur"""
		TableauNoir.objets_crees+= 1
		self.surface = "\n salut! "		#self designe la classe, donc surface est un attribut de classe
		self._lieu_residence = "Paris" 
		# La convention veut qu'on n'acc�de pas, depuis l'ext�rieur de la classe, � un attribut commen�ant par un soulign� _
		
		
	def combien(cls):	#methode de classe
		print("Jusqu'� pr�sent, {} objets ont �t� cr��s.".format(cls.objets_crees))
	combien = classmethod(combien)	#pour que Python reconnaisse une m�thode de classe, il faut appeler la fonction classmethod et utiliser cls comme attribut 
	#classmethod est necessaire pour la definition
	def ecrire(self, message_a_ecrire):		# methode d'objet, methode d'instance, on utilise self
		if self.surface != "":
			self.surface += "\n"
		self.surface += message_a_ecrire
	
	def afficher():		#methode statique, ni self ni cls. ind�pendente de toute donn�e, contenue dans l'instance de l'objet et de la classe.
		print("On affiche la m�me chose.")
		print("peu importe les donn�es de l'objet ou de la classe.")
	afficher = staticmethod(afficher) #necessaire pour la declaration
	
	#l'access au mutateur et accesseur se fait soit en appellant la fonction ou directement la variable qui appellera la fonction
	#si l'le get ou le set n'est pas definit, l'objet ne pourra guerre etrre modif�!!
	def _get_lieu_residence(self):
		print("On acc�de � l'attribut lieu_residence:")
		return self._lieu_residence
	def _set_lieu_residence(self, nouvelle_residence):
		print("Attention, il semble que {} d�m�nage ")
		self._lieu_residence = nouvelle_residence
		# On va dire � Python que notre attribut lieu_residence pointe vers une
		# propri�t�
	lieu_residence = property(_get_lieu_residence, _set_lieu_residence)
	# lieu_residence = property(_get_lieu_residence, _set_lieu_residence,_effaceur_lieu_residence, _helperof_lieu_residence)
# Il s'agit de la d�finition d'une propri�t�. On lui dit que l'attribut lieu_residence (cette fois, sans signe soulign� _) doit �tre une propri�t�. On d�finit dans notre propri�t�, dans l'ordre, la m�thode d'acc�s (l'accesseur) et celle de modification (le mutateur).

	def __repr__(self):
		"""
		Definition de l'objet instance, qd on print l'objet directement, cette methode est appell�"""
		return "surface={},lieu_residence={} ".format(self.surface,self._lieu_residence)
	
	def __getattr__(self, nom):
		"""qd on fait objet.attribut=valeur, Si Python ne trouve pas l'attribut nomm� nom, il appelle
		cette m�thode"""
		print("Alerte ! Il n'y a pas d'attribut {} ici !".format(nom))
	
	def __setattr__(self, nom_attr, val_attr):
		""" objet.nom_attr = val_attr"""
		object.__setattr__(self, nom_attr, val_attr)
	
	def __hasattr__(self, nom): # Renvoie True si l'attribut "nom" existe, False sinon	
		"""qd on fait objet.attribut=valeur, Si Python ne trouve pas l'attribut nomm� nom, il appelle
		cette m�thode"""


class ZDict:
	"""Classe enveloppe d'un dictionnaire"""
	def __init__(self):
		"""Notre classe n'accepte aucun param�tre"""
		self._dictionnaire = {}
		
	def __setitem__(self, index, valeur): 
		"""objet[index] = valeur  ==== self._dictionnaire[index] = valeur"""
		self._dictionnaire[index] = valeur
	def __getitem__(self, index):
		"""on fait objet[index]  ====  self._dictionnaire[index]"""
		try:
			return self._dictionnaire[index]
		except:
			return "Indexe non valide!"
	def __delitem__(self, index):
		""""del objet[i] : l'object a i est supprim�"""
		print("suppression de {}".format(self._dictionnaire[index]))
		del  self._dictionnaire[index]
	def __repr__(self):
		"""
		Definition de l'objet instance, qd on print l'objet directement, cette methode est appell�"""
		return  "{}".format(self._dictionnaire)
	#*****									****#
	#	ma_liste = [1, 2, 3, 4, 5]						#
	#	8 in ma_liste Revient au m�me que  ma_liste.__contains__(8)		#
	#*****									****#

	def __contains__(self, object):
		"""
			si l'objet est dans le dictionnaire, return true
		"""
		return object in self._dictionnaire.values()
	def __len__(self):
		return len(self._dictionnaire)
	
class Duree:
	"""Classe contenant des dur�es sous la forme d'un nombre de minutes
	et de secondes"""
	def __init__(self, min=0, sec=0):
		"""Constructeur de la classe"""
		self.min = min # Nombre de minutes
		self.sec = sec # Nombre de secondes
	def __str__(self):
		"""Affichage un peu plus joli de nos objets"""
		return "{0:02}:{1:02}".format(self.min, self.sec) #formatage: tuple de 2 element, i:nombre de 0
	# d1 + 4 equivalent a d1.__add__(4), on redefinit add:
	def __add__(self,nombre):
		"""
		d'autres meethodes
		__sub__ : - ;
		__mul__ : * ;
		__truediv__ : / ;
		__floordiv__ : // (division enti�re) ;
		__mod__ : % (modulo) ;
		__pow__ : ** (puissance) ;
		__iadd__: += 
		__isub__: -=
		__eq__	: ==
		__ne__	: !=
		__gt__	: >
		__ge__	: >=
		__lt__	: <
		__le__	: <=
		"""
		nbr= self.sec+ nombre
		if(nbr >=60):
			self.min += nbr // 60
			self.sec = nbr % 60
		else:
			self.sec = nbr
		return "{0:02}:{1:02}".format(self.min, self.sec)
		
	def __radd__(self, objet_a_ajouter):
			"""Cette m�thode est appel�e si on �crit object1 + objet2 et que
			le premier objet ne sait pas comment ajouter
			le second. On redirige sur __add__ puisque
			"""			
			return self + objet_a_ajouter
			
class Temp:
	"""Classe contenant plusieurs attributs, dont un temporaire
	L'objectif que nous nous �tions fix� peut �tre atteint par ces deux m�thodes. 
	Soit notre classe met en �uvre une m�thode __getstate__, soit elle met en �uvre une m�thode __setstate__.
	
	Dans le premier cas, on modifie le dictionnaire des attributs avant la s�rialisation. 
	Le dictionnaire des attributs enregistr� est celui que nous avons modifi� avec la valeur 
	de notre attribut temporaire � 0.
	
	Dans le second cas, on modifie le dictionnaire d'attributs apr�s la d�s�rialisation. 
	Le dictionnaire que l'on r�cup�re contient un attribut attribut_temporaire avec une 
	valeur quelconque (on ne sait pas laquelle) mais avant de r�cup�rer l'objet, on met cette valeur � 0.
	
	A vous de choisir la tienne.
	"""
	
	def __init__(self):
		"""Constructeur de notre objet"""
		self.attribut_1 = "une valeur"
		self.attribut_2 = "une autre valeur"
		self.attribut_temporaire = 5
   	
	def __getstate__(self):
		"""Renvoie le DICTIONNAIRE D'ATTRIBUTS	 � s�rialiser"""
		dict_attr = dict(self.__dict__)
		dict_attr["attribut_temporaire"] = 0
		return dict_attr
	def __setstate__(self, dict_attr):
		"""M�thode appel�e lors de la d�s�rialisation de l'objet"""
		dict_attr["attribut_temporaire"] = 0
		self.__dict__ = dict_attr


class Personne:
    def __init__(self, nom):
        self.nom = nom
        self.prenom = "Martin"
    def __str__(self):
        return "{0} {1}".format(self.prenom, self.nom)

class AgentSpecial(Personne):
    def __init__(self, nom, matricule):
        Personne.__init__(self, nom)
        self.matricule = matricule
    def __str__(self):
        return "Agent {0}, matricule {1}".format(self.nom, self.matricule)
       
       

#Cree sa propre exception
class ErreurAnalyseFichier(Exception):
    """ fichier -- le nom du fichier posant probl�me
        ligne -- le num�ro de la ligne posant probl�me
        message -- le probl�me proprement dit"""
    
    def __init__(self, fichier, ligne, message):
        self.fichier = fichier
        self.ligne = ligne
        self.message = message
    def __str__(self):
        """Affichage de l'exception"""
        return "[fichier {}, ligne {}]:{}".format(self.fichier,self.ligne,self.message)
