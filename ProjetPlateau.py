#Nous devons créer deux plateau: un pour le placement des jetons, l'autre pour le placement des bonus
#Nous definissons la fonction init_pla pour avoir un plateau vide réutilisables pour les bonus et les jetons.
def init_plat():
    ligne=[]
    plateau=[]
    for i in range(15):
        ligne.append(' ')
    for j in range(15):
        #On append "list(ligne)" pour éviter qu'il soit liée
        plateau.append(list(ligne))
    return plateau


def init_bonus():
    #Création d'un plateau vide non lier pour les bonus
    plat_bonus=list(init_plat())
    #Création des listes de coordonées des emplacements des bonus
    cases_MT = [[0,0],[0,7],[0,14],[7,0],[7,14],[14,0],[14,7],[14,14]]
    cases_MD = [[1,1],[1,13],[2,2],[2,12],[3,3],[3,11],[4,4],[4,10],[7,7],[10,4],[10,10],[11,3],[11,11],[12,2],[12,12],[13,1],[13,13]]
    cases_LT = [[1,5],[1,9],[5,1],[5,5],[5,9],[5,13],[9,1],[9,5],[9,9],[9,13],[13,5],[13,9]]
    cases_LD = [[0,3],[0,11],[2,6],[2,8],[3,0],[3,7],[3,14],[6,2],[6,6],[6,8],[6,12],[7,3],[7,11],[8,2],[8,6],[8,8],[8,12],[11,0],[11,7],[11,14],[12,6],[12,8],[14,3],[14,11]]
    #Mise en place des bonus dans le plat_bonus.
    #La création des variable "l" et "c" permet de mettre en évidence les emplacemants par lignes et par colonnes
    for i in cases_MT:
        l=i[0]
        c=i[1]
        plat_bonus[l][c]="MT"
    for i in cases_MD:
        l=i[0]
        c=i[1]
        plat_bonus[l][c]="MD"
    for i in cases_LT:
        l=i[0]
        c=i[1]
        plat_bonus[l][c]="LT"
    for i in cases_LD:
        l=i[0]
        c=i[1]
        plat_bonus[l][c]="LD"
    return plat_bonus

#Fonction permettant d'afficher des symboles à la place des noms réel des bonus.
#Les lien entre symboles et bonus sont afficher dans "affiche_plateau"
def symbole(Bonus):
    #Test pour évitait de tester tout les possibilitées à chaque case.
    if Bonus!="":
        if "MT" in Bonus:
            return "*"
        if "MD" in Bonus:
            return "#"
        if "LT" in Bonus:
            return "%"
        if "LD" in Bonus:
            return "&"
        else:
            #Renvoie un espace pour garder un format d'affichage cohérent.
            return " "

def init_jetons():
    plat_jetons=list(init_plat())
    #Création d'un plateau vide non lier pour les jetons
    return plat_jetons

#Création des listes requise pour les fonctions suivante
plateau = init_plat()
plat_bonus = init_bonus()
plat_jetons = init_jetons()

#J'ai rajouter le paramétre "plat_jetons car l'initialisation ne marcher pas sans cela
def affiche_jetons(j=[]):
    #"j" doit être une liste de liste où les liste à l'intérieur de la listes
    #doivent être au format : [NomDuJeton,Ligne,Colonne]
    for i in j:
        l=i[1]
        c=i[2]
        plat_jetons[l][c]=i[0]


#Commande pour initialiser le plateau:
def init_jeu_plateau(j=[]):
    #"j" sera une liste de liste, comme déjà expliqué, servant de sauvegarde
    affiche_jetons(j)
    #Lien entre bonus et symboles
    print("Les signes des bonus :\n MT = *\n MD = #\n LT = %\n LD = &")
    #Pour afficher les numéros des colonnes
    for i in range(len(plateau[0])+1):
        #Conditions pour la cohérence d'affichage
        if i<9:
            print(str(i),end=" │  ")
        else:
            print(str(i),end=" │ ")
    #"print" séparer les lignes.
    print("\n------------------------------------------------------------------------------")
    for l in range(len(plateau)):
        #Pour afficher les numéros des lignes avec conditions pour la cohérence d'affichage
        if l<9:
            print(" "+str(l+1),end="│ ")
        else:
            print(str(l+1),end="│ ")
        for c in range(len(plateau[0])):
            #Case à la ligne "l" et à la colonne "c"
            #"plat_jetons" contient les jetons, "plat_bonus" contient les bonus
            print(plat_jetons[l][c]+symbole(plat_bonus[l][c]),end=" │ ")
        print("\n------------------------------------------------------------------------------")


# Fonction qui affiche juste le plateau
def affiche_plateau():
    #Lien entre bonus et symboles
    print("Les signes des bonus :\n MT = *\n MD = #\n LT = %\n LD = &")
    #Pour afficher les numéros des colonnes
    for i in range(len(plateau[0])+1):
        #Conditions pour la cohérence d'affichage
        if i<9:
            print(str(i),end=" │  ")
        else:
            print(str(i),end=" │ ")
    #"print" séparer les lignes.
    print("\n------------------------------------------------------------------------------")
    for l in range(len(plateau)):
        #Pour afficher les numéros des lignes avec conditions pour la cohérence d'affichage
        if l<9:
            print(" "+str(l+1),end="│ ")
        else:
            print(str(l+1),end="│ ")
        for c in range(len(plateau[0])):
            #Case à la ligne "l" et à la colonne "c"
            #"plat_jetons" contient les jetons, "plat_bonus" contient les bonus
            print(plat_jetons[l][c]+symbole(plat_bonus[l][c]),end=" │ ")
        print("\n------------------------------------------------------------------------------")

#On definie "j" qui nous servira de liste sauvegardes pour les jetons
j=[]

#Petit "j" pour le teste:
#   j=[["B",7,4],["R",7,10],["N",7,6],["O",7,8],["O",7,5],["U",7,9],["J",7,7]]


