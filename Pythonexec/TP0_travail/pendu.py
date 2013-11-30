# -*-coding:Latin-1 -*
import os
from fonctions import *

Exit = True
while (Exit  == True):
	print("**********************")
	print("**********Menu********")
	print("1-start new game")
	print("2-Show scores")
	print("3-Help")
	print("4-Exit")
	print("5-Cean up base scores")
	print("**********************")
	print("**********************")

	select = input()
	os.system("cls")
	if(select == "1"):
		Start()
	elif (select == "2"):
		PrintScores()
	elif (select == "3"):
		print("Game rules:")
		print("you have to guess a word given to you")
		print("you have only 8 short and 8 points to win in the end")
		print("7 shots left? 7 points  you win, etc...")
	elif (select == "4"):
		Exit = False
	elif (select == "5"):
		cleanUpScores()
	
os.system("pause")