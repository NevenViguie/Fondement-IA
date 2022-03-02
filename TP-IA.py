# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 13:04:57 2022

@author: neven
"""
def createGame():
    #0 = noir
    #1 = blanc
    #-1 = vide
    L=[]
    for i in range(8):
        L.append([])
        if(i!=3 and i!=4):
            for j in range(8):
                L[i].append("_")
        elif(i==3):
            L[i]=["_","_","_","B","N","_","_","_"]
        elif(i==4):
            L[i]=["_","_","_","N","B","_","_","_"]
    
    return L

def display(L):
    for i in range(len(L)):
        print(i, L[i])
    print("    0    1    2    3    4    5    6    7")

def getAdjacentCells(i,j):
    L=[]
    
    if(i>0):
        L.append((i-1,j))
        if(j>0):
            L.append((i-1,j-1))
            
    if(i+1<7):
        L.append((i+1,j))
        if(j+1<7):
            L.append((i+1,j+1))
            
    if(j>0):
        L.append((i,j-1))
        if(i<7):
            L.append((i+1,j-1))
        
    if(j+1<7):
        L.append((i,j+1))
        if(i>0):
            L.append((i-1,j+1))
    
    return L

def getAllPossibleMoves(k, L):
    #k est le joueur : 0 = noir, 1 = blanc
    C=[] #coups possibles                               
    
    if(k=="B"):
        for i in range(8):
            for j in range(8):
                if(L[i][j] == "B"):
                    A=getAdjacentCells(i, j)
                    for n in range(len(A)):
                        if(L[A[n][0]][A[n][1]]=="N"):
                            x=A[n][0]-i
                            y=A[n][1]-j
                            a=i+x
                            b=j+y
                            while(a>=0 and a<8 and b>=0 and b<8):
                                if(L[a][b]=="_"):
                                    C.append((a,b))
                                    break
                                if(L[a][b]=="B"):
                                    break
                                a+=x
                                b+=y
                            
    if(k=="N"):
        for i in range(8):
            for j in range(8):
                if(L[i][j] == "N"):
                    A=getAdjacentCells(i, j)
                    for n in range(len(A)):
                        if(L[A[n][0]][A[n][1]]== "B"):
                            x=A[n][0]-i
                            y=A[n][1]-j
                            a=i+x
                            b=j+y
                            while(a>=0 and a<8 and b>=0 and b<8):
                                if(L[a][b]=="_"):
                                    C.append((a,b))
                                    break
                                if(L[a][b]=="N"):
                                    break
                                a+=x
                                b+=y
                                
    return C
                               
def isFinished(compteTour, L):
    if "N" in L == False:
        print("Le joueur Noir a gagné la partie !!!")
        return True
    elif "B" in L == False:
        print("Le joueur Blanc a gagné la partie !!!")
        return True
    elif compteTour == 63:
        if L.count("N")>L.count("B"):
            print("Le joueur Noir a gagné la partie !!!")
        elif L.count("N")<L.count("B"):
            print("Le joueur Blanc a gagné la partie !!!")
        else :
            ("Partie terminée. Egalité !!!")
        return True
    else:
        return False

def isPlayable(i,j,k,L):
    if (i,j) in getAllPossibleMoves(k,L):
        return True
    else:
        return False

def move(k, L):
    print('Mouvements possibles : ', getAllPossibleMoves(k,L))
    i = int(input("Jouer en ligne : "))
    j = int(input("Jouer en colonne : "))
    while isPlayable(i,j,k,L) == False:
        print("Ce mouvement est impossible, veuillez saisir des valeurs correctes")
        print('Mouvements possibles : ', getAllPossibleMoves(k,L))
        i = input("Jouer en ligne : ")
        j = input("Jouer en colonne : ")
    L[i][j] = k
    return L

def play():
    L = createGame()
    display(L)
    compteTour= 1
    while isFinished(compteTour, L) == False:
        if compteTour % 2 == 0:
            print("Joueur Blanc, c'est votre tour")
            k="B"
            L=move(k, L)
        if compteTour % 2 == 1:
            print("Joueur Noir, c'est votre tour")
            k="N"
            L=move(k, L)
        display(L)
        compteTour += 1

#Code principal
play()        

 