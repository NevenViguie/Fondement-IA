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
@ -121,16 +120,187 @@ def isPlayable(i,j,k,L):
    else:
        return False

def convertTaken(i, j, k, L):
    if(k=="B"):
        #Parcours Nord
        if L[i+1][j]=="N":#Gérer l'exception out of range
            for x in range(i+1, 8):
                if L[x][j]=="_":
                    break
                if L[x][j]=="B":
                    for l in range(i+1,x):
                        L[l][j]="B"
                        break

        #Parcours Sud
        if L[i-1][j]=="N":
            for x in range(i-1, -1,-1):
                if L[x][j]=="_":
                    break
                if L[x][j]=="B":
                    for l in range(i-1,x,-1):
                        L[l][j]="B"
                        break

        #Parcours Est            
        if L[i][j+1]=="N":
            for x in range(j+1, 8):
                if L[i][x]=="_":
                    break
                if L[i][x]=="B":
                    for l in range(x,j+1):
                        L[i][l]="B"
                        break
        #Parcours Ouest       
        if L[i][j-1]=="N":
            for x in range(j-1, -1,-1):
                if L[i][x]=="_":
                    break
                if L[i][x]=="B":
                    for l in range(x,j-1,-1):
                        L[i][l]="B"
                        break
        #Parcours Sud Est
        if L[i+1][j+1]=="N":
            for x in range(i+1, 8):
                if L[x][x]=="_":
                    break
                if L[x][x]=="B":
                    for l in range(i+1,x):
                        L[l][l]="B"
                        break
        #Parcours Sud Ouest
        if L[i+1][j-1]=="N":
            for x in range(i+1, 8):
                for y in range(i-1,-1,-1):
                    if L[x][y]=="_":
                        break
                    if L[x][y]=="B":
                        for l in range(i+1,x):
                            for m in range(j-1,y,-1):
                                L[l][m]="B"
                                break
        #Parcours Nord Est
        if L[i-1][j+1]=="N":
            for x in range(i-1, -1,-1):
                for y in range(i+1,8):
                    if L[x][y]=="_":
                        break
                    if L[x][y]=="B":
                        for l in range(i-1,x,-1):
                            for m in range(j+1,y):
                                L[-l][l]="B"
                                break
        #Parcours Nord Ouest
        if L[i-1][j-1]=="N":
            print('Nord Ouest')
            for x in range(i-1, -1,-1):
                if L[x][x]=="_":
                    break
                if L[x][x]=="B":
                    print("on passe par là")
                    for l in range(i-1,x,-1):
                        L[l][l]="B"
                        break
    if(k=="N"):
        #Parcours Nord
        if L[i+1][j]=="B":
            print("Nord")
            for x in range(i+1, 8):
                if L[x][j]=="_":
                    break
                if L[x][j]=="N":
                    for l in range(i+1,x):
                        L[l][j]="N"
                        break

        #Parcours Sud
        if L[i-1][j]=="B":
            print("Sud")
            for x in range(i-1, -1,-1):
                if L[x][j]=="_":
                    break
                if L[x][j]=="N":
                    for l in range(i-1,x,-1):
                        L[l][j]="N"
                        break            

        #Parcours Est          
        if L[i][j+1]=="B":
            print("Est ")
            for x in range(j+1, 8):
                if L[i][x]=="_":
                    break
                if L[i][x]=="N":
                    for l in range(x,j+1):
                        L[i][l]="N"
                        break
        #Parcours Ouest           
        if L[i][j-1]=="B":
            print("Ouest")
            for x in range(j-1, -1,-1):
                if L[i][x]=="_":
                    break
                if L[i][x]=="N":
                    for l in range(x,j-1,-1):
                        L[i][l]="N"
                        break  
        #Parcours Sud Est
        if L[i+1][j+1]=="B":
            for x in range(i+1, 8):
                if L[x][x]=="_":
                    break
                if L[x][x]=="N":
                    for l in range(i+1,x):
                        L[l][l]="N"
                        break
        #Parcours Sud Ouest
        if L[i+1][j-1]=="B":
            for x in range(i+1, 8):
                for y in range(i-1,0,-1):
                    if L[x][y]=="_":
                        break
                    if L[x][y]=="N":
                        for l in range(i+1,x):
                            for m in range(j-1,y,-1):
                                L[l][m]="N"
                                break
        #Parcours Nord Est
        if L[i-1][j+1]=="B":
            for x in range(i-1, -1,-1):
                for y in range(i+1,8):
                    if L[x][y]=="_":
                        break
                    if L[x][y]=="N":
                        for l in range(i-1,x,-1):
                            for m in range(j+1,y):
                                L[-l][l]="N"
                                break
        #Parcours Nord Ouest
        if L[i-1][j-1]=="B":
            print('Nord Ouest')
            for x in range(i-1, -1,-1):
                if L[x][x]=="_":
                    break
                if L[x][x]=="B":
                    print("on passe par là")
                    for l in range(i-1,x,-1):
                        L[l][l]="N"
                        break
    return L

def move(k, L):
    print('Mouvements possibles : ', getAllPossibleMoves(k,L))
    i = int(input("Jouer en ligne : "))
    i = int(input("Jouer en ligne : "))#Gérer les erreurs non int() avec un try catch ?
    j = int(input("Jouer en colonne : "))
    while isPlayable(i,j,k,L) == False:
        print("Ce mouvement est impossible, veuillez saisir des valeurs correctes")
        print('Mouvements possibles : ', getAllPossibleMoves(k,L))
        i = input("Jouer en ligne : ")
        j = input("Jouer en colonne : ")
        i = int(input("Jouer en ligne : "))
        j = int(input("Jouer en colonne : "))
        print(isPlayable(i,j,k,L))
    L[i][j] = k
    convertTaken(i,j,k,L)
    return L

def play():
    L = createGame()
@ -152,4 +322,3 @@ def play():
#Code principal
play()        

 