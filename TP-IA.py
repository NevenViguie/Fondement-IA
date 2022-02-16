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
                L[i].append(-1)
        elif(i==3):
            L[i]=[-1,-1,-1,1,0,-1,-1,-1]
        elif(i==4):
            L[i]=[-1,-1,-1,0,1,-1,-1,-1]
    
    return L

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
    
    if(k==1):
        for i in range(8):
            for j in range(8):
                if(L[i][j] == 1):
                    A=getAdjacentCells(i, j)
                    for n in range(len(A)):
                        if(L[A[n][0]][A[n][1]]==0):
                            x=A[n][0]-i
                            y=A[n][1]-j
                            a=i+x
                            b=j+y
                            while(a>=0 and a<8 and b>=0 and b<8):
                                if(L[a][b]==-1):
                                    C.append((a,b))
                                    break
                                if(L[a][b]==1):
                                    break
                                a+=x
                                b+=y
                            
    if(k==0):
        for i in range(8):
            for j in range(8):
                if(L[i][j] == 0):
                    A=getAdjacentCells(i, j)
                    for n in range(len(A)):
                        if(L[A[n][0]][A[n][1]]==1):
                            x=A[n][0]-i
                            y=A[n][1]-j
                            a=i+x
                            b=j+y
                            while(a>=0 and a<8 and b>=0 and b<8):
                                if(L[a][b]==-1):
                                    C.append((a,b))
                                    break
                                if(L[a][b]==0):
                                    break
                                a+=x
                                b+=y
                                
    return C
                
                     

    #def play(i,j,L):
        
                    
                    
    
        