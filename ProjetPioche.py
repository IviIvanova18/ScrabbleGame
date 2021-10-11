#On créer le dictionnaire liant la valeurs et le nombre d'occurences d'une lettre
def init_dico():
    dico={
        "A" : {"occ" : 9 , "val" : 1 },
        "B" : {"occ" : 2 , "val" : 3 },
        "C" : {"occ" : 2 , "val" : 3 },
        "D" : {"occ" : 3 , "val" : 2 },
        "E" : {"occ" : 15, "val" : 1 },
        "F" : {"occ" : 2 , "val" : 4 },
        "G" : {"occ" : 2 , "val" : 2 },
        "H" : {"occ" : 2 , "val" : 4 },
        "I" : {"occ" : 8 , "val" : 1 },
        "J" : {"occ" : 1 , "val" : 8 },
        "K" : {"occ" : 1 , "val" : 10},
        "L" : {"occ" : 5 , "val" : 1 },
        "M" : {"occ" : 3 , "val" : 2 },
        "N" : {"occ" : 6 , "val" : 1 },
        "O" : {"occ" : 6 , "val" : 1 },
        "P" : {"occ" : 2 , "val" : 3 },
        "Q" : {"occ" : 1 , "val" : 8 },
        "R" : {"occ" : 6 , "val" : 1 },
        "S" : {"occ" : 6 , "val" : 1 },
        "T" : {"occ" : 6 , "val" : 1 },
        "U" : {"occ" : 6 , "val" : 1 },
        "V" : {"occ" : 2 , "val" : 4 },
        "W" : {"occ" : 1 , "val" : 10},
        "X" : {"occ" : 1 , "val" : 10},
        "Y" : {"occ" : 1 , "val" : 10},
        "Z" : {"occ" : 1 , "val" : 10},
        "?" : {"occ" : 2 , "val" : 0 }
        }
    return dico

#On initialise une liste qui sera la pioche
def init_pioche(dico=init_dico()):
    sac=[]
    #Le contenue est définie par le dictionnaire
    for i in dico:
        n=dico[i]["occ"]
        for j in range(n):
            sac.append(i)
    return sac

#Initialisation de la pioche
sac=init_pioche()

#On import les fonction nésséssaire à la création du hasard pour la pioche
import random
from random import randint
#On définie l'action de pioché
#On ramarque que il n'y a pas de conditions ici car elle sont définie dans les autres fonctions
def piocher(x,sac):
    JetonPioche=[]
    for i in range(x):
        temp=randint(0,(len(sac)-1))
        JetonPioche.append(sac.pop(temp))
    return JetonPioche,sac

#On compléte la main après un échange ou une pose de mot
def completer_main(main,sac):
    NbJetons=(7-len(main))
    #C'est ici que l'on teste si il reste assez de jeton pour completer la main.
    #Si il n'y a pas assez dz jeton pour completer la main, on prend le reste
    if NbJetons>len(sac):
        JetonPioche,sac=piocher(len(sac),sac)
        main+=JetonPioche
    else:
        JetonPioche,sac=piocher(NbJetons,sac)
        main+=JetonPioche


def echanger(Jetons,main,sac):
    #La fonction return fait sortir de la fonction donc pas besion de test après le "if" et le "else"
    #On teste d'abord si il y a assez de jetons dans le sac,
    if len(Jetons)>=len(sac):
        print("Echec de l\'échange")
        print("Plus assez de jetons")
        print("Reste "+len(sac)+" jetons")
        return False
    #Puis, on teste si il y a les jetons à echanger sont dans la main.
    else:
        #On créer la liste "test" pour pouvoir garder en mémoire les lettres retirer
        test=[]
        for i in Jetons:
            if i in main:
                test.append(i)
                main.remove(i)
            else:
                #Le test à echouer, on redonne les lettres en lever à "main"
                main+=test
                print("Echec de l\'échange")
                print("On echange seulment les jetons que l\'on a")
                return False
            
        #Pour l'échanger, on pioche d'abord les jetons
        completer_main(main,sac)
        #avant de remettre se que l'on echange dans le sac
        sac+=Jetons
        return True
    #On remarque que, lorsque le test échoue, la "main" récupére ces lettres mais pas à la même position.
    #Pour éviter cela nous avons voulue utiliser "test" comme copie de la liste"main" avec "test=list(main)" au début,
    #puis en utilisant "test.remove(i)" à la place de "main.remove(i)",
    #et en m'étant "main=test" ou "main=list(test)" si le teste réussissais
    #mais lorsque l'on faisait cela, la liste main n'était plus modifié la fin du programme
