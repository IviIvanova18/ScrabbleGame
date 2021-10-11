#Importation des bibliothéques requise
import ProjetPioche
from ProjetPioche import *
import ProjetConstruction
from ProjetConstruction import *
import ProjetPlateau
from ProjetPlateau import *
import ProjetPlacement
from ProjetPlacement import *
list_mot_possible=generer_dico()

#Récupération de la valeur d'une lettre
def val_lettre(lettre,dico=init_dico()):
    return dico[lettre]["val"]

#Calcul de la valeur d'un mot
def val_mot(mot):
    valeur_mot=0
    for i in mot:
        valeur_lettre=val_lettre(i)
        valeur_mot+=valeur_lettre
    return valeur_mot

#Calcul des bonus
def val_bonus(mot,ligne,colonne,direction):
    l=ligne
    c=colonne
    d=direction
    valeur_bonus=0
    for i in mot:
        Bonus=plat_bonus[l][c]
        #Test pour évitait de tester tout les possibilitées à chaque case et filtre les bonus déjà utilisés.
        if Bonus!=" " and not("¤" in Bonus):
            #Le multiplicateur des bonus est réduit de 1 car la "valeur_bonus" sera ajouter "valeur_mot"
            if Bonus=="MT":
                valeur_bonus+=2*val_mot(mot)
                plat_bonus[l][c]+="¤"
            if Bonus=="MD":
                valeur_bonus+=val_mot(mot)
                plat_bonus[l][c]+="¤"
            if Bonus=="LT":
                valeur_bonus+=2*val_lettre(i)
                plat_bonus[l][c]+="¤"
            if Bonus=="LD":
                valeur_bonus+=val_lettre(i)
                plat_bonus[l][c]+="¤"
        l+=d[0]
        c+=d[1]
    #Teste pour savoir si le joueur a fait un «SCRABBLE», c'est à dire si il a posé 7 lettres d'un coup,
    #donc toute sa main.
    #if len(main)==0:
     #   print("Scrabble !")
      #  valeur_bonus+=50
    return valeur_bonus

#Petite fonction pour inverser une chaine de caractére(string)
def inverse_str(string):
    inver=""
    for i in range(len(string)):
        inver+=string[len(string)-1-i]
    return inver
#Fonction requise a la fin de "val_voisin(...)"
        
#Calcul des points obtenue par la création d'autre mots voisin
def val_voisin(mot,ligne,colonne,direction):
    l=ligne
    c=colonne
    d=direction
    valeur_voisin=0
    list_voisin=ProjetPlacement.list_voisin(mot,ligne,colonne,direction)
    #On n'a besion que des lettres perpendiculaire au mots formé.
    for i in range(len(list_voisin)):
        L=list_voisin[i][1]
        C=list_voisin[i][2]
        temp1=""
        temp2=""
        #On test dans quel sens le mot est formé
        if d[0]==0:
            #On teste des deux coté du mot
            if L==(l-1):
                temp1=""
                #Si il y a une lettre, on voit jusqu'où elle va
                while plat_jetons[L][C]!=" ":
                    temp1+=plat_jetons[L][C]
                    L-=1
            if L==(l+1):
                temp2=""
                while plat_jetons[L][C]!=" ":
                    temp2+=plat_jetons[L][C]
                    L+=1
        if d[1]==0:
            if C==(c-1):
                temp1=""
                while plat_jetons[L][C]!=" ":
                    temp1+=plat_jetons[L][C]
                    C-=1
            if C==(c+1):
                temp2=""
                while plat_jetons[L][C]!=" ":
                    temp2+=plat_jetons[L][C]
                    C+=1
        #On inverse temp1 puis temp2 pour qu'il soit a chaque fois dans le sens de lecture
        #if (inverse_str(temp1)+mot[i]+temp2 in list_mot_possible) or (inverse_str(temp2)+mot[i]+temp1 in list_mot_possible):
            #Pas besion de calculer les bonus car si les lettres sont déjà sur le plateau,
            #Les bonus sont déjà consommés
            #valeur_voisin+=val_mot(temp1+temp2)
    return valeur_voisin

#Calcul de la valeur total du coup
def val_totale(mot,ligne,colonne,direction):
    return val_bonus(mot,ligne,colonne,direction)+val_mot(mot)+val_voisin(mot,ligne,colonne,direction)
    

def meilleurs_mots(main):
    #Selection des mots jouables
    mots_possible=mots_jouables(main)
    #Test si on peut jouer des mots
    if len(mots_possible) == 0:
        return []
    #on initialise les variables requise
    meilleur_mot = mots_possible[0]
    meilleure_valeur = val_mot(meilleur_mot)
    meilleur_mot_list =[]
    meilleur_mot_list.append(meilleur_mot)
    for i in mots_possible:
        val = val_mot(i)
        if val == meilleure_valeur:
            meilleur_mot_list.append(i)
        if val > meilleure_valeur:
            meilleur_mot_list.clear()
            meilleur_mot_list.append(i)
            meilleur_mot = i
            meilleure_valeur = val 
    #Renvoie la liste des meilleurs mots
    return meilleur_mot_list
