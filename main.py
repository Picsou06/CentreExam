from random import randint
from math import *
import matplotlib.pyplot as plt
import numpy as np


def alea(a,b): #Définition de la fonction alea
    """

    Parameters
    ----------
    a : entiers relatifs
    
    b : entiers relatifs

    Returns
    -------
    Couple d'entier entre a et b

    """
    x=randint(a,b) #création de la variable x qui donne un nombre entre a et b
    y=randint(a,b) #création de la variable y qui donne un nombre entre a et b
    s=(x,y) #création d'un tuple avec les deux variables x et y
    return s

def centreExam(a, b, n): #Définition de la fonction centreExam
    """
    

    Parameters
    ----------
    a : entiers relatifs
        DESCRIPTION.
    b : entiers relatifs
        DESCRIPTION.
    n : nombre de couple
        DESCRIPTION.

    Returns
    -------
    n couple d'entier entre a et b'

    """
    s=[]
    for i in range(n): #Boucle qui tourne n fois
        x=alea(a,b) #création d'un tuple avec les deux variables a et b
        s.append(x)  #ajout du tuple a la liste des centreExam
    return s

def distance(a,b): #Définition de la fonction distance
    """
    

    Parameters
    ----------
    a : tuple de nombre entier (coordonnée)
    
    b : tuple de nombre entier (coordonnée)

    Returns
    -------
    la distance AB

    """
    return sqrt((b[0]-a[0])**2+(b[1]-a[1])**2) #calcul de la distance
    
def GPS(mesCoords,listeCentres): #Définition de la fonction GPS
    """
    

    Parameters
    ----------
    mesCoords : tuple de nombre entier (coordonnée)
    listeCentres : liste de tuple de nombre entier (coordonnée)

    Returns
    -------
    proche : tuple de nombre entier (coordonnée le plus proche)

    """
    proche=distance(mesCoords,listeCentres[0]) #création de la variable proche 
    for i in listeCentres: #boucle qui tourne le nombre d'élément de listeCentres
        dst=distance(mesCoords,i) #initialisation de la variable dst qui vérifie la distance entre nos coordonnée et i.
        if dst<proche:  #Vérification si la distance est plus petit que le plus petit (ou le premier élément)
            proche=dst #initialisation de la variable proche
            s=i #initialisation de la variable s
    return s

    

#création du schéma
mesCoords=alea(-50, 50) #Création de la varible MesCoord
listeCentres=centreExam(-50, 50, 20) #Création de la liste des listeCentres(avec 20 élément)
proche=GPS(mesCoords,listeCentres) #Creaion de la variable proche
x=[] #Création de la liste X
y=[] #Création de la liste Y
for i in listeCentres: #Boucle qui tourne le nombre d'élément de listeCentres
    x.append(i[0]) #Ajout des coordonnées X de chaque élément dans la liste X
    y.append(i[1]) #Ajout des coordonnées Y de chaque élément dans la liste Y

fig, ax = plt.subplots() #Création de ax pour plt

linx=[mesCoords[0],proche[0]] #Création de la liste linx avec les coordonnées X de mes coords et du centre le plus proche
liny=[mesCoords[1],proche[1]] #Création de la liste liny avec les coordonnées Y de mes coords et du centre le plus proche
dist=distance(mesCoords,proche) #création de la variable dist pour avoir la distance avec le centre le plus proche (le rayon du cercle)
ax.scatter(x, y, s=5, c="blue") #Création de tout les centres Exams
draw_circle = plt.Circle((mesCoords[0], mesCoords[1]),dist ,fill=False) #Création du cercle avec pour rayon le centre le plus proche

ax.set_aspect(1) #Modification de l'aspect du tableau
ax.add_artist(draw_circle) #Ajout de cercle au tableau
ax.plot(linx,liny,color='green') #Ajout du trait entre MesCoords et le centre le plus proche
ax.scatter(mesCoords[0], mesCoords[1], s=5, c="red") #Ajout du point de mes coordonnées

plt.show() #Affiche le tableau




def insertion(A,i): #Création de la fonction insertion
    """
    
    A : TYPE C'est une liste 
        
    i : TYPE C'est l'indice de l'élément à inserer
    

    Return Insert l'élément dans la liste

    """
    m = A[i] #Création de la variable m
    while i > 0 and m < A[i-1]: #Boucle temps que i supérieur a 0 ET m inférieur à A[i-1]
        A[i] = A[i-1] #initialisation de la variable A[i]
        i = i-1 #initialisation de la variable i
    A[i] = m #initialisation de la variable A[i]
    return A

def Tri_par_insertion(A):
    """

    A : TYPE C'est une liste
    
    Returns La liste triée
    
    """
    L = [] #Création de la liste L
    for i in range(len(A)): #Boucle i qui tourne le nombre d'élément de A
        L = insertion(A,i) #initialisation de L
    return L

def tri(mesCoord,listeCentres):
    """

    Parameters
    ----------
    mesCoord : Couble d'entier
        Coordonnée utilisateur
    listeCentres : liste de couble d'entier
        Coordonnées centres

    Returns
    -------
    distance dans l'ordre

    """
    dico={} #Création du dico
    t=[] #Création de la liste t
    result=[] #Création de la liste result
    for i in listeCentres: #Création de la liste i qui tourne pour chaque élément de listeCentres
        temp=distance(mesCoord,i) #Création de la liste temp 
        dico[temp] = i #Modification d'un élément de dico
        t.append(distance(mesCoord,i)) #Ajout de distance à t
    tri=Tri_par_insertion(t) #Création de la variable tri
    for i in tri: #Boucle for qui tourne pour chaque élément de tri
        result.append(dico[i]) #Ajout de dico à la liste résult
    return result
print("Liste des centre les plus proches: ", tri(mesCoords, listeCentres)) #print
