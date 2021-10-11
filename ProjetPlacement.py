#Importation des bibliothéques requise
import ProjetPlateau
from ProjetPlateau import *
import ProjetConstruction
from ProjetConstruction import *
import ProjetPioche
from ProjetPioche import *

#Demande les coordonnées d'origine puis la direction pour placer le mot
def lire_coords():
    # Le test permet de repéter la demande jusqu'a avoir des coordonées valides
    test=False
    while test==False :
        while test==False :
            ligne=int(input("Quel ligne entre 1 et 15 ? "))-1
            colonne=int(input("Quel colonne entre 1 et 15 ? "))-1
            test=(0 < ligne < 16 and 0 < colonne < 16)
            if test==False:
                print("Il faut des coordonnées dans le plateau")
        test=(plat_jetons[ligne][colonne]==" ")
        if test==False:
                print("La case a déjà une lettre")
    # La direction est nécessaire pour savoir où diriger les fonctions
    direction=""
    while type(direction)!=list:
        direction=input("Quel direction entre haut, bas, gauche ou droite ?")
        if direction=="haut":
            direction=[1,0]
        if direction=="bas":
            direction=[-1,0]
        if direction=="gauche":
            direction=[0,-1]
        if direction=="droite":
            direction=[0,1]
    return ligne,colonne,direction

#Teste si le mot est plaçable à ces coordonnées
def tester_placement(plateau,ligne,colonne,direction,mot):
    #"direction" sera une liste de la forme [0,1],droite, ou [0,-1],gauche, ou [1,0],haut, ou [-1,0],bas.
    # On renomme les variables pour rendre le code plus lisibles
    l=ligne
    c=colonne
    d=direction
    # Cette variable est ajouter pour savoir quel lettre sont déjà présente sur le plateau
    lettre_plateau=[]
    lettre_requis=list(mot)
    for i in range(len(mot)):
        if plateau[l][c]!=" ":
            if plateau[l][c]==mot[i]:
                lettre_plateau.append(lettre_requis.pop(i))
            else:
                print("La ligne contient des lettre non compatible")
                return [],[]
        l+=d[0]
        c+=d[1]
        if l<0 or 15<l or c<0 or 15<c :
            print("Le mot sort du plateau")
            return [],[]
    return lettre_requis,lettre_plateau

#Liste les voisins d'une case
def list_voisin_case(ligne,colonne):
    # On renomme les variables pour rendre le code plus lisibles
    l=ligne
    c=colonne
    voisin_case= []
    #On utilise "min" et "max" pour étre sur de ne pas sortir du plateau.
    for i in range(max(0,l-1),min(15,l+1)+1):
        for j in range(max(0,c-1),min(15,c+1)+1):
            #On ne veux pas des voisins en diagonal, c'est à dire l'associations (l+-1,c+-1),
            #On veux éviter la case elle même,
            #Et on ne veux que les voisin qui existe.
            if 0 in [i-l,j-c] and (i,j)!=(l,c) and plat_jetons[i][j]!=" ":
                voisin_case.append([plat_jetons[i][j],i,j])
    return voisin_case

#Liste les voisins d'un mot
def list_voisin(mot,ligne,colonne,direction):
    # On renomme les variables pour rendre le code plus lisibles
    l=ligne
    c=colonne
    d=direction
    voisin=[]
    for i in range(len(mot)):
        for j in list_voisin_case(l,c):
            voisin.append(j)
        l+=d[0]
        c+=d[1]
    return voisin

#Place les mots en modifiant "plat_jetons" et ajoute les jetons à "j"
def placer_mot(plateau,main,mot,ligne,colonne,direction):
    # On renomme les variables pour rendre le code plus lisibles
    l=ligne
    c=colonne
    d=direction
    lettre_requis,lettre_plateau=tester_placement(plateau,ligne,colonne,direction,mot)
    #Suite de test pour s'asurrer que l'on peut modifier les listes
    if lettre_requis!=[] :
        #Le premier coup doit se jouer en commence du centre du plateau,
        #Puis les coup suivant se font par rapport aux jetons déjà posés
        listeVoisin=list_voisin(mot,ligne,colonne,direction)
        if len(listeVoisin)!=0 or (l,c)==(7,7):
            for i in range(len(mot)):
                #Teste si la case a besion d'être remplie ou non.
                if plateau[l][c]==" ":
                    if lettre_requis[i] in main :
                        plateau[l][c]=lettre_requis[i]
                        main.remove(lettre_requis[i])
                        j.append([i,l,c])
                    else:
                        plateau[l][c]=lettre_requis[i]
                        main.remove("?")
                        j.append([i,l,c])
                l+=d[0]
                c+=d[1]
            return True
        else:
            print("Recommencer")
            return False
    else:
        print("Recommencer")
        return False



















