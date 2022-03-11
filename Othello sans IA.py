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
                                elif(L[a][b]=="B"):
                                    break
                                a+=x
                                b+=y
                            
    else:
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
                                elif(L[a][b]=="N"):
                                    break
                                a+=x
                                b+=y
                                
    return C
                               
def isFinished(compteTour, L):      #Pas encore testée
    if "N" in L == False:
        print("Le joueur Blanc a gagné la partie !!!")
        return True
    elif "B" in L == False:
        print("Le joueur Noir a gagné la partie !!!")
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

def convertTaken(i, j, k, L):
    if(k=="B"):
        #Parcours SUD
        if i<7 and L[i+1][j]=="N":#Gérer l'exception out of range
            for x in range(i+1, 8):
                if L[x][j]=="_":
                    break
                if L[x][j]=="B":
                    for l in range(i+1,x):
                        L[l][j]="B"
                    

        #Parcours NORD
        if i>0 and L[i-1][j]=="N":
            for x in range(i-1, -1,-1):
                if L[x][j]=="_":
                    break
                if L[x][j]=="B":
                    for l in range(i-1,x,-1):
                        L[l][j]="B"
                    
        #Parcours Est
        if j<7 and L[i][j+1]=="N":
            for x in range(j+1, 8):
                if L[i][x]=="_":
                    break
                if L[i][x]=="B":
                    for l in range(j+1,x):
                        L[i][l]="B"
                    
        #Parcours Ouest 
        if j>0 and L[i][j-1]=="N":
            for x in range(j-1, -1,-1):
                if L[i][x]=="_":
                    break
                if L[i][x]=="B":
                    for l in range(j-1,x,-1):
                        L[i][l]="B"
                        
        #Parcours Sud Est
        if i<7 and j<7 and L[i+1][j+1]=="N":
            for x in range(i+1, 8):
                if x>7 or L[x][x]=="_":
                    break
                if L[x][x]=="B":
                    for l in range(i+1,x):
                        L[l][l]="B"
                        
        #Parcours Sud Ouest
        if i<7 and j>0 and L[i+1][j-1]=="N":
            y=j
            for x in range(i+1, 8):
                y-=1
                if x>7 or y<0 or L[x][y]=="_":
                    break
                if L[x][y]=="B": 
                    for l in range(i+1,x):
                        for m in range(j-1,y,-1):
                            L[l][m]="B"
                            
        #Parcours Nord Est
        if i>0 and j<7 and L[i-1][j+1]=="N":
            y=j
            for x in range(i-1, -1,-1):
                y+=1
                if x<0 or y>7 or L[x][y]=="_":
                    break
                if L[x][y]=="B":
                    print("on passe par là")
                    for l in range(i-1,x,-1):
                        for m in range(j+1,y):
                            L[l][m]="B"
                            
        #Parcours Nord Ouest
        if i>0 and j>0 and L[i-1][j-1]=="N":
            print('Nord Ouest')
            for x in range(i-1, -1,-1):
                if x<0 or L[x][x]=="_":
                    break
                if L[x][x]=="B":
                    for l in range(i-1,x,-1):
                        L[l][l]="B"
                        
    else:
        #Parcours SUD
        if i<7 and L[i+1][j]=="B":#Gérer l'exception out of range
            for x in range(i+1, 8):
                if L[x][j]=="_":
                    break
                if L[x][j]=="N":
                    for l in range(i+1,x):
                        L[l][j]="N"
                        

        #Parcours NORD
        if i>0 and L[i-1][j]=="B":
            for x in range(i-1, -1,-1):
                if L[x][j]=="_":
                    break
                if L[x][j]=="N":
                    for l in range(i-1,x,-1):
                        L[l][j]="N"
                        
        #Parcours Est
        if j<7 and L[i][j+1]=="B":
            for x in range(j+1, 8):
                if L[i][x]=="_":
                    break
                if L[i][x]=="N":
                    for l in range(j+1,x):
                        L[i][l]="N"
                        
        #Parcours Ouest 
        if j>0 and L[i][j-1]=="B":
            for x in range(j-1, -1,-1):
                if L[i][x]=="_":
                    break
                if L[i][x]=="N":
                    for l in range(j-1,x,-1):
                        L[i][l]="N"
                        
        #Parcours Sud Est
        if i<7 and j<7 and L[i+1][j+1]=="B":
            for x in range(i+1, 8):
                if x>7 or L[x][x]=="_":
                    break
                if L[x][x]=="N":
                    for l in range(i+1,x):
                        L[l][l]="N"
                        
        #Parcours Sud Ouest
        if i<7 and j>0 and L[i+1][j-1]=="B":
            y=j
            for x in range(i+1, 8):
                y-=1
                if x>7 or y<0 or L[x][y]=="_":
                    break
                if L[x][y]=="N": 
                    for l in range(i+1,x):
                        for m in range(j-1,y,-1):
                            L[l][m]="N"
                            
        #Parcours Nord Est
        if i>0 and j<7 and L[i-1][j+1]=="B":
            y=j
            for x in range(i-1, -1,-1):
                y+=1
                if x<0 or y>7 or L[x][y]=="_":
                    break
                if L[x][y]=="N":
                    print("on passe par là")
                    for l in range(i-1,x,-1):
                        for m in range(j+1,y):
                            L[l][m]="N"
                            
        #Parcours Nord Ouest
        if i>0 and j>0 and L[i-1][j-1]=="B":
            print('Nord Ouest')
            for x in range(i-1, -1,-1):
                if x<0 or L[x][x]=="_":
                    break
                if L[x][x]=="N":
                    for l in range(i-1,x,-1):
                        L[l][l]="N"
                        
    return L

def move(k, L):
    print('Mouvements possibles : ', getAllPossibleMoves(k,L))
    
    i = int(input("Jouer en ligne : "))#Gérer les erreurs non int() avec un try catch ?
    j = int(input("Jouer en colonne : "))
        
    while isPlayable(i,j,k,L) == False:
        print("Ce mouvement est impossible, veuillez saisir des valeurs correctes")
        print('Mouvements possibles : ', getAllPossibleMoves(k,L))
        i = int(input("Jouer en ligne : "))
        j = int(input("Jouer en colonne : "))
        print(isPlayable(i,j,k,L))
            
    L[i][j] = k
    convertTaken(i,j,k,L)
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
        else:
            print("Joueur Noir, c'est votre tour")
            k="N"
            L=move(k, L)
        display(L)
        compteTour += 1

#Code principal
play()      