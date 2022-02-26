#	trollSpeak v0.6
#	by kris dreemurr
#	v0.3 - initial version, contains quirks for kanaya, terezi, and vriska.
#   	v0.6 - added gamzee, eridan, and sollux. rewrote clipboard bits so as to make use of a less inconvenient library. 

import keyword
import clipboard
from multiprocessing.sharedctypes import Value
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def eridanSpeak():
	i = 1
	while(i == 1):

		a_string = input()
		if a_string == "quit()":
			i = 0
		else: 
			a_string = a_string.replace("w","ww")
			a_string = a_string.replace("v","vv")
			a_string = a_string.replace("ing","in")
			print(a_string)
			clipboard.copy(a_string)

def gamzeeSpeak():
	i = 1
	while(i == 1):

		a_string = input()
		if a_string == "quit()":
			i = 0
		else: 
			gamzee = ""

			for idx in range(len(a_string)):

				if not idx % 2 :

				   gamzee = gamzee + a_string[idx].lower()

				else:

				   gamzee = gamzee + a_string[idx].upper()

			print(gamzee)
			clipboard.copy(gamzee)

def kanayaSpeak():
	i = 1
	while(i == 1):
	
		a_string = input()
		if a_string == "quit()":
			i = 0
		else:
			a_string = a_string.title()
			print(a_string)
			clipboard.copy(a_string)

def solluxSpeak():
	i = 1
	while(i == 1):

		a_string = input()
		if a_string == "quit()":
			i = 0
		else: 
			a_string = a_string.replace("i","ii")
			a_string = a_string.replace("s","2")
			a_string = a_string.replace(" to "," two ")
			a_string = a_string.replace(" too "," two ")
			print(a_string)
			clipboard.copy(a_string)
            
def tereziSpeak():
	i = 1
	while(i == 1):
	
		a_string = input()
		if a_string == "quit()":
			i = 0
		else:
			a_string = a_string.replace("A","4")
			a_string = a_string.replace("I","1")
			a_string = a_string.replace("E","3")
			a_string = a_string.replace("a","4")
			a_string = a_string.replace("i","1")
			a_string = a_string.replace("e","3")
			print(a_string.upper())
			clipboard.copy(a_string.upper())

def vriskaSpeak():
	i = 1
	while(i == 1):
		
		a_string = input()
		if a_string == "quit()":
			i = 0
		else: 
			a_string = a_string.replace("B","8")
			a_string = a_string.replace("b","8")
			a_string = a_string.replace("ate","8")
			a_string = a_string.replace("ait","8")
			a_string = a_string.replace("ation","8tion")
			a_string = a_string.replace("relatable","rel8a8le")
			a_string = a_string.replace("great","gr8")
			print(a_string)
			clipboard.copy(a_string)

i = 1		
while(i == 1):
	
	cls()
	print("select a troll: ")
	a_string = input()
	if a_string == "quit()":
		i = 0
	elif a_string == "Eridan" or a_string == "eridan":
		print("\n----------------\n")
		eridanSpeak()
	elif a_string == "Gamzee" or a_string == "gamzee":
		print("\n----------------\n")
		gamzeeSpeak()
	elif a_string == "Kanaya" or a_string == "kanaya":
		print("\n----------------\n")
		kanayaSpeak()
	elif a_string == "Sollux" or a_string == "sollux":
		print("\n----------------\n")
		solluxSpeak()
	elif a_string == "Terezi" or a_string == "terezi":
		print("\n----------------\n")
		tereziSpeak()
	elif a_string == "Vriska" or a_string == "vriska":
		print("\n----------------\n")
		vriskaSpeak()
	
