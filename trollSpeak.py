#   trollSpeak v1.0
#   by kris dreemurr
#   v0.3 - initial version, contains quirks for kanaya, terezi, and vriska.
#   v0.6 - added gamzee, eridan, and sollux. rewrote clipboard bits so as to make use of a less inconvenient library.
#   v0.6.1 - fixed a bug in eridan's quirk.
#   v1.0 - all of the beta trolls have been added. some issues with capitalization have been fixed. not all possible puns have been added yet; these will come in future updates. 

import keyword
import clipboard
import os
from multiprocessing.sharedctypes import Value
from random import randrange

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
def aradiaSpeak():
    i = 1
    while(i == 1):
        
        a_string = input()
        if a_string == "quit()":
            i = 0
        else:
            a_string = a_string.replace("o","0")
            a_string = a_string.replace("O","0")
            print(a_string)
            clipboard.copy(a_string)
            
def equiusSpeak():
    i = 1
    while(i == 1):
    
        a_string = input()
        if a_string == "quit()":
            i = 0
        else:
            a_string = "D --> " + a_string
            a_string = a_string.replace("x","%")
            a_string = a_string.replace("ool","001")
            a_string = a_string.replace("OOL","001")
            a_string = a_string.replace("loo","100")
            a_string = a_string.replace("LOO","100")
            a_string = a_string.replace("blue","b100")
            a_string = a_string.replace("BLUE","B100")
            a_string = a_string.replace("strongest","STRONGEST")
            a_string = a_string.replace("stronger","STRONGER")
            a_string = a_string.replace("strong","STRONG")
            a_string = a_string.replace("structure","stru%ure")
            a_string = a_string.replace("misdirection","misdire%ion")
            a_string = a_string.replace("topics","topi%")
            a_string = a_string.replace("cross","%")
            a_string = a_string.replace("doublecross","%%")
            a_string = a_string.replace("double cross","%%")
            a_string = a_string.replace("sakes","sa%es")
            a_string = a_string.replace("STRUCTURE","STRU%URE")
            a_string = a_string.replace("MISDIRECTION","MISDIRE%ION")
            a_string = a_string.replace("TOPICS","TOPI%")
            a_string = a_string.replace("CROSS","%")
            a_string = a_string.replace("DOUBLECROSS","%%")
            a_string = a_string.replace("DOUBLE CROSS","%%")
            a_string = a_string.replace("SAKES","SA%ES")
            print(a_string)
            clipboard.copy(a_string)

def eridanSpeak():
    i = 1
    while(i == 1):

        a_string = input()
        if a_string == "quit()":
            i = 0
        else: 
            a_string = a_string.replace("w","ww")
            a_string = a_string.replace("v","vv")
            a_string = a_string.replace("ing ","in ")
            a_string = a_string.replace("W","WW")
            a_string = a_string.replace("V","VV")
            a_string = a_string.replace("ING ","IN ")
            print(a_string)
            clipboard.copy(a_string)
            
def feferiSpeak():
    i = 1
    while(i == 1):
        
        a_string = input()
        if a_string == "quit()":
            i = 0
        else:
            a_string = a_string.replace("h","}{")
            a_string = a_string.replace("H","}{")
            a_string = a_string.replace("E","-E")
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
            
def karkatSpeak():
    i = 1
    while(i == 1):
        
        a_string = input()
        if a_string == "quit()":
            i = 0
        else:
            print(a_string.upper())
            clipboard.copy(a_string.upper())
            
def nepetaSpeak():
    i = 1
    while(i == 1):
        
        a_string = input()
        if a_string == "quit()":
            i = 0
        else:
            a_string = ":33 < " + a_string
            a_string = a_string.replace("ee","33")
            a_string = a_string.replace("EE","33")
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
            a_string = a_string.replace("I","II")
            a_string = a_string.replace("S","2")
            a_string = a_string.replace(" TO "," TWO ")
            a_string = a_string.replace(" TOO "," TWO ")
            print(a_string)
            clipboard.copy(a_string)
            
def tavrosSpeak():
    i = 1
    while(i == 1):
    
        a_string = input()
        if a_string == "quit()":
            i = 0
        else:
            print(a_string.swapcase())
            clipboard.copy(a_string.swapcase())
            
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
            a_string = a_string.replace("ATE","8")
            a_string = a_string.replace("AIT","8")
            a_string = a_string.replace("ATION","8TION")
            a_string = a_string.replace("RELATABLE","REL8A8LE")
            a_string = a_string.replace("GREAT","GR8")
        print(a_string)
        clipboard.copy(a_string)

i = 1		
while(i == 1):
    
    cls()
    print("select a troll: ")
    a_string = input()
    if a_string == "quit()":
        i = 0
    elif a_string == "Aradia" or a_string == "aradia":
        print("\n----------------\n")
        aradiaSpeak()
    elif a_string == "Equius" or a_string == "equius":
        print("\n----------------\n")
        equiusSpeak()
    elif a_string == "Eridan" or a_string == "eridan":
        print("\n----------------\n")
        eridanSpeak()
    elif a_string == "Feferi" or a_string == "feferi":
        print("\n----------------\n")
        feferiSpeak()
    elif a_string == "Gamzee" or a_string == "gamzee":
        print("\n----------------\n")
        gamzeeSpeak()
    elif a_string == "Kanaya" or a_string == "kanaya":
        print("\n----------------\n")
        kanayaSpeak()
    elif a_string == "Karkat" or a_string == "karkat":
        print("\n----------------\n")
        karkatSpeak()
    elif a_string == "Nepeta" or a_string == "nepeta":
        print("\n----------------\n")
        nepetaSpeak()
    elif a_string == "Sollux" or a_string == "sollux":
        print("\n----------------\n")
        solluxSpeak()
    elif a_string == "Tavros" or a_string == "tavros":
        print("\n----------------\n")
        tavrosSpeak()
    elif a_string == "Terezi" or a_string == "terezi":
        print("\n----------------\n")
        tereziSpeak()
    elif a_string == "Vriska" or a_string == "vriska":
        print("\n----------------\n")
        vriskaSpeak()
    
