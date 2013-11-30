# -*-coding:Latin-1 -*
import random
import pickle
import os
import random

def UpdateScores(player_name,player_sc):
	if os.path.isfile("donnees"):
		with open("donnees",'rb') as f_scores:
			my_unpickler = pickle.Unpickler(f_scores)
			score_p = my_unpickler.load()
	else:
		score_p = dict() 
	with open("donnees",'wb') as f_scores:
		score_p[player_name]=player_sc
		my_pickler = pickle.Pickler(f_scores)
		my_pickler.dump(score_p)	
		
def PrintScores():
	if os.path.isfile("donnees"):
		with open('donnees','rb') as f_scores:
			my_unpickler = pickle.Unpickler(f_scores)
			score_recovery = my_unpickler.load()
			print("*********Scores********")
			for joueur,score in score_recovery.items():
				print("    {} : {} ".format(joueur,score))
			print("***********************") 
	else:
		print("*********Scores********")
		print("No scores stored yet!") 
		print("***********************") 


def cleanUpScores():
	"""
	 to clean file
	"""
	if os.path.isfile("donnees"):
		os.remove("donnees") 

def convertASCII(L):
	my_word = L[0]
	my_word= my_word.lower()
	my_word= my_word.replace("é","e") 
	my_word= my_word.replace("è","e")
	my_word= my_word.replace("ê","e")
	my_word= my_word.replace("ë","e")
	my_word= my_word.replace("à","a")
	my_word= my_word.replace("ä","a")
	my_word= my_word.replace("â","a")
	my_word= my_word.replace("ç","c")
	my_word= my_word.replace("æ","ae")
	my_word= my_word.replace("ï","i")
	my_word= my_word.replace("î","i")
	my_word= my_word.replace("ö","o")
	my_word= my_word.replace("ù","u")
	my_word= my_word.replace("û","u")
	my_word= my_word.replace("ü","u")
	my_word= my_word.replace("ÿ","y")
	L[0] = my_word
	return my_word[0:len(my_word)-1].isalpha()

def pickword():
	with open("motsFR.txt",'r') as motsFR:
		listOfWords = motsFR.readlines()
		pos_my_word = random.randint(1,len(listOfWords))
		my_word = listOfWords[pos_my_word]
		L=[my_word]
		IsValid = convertASCII(L)
		while((len(L[0])-1) >8 or IsValid == False):
			pos_my_word = random.randint(1,len(listOfWords))
			my_word = listOfWords[pos_my_word]
			L=[my_word]
			IsValid = convertASCII(L)
	return L[0]

def RunGame(L,my_word):
	guessedW = L[0]
	chance = L[1]
	print("you have {} shots".format(chance))
	while(guessedW.find("*") != -1 and chance > 0):
		print("\nvotre mot est",guessedW)
		l = input("\nplease enter one letter: ")
		while(len(l)!=1 or l.isalpha() == False): #must be 1 caracter
			l = input("please enter one letter: ")
		l = l.lower()
		if(my_word.find(l) == -1):
			chance-=1
			print("\nyou have {} shots left".format(chance))
		else: #changing letter occurences		
			i=0
			for c in my_word:
				if c==l:
					guessedW = guessedW[0:i] +l+guessedW[i+1:]
				i+=1
	L[0] = guessedW
	L[1] = chance

def Start():
	player_name = input("veuillez saisir votre nom: ")
	my_word = pickword()
	guessedW = str()
	for i in range(1,len(my_word)):
		guessedW=guessedW+'*'

	chance = 8
	L=[guessedW,chance]
	RunGame(L,my_word)
	guessedW = L[0]
	chance = L[1]
	if(guessedW.find("*") != -1):
		print("You loose. the word you are looking for is:",my_word)
	else:
		print("Congrats! the word is:",guessedW)
	UpdateScores(player_name,chance)
	print("Your score is:",chance)
