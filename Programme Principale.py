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
import ProjetJoueur
from ProjetJoueur import *
import random
from random import randint

#Programme¨principale
def scrabble():
    Joueur,scoreJoueur,mainJoueur=CreationPartie()
    LancerPartie(Joueur,scoreJoueur,mainJoueur)
    score_final(Joueur,scoreJoueur,mainJoueur)

scrabble()
