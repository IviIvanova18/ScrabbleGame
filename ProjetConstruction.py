#Importation des bibliothéques requise
import ProjetPlateau
from ProjetPlateau import *


#Création de la liste de mots autorisés
def generer_dico(nomFichier='liste_mots.txt'):
    #Ouveture fichier
    with open(nomFichier, "r") as text:
        #Lecture du fichier par ligne 
        lines = text.readlines()
        list_mots_autorisés = []
        for l in lines:
            #Mise en liste des mots autorisés
            list_mots_autorisés.append(l.replace("\n", ""))
        return list_mots_autorisés


#Initialistion de la liste de mots autorisé pour éviter d'avoir a le faire plusieurs fois
list_mots_autorisés=generer_dico()
    
#Récupération des lettres utilisables sur le plateau
def lettres_plateau_dispo(j):
    lettres_dispo=[]
    for i in j:
        #Test si la lettre est entourée et donc inutilisable
        NbVoisins=list_voisin_case(i[1],i[2])
        if NbVoisins!=4:
            lettres_dispo.apppend(i[0])
    return lettres_dispo

#Test si les lettres requise pour le mot sont présentes dans la main et/ou dans le plateau
#L'argument par défaut permet d'éviter d'avoir à rentrer les jetons sur le plateau d'est qu'il y a un changemment.
def mot_jouable(mot,main,lettres_plateau=lettres_plateau_dispo(j)):
    #Faire une copie de cette liste pour pouvoir la modifier
    copie_main = list(main)
    lettres_manquant =[]
    #Parcourir les lettres du mot
    for i in mot:
        if i in copie_main:
            # on "consomme" cette lettre
            copie_main.remove(i)
        else :
            lettres_manquant.append(i)
    if len(lettres_manquant)==0:
        return True
    if len(copie_main)>=len(lettres_manquant):
        #joker = "?"
        if len(lettres_manquant)==1 and "?" in copie_main:
            return True
        else:
            #Teste si il y a assez de lettres sur le plateau pour completer le mot
            if len(lettres_plateau)>=len(lettres_manquant):
                for j in lettres_manquant:
                    if j in lettres_plateau:
                        lettres_manquant.remove(j)
                return True
            else:
                return False
            
#Renvoie la listes des mot jouables        
def mots_jouables(main,liste_mots=list_mots_autorisés):
    mots_jouables=[]
    # parcourir tous les mots
    for mot in liste_mots :
        if mot_jouable(mot,main):
            mots_jouables.append(mot)
    # sortie: on a testé tous les mots, on renvoie la sélection
    return mots_jouables


