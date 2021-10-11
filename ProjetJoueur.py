#Importation des bibliothéques requise
import ProjetPlateau
from ProjetPlateau import *
import ProjetPioche
from ProjetPioche import *
import ProjetConstruction
from ProjetConstruction import *
import ProjetPlacement
from ProjetPlacement import *
import ProjetValeur
from ProjetValeur import *
import random
from random import randint

def CreationPartie():
    NbJoueur=-1
    while NbJoueur<0:
        NbJoueur=int(input("Quel est le nombre de joueur ? "))
    Joueur={}
    scoreJoueur={}
    mainJoueur={}
    for i in range(NbJoueur):
        Nom=input("Nom du joueur "+str(i+1)+" ? ")
        Joueur[i+1]=Nom
        scoreJoueur[i+1]=0
        mainJoueur[i+1]=[]
        completer_main(mainJoueur[i+1],sac)
    return Joueur,scoreJoueur,mainJoueur


#Lance la partie et creer les
def LancerPartie(Joueur,scoreJoueur,mainJoueur,j=[]):
    init_jeu_plateau()
    Prems=randint(1,len(Joueur))
    tourJoueur(Joueur,scoreJoueur,mainJoueur,Prems)


#Déroulement du tour des joueurs
def tourJoueur(Joueur,scoreJoueur,mainJoueur,Prems):
    X=Prems
    while finDePartie(mainJoueur):
        input("Au tour de "+Joueur[X]+" ! ")
        affiche_plateau()
        print(mainJoueur[X])
        choix=""
        while (choix!="Passer" and choix!="Echanger" and choix!="Placer"):
            choix=input("Que voulez-vous faire ? Passer/Echanger/Placer ")
        if choix=="Echanger":
            Jetons=[None]
            while echanger(Jetons,mainJoueur[X],sac)==False:
                Jetons=list(input("Quels sont les jetons à échanger ?"))
        if choix=="Placer":
            print("Les mots jouables sont :",mots_jouables(mainJoueur[X]))
            print("Les meilleurs mot sont :",meilleurs_mots(mainJoueur[X]))
            ligne,colonne,direction,mot=7,7,(0,1),""
            while placer_mot(plat_jetons,mainJoueur[X],mot,ligne,colonne,direction)==False:
                ligne,colonne,direction=lire_coords()
                mot=input("Quels mots ?")
            scoreJoueur[X]+=val_totale(mot,ligne,colonne,direction)
        #Joueur suivant
        X+=1
    #Fin de partie après le while


#Décrète la fin de partie lorsque le sac est vide et que un joueur n'a plus de main.
def finDePartie(mainJoueur):
    if sac==[] and mainJoueur[X]==[]:
        return False
    else:
        return True

#Calcul et affiche le score de fin
def score_final(Joueur,scoreJoueur,mainJoueur):
    for i in range(len(Joueur)):
        scoreJoueur[i+1]-=(val_mot("".join(mainJoueur[i+1])))
    for j in range(len(Joueur)):
        Gagnant=1
        Max=scoreJoueur[1]
        if scoreJoueur[j+1]>Max:
            Gagnant=j+1
            Max=scoreJoueur[j+1]
    print("Le gagnant est",Joueur[Gagnant],"avec",scoreJoueur[Gagnant],"points")
