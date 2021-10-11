from tkinter import *
from random import randint,choice,shuffle
from string import ascii_uppercase
import ProjetPioche
import ProjetPlateau

global lettersList
lettersList = ProjetPioche.init_pioche()

def instructions():
    text = """                   Instructions for Scrabble:
            Le Scrabble® est un jeu de société ou sport cérébral, qui consiste à former des mots
        \n entrecroisés surune grille avec des lettres de valeurs différentes, les cases de 
        \ncouleur sur la grille permettant de multiplier la valeur des lettres ou des mots. 
        \nLe vainqueur est le joueur qui cumule le plus grand nombrede points à l'issue de la partie.

        Les règles du jeu varient selon la formule utilisée. Il peut se pratiquer à 2, 3 ou 4 joueurs
        \n en formule classique (une même grille pour tous, chacun ses lettres), ou à un grand nombre de joueurs 
        \nen formule Duplicate (une grille chacun, les mêmes lettres pour tous, en essayant de trouver le mot
        \n le plus rémunérateur).
        Les joueurs jouent à tour de rôle. Lorsque c'est son tour, un joueur pioche 7 pions dans le sac, puis il
        \n doit poser un mot d'au moins 2 lettres sur le plateau en utilisant un ou plusieurs de ses pions. 
        \nUne fois le mot posé, les points de ce mot sont ajoutés à son score (voir Décompte des points), 
        \net c'est au tour du joueur suivant.

        Au début de la partie, le mot placé par le premier joueur doit obligatoirement passer par la case
        \n centrale, marquée d'une étoile. Cette case faisant office de case "mot compte double", 
        \nla valeur du mot posé est multipliée par deux.

        Ensuite, chaque mot placé par un joueur doit obligatoirement se raccorder sur une ou plusieurs lettres 
        \ndéjà posées sur la grille. Si un mot placé par un joueur forme d'autres mots, ceux-ci doivent également 
        \nêtre des mots valides."""
    
    
    instructionsWindow = Toplevel(root, height=root.winfo_screenheight(), width=root.winfo_screenwidth())
    instructionsWindow.title("Instructions")
    instructionsWindow.iconbitmap("Scrabble.ico")
    instructionsWindow.config(bg="#ff9130")
    instructionsLabel = Label(instructionsWindow, text=text)
    instructionsLabel.place(x=300, y=0, height=650, width=700)
    closeButton = Button(instructionsLabel, text="Close", command=instructionsWindow.destroy)
    closeButton.place(x=225, y=600)


def play():
    label = Label(root,text="Play")
    label.pack()

def popup(root, header, text, windowHeight, windowWidth, closable = True, closeTime = 2, winx=0, winy=0):
    """Makes a new window pop up with a text. Very helpful. Note: closable=False does not work."""
    global popupClosed, window
    popupClosed = 0
    window = Toplevel(root, height=windowHeight, width=windowWidth)
    window.wm_title(header)

    label = Label(window, text=text, relief = SUNKEN)
    #label.place(x=(windowWidth//2)-250+winx, y=(windowHeight//2)-25+winy, \
    #            height = 500, width = 500)
    label.place(x=winx, y=winy, height = 500, width = 500)
    if closable:
        button = Button(window, text="Close", command=window.destroy)
        button.place(x=300, y=300)
    else:
        window.destroy()

def passTurn():
    return

def exchangeTiles():
    global exchangeWindow
    exchangeWindow = Toplevel(root)
    exchangeWindow.wm_title("Exghange Tile")
    exchangeWindow.geometry('300x300') 
    exchangeWindow.config(bg="#a1b6f0")
    exchangeWindow.iconbitmap("Scrabble.ico")
    exchangeLable = Label(exchangeWindow,text="Click the tiles you want to exchange")
    exchangeLable.place(x= 25, y = 50, height = 20, width =250)
    # placeTilesFrame =  Frame(exchangeWindow)
    # placeTilesFrame.place(x=100, y = 100, height = 40,width = 100)
    getExchangeRack(exchangeWindow,20,150)
    placeLetters(exchangeWindow,30,200) 
    enterButton=Button(exchangeWindow,exchangeLable,text="Exchange",command=exchange)
    enterButton.place(x=100,y=250)
    okButton=Button(exchangeWindow,exchangeLable,text="Close",command=exchangeWindow.destroy)
    okButton.place(x=200,y=250)

def exchange():
    ProjetPioche.echanger(exchangeLetters,playerRack,rack)
    exchangeWindow.destroy


def getExchangeRack(root,x,y):
    exchangeRack = Frame(root, bd=1, relief=RAISED)
    exchangeRack.place(x=x, y=y, height =40,width=250)
    labels = []
    for i in range(7):
        labels.append(Label(exchangeRack, relief=SUNKEN))
        labels[-1].place(x=i*30+x, y=y, height=30, width=30)


def board(): 
    global board
    root.title("Board")  
    board = [[" ", "A ", "B ", "C ", "D ", "E ", "F ", "G ", "H ", "I ", "J ", "K ", "L ", "M ", "N ", "O "],
    ['01', 'MT', ' ', ' ', 'LD', ' ', ' ', ' ', 'MT', ' ', ' ', ' ', 'LD', ' ', ' ', 'MT'],
    ['02', ' ', 'MD', ' ', ' ', ' ', 'LT', ' ', ' ', ' ', 'LT', ' ', ' ', ' ', 'MD', ' '],
    ['03',' ', ' ', 'MD', ' ', ' ', ' ', 'LD', ' ', 'LD', ' ', ' ', ' ', 'MD', ' ', ' '],
    ['04', 'LD', ' ', ' ', 'MD', ' ', ' ', ' ', 'LD', ' ', ' ', ' ', 'MD', ' ', ' ', 'LD'],
    ['05', ' ', ' ', ' ', ' ', 'MD', ' ', ' ', ' ', ' ', ' ', 'MD', ' ', ' ', ' ', ' '],
    ['06', ' ', 'LT', ' ', ' ', ' ', 'LT', ' ', ' ', ' ', 'LT', ' ', ' ', ' ', 'LT', ' '],
    ['07', ' ', ' ', 'LD', ' ', ' ', ' ', 'LD', ' ', 'LD', ' ', ' ', ' ', 'LD', ' ', ' '],
    ['08','MT', ' ', ' ', 'LD', ' ', ' ', ' ', 'MD', ' ', ' ', ' ', 'LD', ' ', ' ', 'MT'],
    ['09',' ', ' ', 'LD', ' ', ' ', ' ', 'LD', ' ', 'LD', ' ', ' ', ' ', 'LD', ' ', ' '],
    ['10',' ', 'LT', ' ', ' ', ' ', 'LT', ' ', ' ', ' ', 'LT', ' ', ' ', ' ', 'LT', ' '],
    ['11',' ', ' ', ' ', ' ', 'MD', ' ', ' ', ' ', ' ', ' ', 'MD', ' ', ' ', ' ', ' '],
    ['12', 'LD', ' ', ' ', 'MD', ' ', ' ', ' ', 'LD', ' ', ' ', ' ', 'MD', ' ', ' ', 'LD'],
    ['13', ' ', ' ', 'MD', ' ', ' ', ' ', 'LD', ' ', 'LD', ' ', ' ', ' ', 'MD', ' ', ' '],
    ['14', ' ', 'MD', ' ', ' ', ' ', 'LT', ' ', ' ', ' ', 'LT', ' ', ' ', ' ', 'MD', ' '],
    ['15', 'MT', ' ', ' ', 'LD', ' ', ' ', ' ', 'MT', ' ', ' ', ' ', 'LD', ' ', ' ', 'MT']]
    n,m=16,16
    colors = {"MT":"red", "MD":"orange", "LT":"#3e3bf7", "LD":"light blue"}
    boardWidth = 560
    boardHeight = 560
    boardFrame = Frame(root, relief=SUNKEN)
    boardFrame.place(x=30, y=40, width=boardWidth, height = boardHeight)
    labels = list()
    squares = list()
    for i in range(m):
        for j in range(n):
            label = board[i][j]
            labels.append(Label(text = label))
            frame = Frame(boardFrame, bd=1, relief=RAISED)
            frame.place(x=i*35,y = j*35,width=35, height=35)
            if label in colors:
                square = Label(frame,text=label,bg = colors[label], height=30, width=30, relief=RAISED)
            else:
                square = Label(frame,text=label, bg = "#327d46", height=30, width=30, relief=RAISED)   
            squares.append(square)
            squares[-1].pack(fill=X)
            frame.lift()
    root.resizable(True, True) 
    root.geometry('800x900') 
    placeLetters(root,200, boardHeight+50)
    placeButtons(boardHeight)
    #getScoreBoard(playersNames)
    
rack = ProjetPioche.init_pioche()
playerRack = []
ProjetPioche.completer_main(playerRack,rack)

def placeLetters(rootName,x, y):
    global movables
    row = 0
    movables = []
    for letter in playerRack:
        if rootName == root:
            movables.append(Letters(root, letter, row*30+x, y+12, root))
        else :
            movables.append(ExchangeLetters(exchangeWindow, letter, row*30+x, y+12, exchangeWindow))
        row += 1

def shuffleRack():
    shuffle(playerRack)
    for i in movables:
        i.frame.destroy()
    placeLetters(root,200, 560+50)

def getScoreBoard(playersNames):
    i=1
    label = Label(root,text="Score Board")
    label.place(x= 630,y=50,height= 20,width=150)
    for player in playersNames:
        playerScore = Label(root,text="{}'s Score: 0".format(player), height=1, width=20)
        playerScore.place(x =630, y=50+20*i, height = 20, width = 150)
        i+=1

def placeButtons(boardHeight):
    enterButton = Button(root, text = "Enter Word", command = getNewWord)
    enterButton.place(x=210,y=boardHeight+120,height = 20, width= 200)
    shuffleButton = Button(root, text = "Shuffle Tiles", command = shuffleRack)
    shuffleButton.place(x=110,y=boardHeight+160,height = 20, width= 100)
    returnButton = Button(root, text = "Pass Turn", command = passTurn)
    returnButton.place(x=260,y=boardHeight+160,height = 20, width= 100)
    exchangeButton = Button(root, text = "Exchange Tiles", command= exchangeTiles)
    exchangeButton.place(x=410,y=boardHeight+160,height = 20, width= 100)

def placePlayers():
    return

def numberPlayes():
    global players
    global enterWindow
    enterWindow = Toplevel(root)
    enterWindow.wm_title("Players")
    enterWindow.geometry('260x260') 
    enterWindow.config(bg="#ff9130")
    enterWindow.iconbitmap("Scrabble.ico")
    numPlayers = Label(enterWindow,text="Enter the number of player between 2 and 4")
    numPlayers.place(x= 5, y = 50, height = 20, width =250)
    players = Entry(enterWindow)
    players.place(x = 75, y = 100, height = 20, width = 100)   
    cd = lambda:closeWindowOpenNew(playEnter,enterWindow.destroy)
    mybutton=Button(enterWindow,text="OK",command=cd)
    mybutton.place(x=110,y=150)

def playEnter(): 
    global playersWindow
    global playersNames
    playersWindow = Toplevel(root)
    playersWindow.wm_title("Enter Players") 
    playersWindow.geometry('500x300') 
    playersWindow.config(bg="#ff9130")
    playersWindow.iconbitmap("Scrabble.ico")
    x=players.get()
    number=int(x)
    cd = lambda:closeWindowOpenNew(board,playersWindow.destroy)
    playButton = Button(playersWindow, text = "Play", command = cd)
    playButton.place(x = 10, y = 250)
    playersNames=list()
    for i in range(number):
        nameLabel = Label(playersWindow, text = "Enter player "+str(i+1)+" name:")
        nameLabel.place(x = 20, y = 10+50*i, height = 20, width = 150)
        nameVar = StringVar()
        entryName = Entry(playersWindow, textvariable=nameVar)
        entryName.place(x = 200, y = 10+50*i, height = 20, width = 200)
        nameVar.set("")
        name= entryName.get()
        playersNames.append(name)
        playButton = Button(playersWindow, text = "Play", command = board)
        playButton.place(x = 10, y = 450)
    
def closeWindowOpenNew(*args):
    for func in args:
        func()


class Letters():
    def __init__(self,root,text,x,y,frame):
        self.board = [[" ", "A ", "B ", "C ", "D ", "E ", "F ", "G ", "H ", "I ", "J ", "K ", "L ", "M ", "N ", "O "],
    ['01', 'MT', ' ', ' ', 'LD', ' ', ' ', ' ', 'MT', ' ', ' ', ' ', 'LD', ' ', ' ', 'MT'],
    ['02', ' ', 'MD', ' ', ' ', ' ', 'LT', ' ', ' ', ' ', 'LT', ' ', ' ', ' ', 'MD', ' '],
    ['03',' ', ' ', 'MD', ' ', ' ', ' ', 'LD', ' ', 'LD', ' ', ' ', ' ', 'MD', ' ', ' '],
    ['04', 'LD', ' ', ' ', 'MD', ' ', ' ', ' ', 'LD', ' ', ' ', ' ', 'MD', ' ', ' ', 'LD'],
    ['05', ' ', ' ', ' ', ' ', 'MD', ' ', ' ', ' ', ' ', ' ', 'MD', ' ', ' ', ' ', ' '],
    ['06', ' ', 'LT', ' ', ' ', ' ', 'LT', ' ', ' ', ' ', 'LT', ' ', ' ', ' ', 'LT', ' '],
    ['07', ' ', ' ', 'LD', ' ', ' ', ' ', 'LD', ' ', 'LD', ' ', ' ', ' ', 'LD', ' ', ' '],
    ['08','MT', ' ', ' ', 'LD', ' ', ' ', ' ', 'MD', ' ', ' ', ' ', 'LD', ' ', ' ', 'MT'],
    ['09',' ', ' ', 'LD', ' ', ' ', ' ', 'LD', ' ', 'LD', ' ', ' ', ' ', 'LD', ' ', ' '],
    ['10',' ', 'LT', ' ', ' ', ' ', 'LT', ' ', ' ', ' ', 'LT', ' ', ' ', ' ', 'LT', ' '],
    ['11',' ', ' ', ' ', ' ', 'MD', ' ', ' ', ' ', ' ', ' ', 'MD', ' ', ' ', ' ', ' '],
    ['12', 'LD', ' ', ' ', 'MD', ' ', ' ', ' ', 'LD', ' ', ' ', ' ', 'MD', ' ', ' ', 'LD'],
    ['13', ' ', ' ', 'MD', ' ', ' ', ' ', 'LD', ' ', 'LD', ' ', ' ', ' ', 'MD', ' ', ' '],
    ['14', ' ', 'MD', ' ', ' ', ' ', 'LT', ' ', ' ', ' ', 'LT', ' ', ' ', ' ', 'MD', ' '],
    ['15', 'MT', ' ', ' ', 'LD', ' ', ' ', ' ', 'MT', ' ', ' ', ' ', 'LD', ' ', ' ', 'MT']]
        self.scoreList = ['MD', 'MT', 'LT', 'LD']
        self.letters = ProjetPioche.init_dico()
        
        self. root = root
        self.rackFrame = frame
        self.x = x
        self.y = y

        self.originX = x
        self.originY = y

        self.text = text
        self.originText = text
        self.drawTile(32)
        self.movables = []
        # dimentions of the board
        self.boardWidth = 560
        self.boardHeight = 560
        # x and y where the board starts
        self.boardX, self.boardY = 30, 40


    def drawTile(self, size):
        """Draws the tile of letter """
        self.frame = Frame(self.rackFrame, bd=1, relief=RIDGE)
        self.frame.place(x=self.x, y=self.y, width=size, height=size)

        self.label = Label(self.frame, bd=1, relief=RAISED, \
                           text=self.text+self.getSubscript(self.letters[self.text]['val']),  #Puts the points for the letter on the label
                           height=size, width=size, bg="#ebc89b")
        self.label.pack(fill=X, padx=1, pady=1)     
        self.frame.lift()

        self.label.bind('<ButtonPress-1>', self.startMoveTile)
        self.label.bind('<B1-Motion>', self.MoveTile)
        self.label.bind('<ButtonRelease-1>', self.placementCheck)
        

    def getSubscript(self, number):
        """Uses unicode characters to generate subscript letters; used for point values"""
        points = {0:"\u2080", 1:"\u2081", 2:"\u2082", 3:"\u2083", 4:"\u2084", 5:"\u2085", 6:"\u2086", 7:"\u2087", 8:"\u2088", 9:"\u2089", 10:"\u2081\u2080"}
        return points[number]

    def startMoveTile(self, event):
        """Gets the last position when the tile is clicked"""
        self.lastX = event.x_root
        self.lastY = event.y_root

    def MoveTile(self, event):
        """Moves the tile with the mouse; event is mouse motion"""
        self.root.update_idletasks()
        self.x += event.x_root - self.lastX
        self.y += event.y_root - self.lastY
        # The tile can't go of the board
        if self.x > 560: self.x = 560 
        if self.y > 650: self.y = 650
        if self.x < 0: self.x = 0
        if self.y < 0: self.y = 0
        
        self.lastX, self.lastY = event.x_root, event.y_root
        self.frame.place_configure(x=self.x, y=self.y)

        self.frame.lift()
    
    def placementCheck(self, *event):
        tilePosition = (self.x, self.y)
        #If the tile is touching the board, it goes to the nearest square 
        #If the tile is not touching the board, it goes to its origin point
        if not(self.isInBoard(tilePosition, (self.boardX, self.boardY),
                          self.frame.winfo_width(), self.frame.winfo_height(),
                          self.boardWidth, self.boardHeight)):
            self.returnToOrigin()
        else:
            self.goToBoard()

    def returnToOrigin(self):
        self.x = self.originX
        self.y = self.originY
        self.frame.place_configure(x=self.x, y=self.y)

    def goToBoard(self):
        """Go to the nearest square on the board"""
        self.labels_positionList = {}
        for i in range(16):
            for j in range(16):
                self.labels_positionList[(i*35)+30, (j*35)+40] = (j, i)
        tilePosition = [self.x, self.y]
        for labelPosition in self.labels_positionList:
            if self.isInBoard(tilePosition, labelPosition, self.frame.winfo_width(), self.frame.winfo_height(),32, 32):
                if self.isEmpty(): 
                    self.frame.place_configure(x=labelPosition[0], y=labelPosition[1])
                    self.x = labelPosition[0]
                    self.y = labelPosition[1]
                    tilePosition = [self.x, self.y]
                else:
                    self.returnToOrigin()

    def isEmpty(self):
        #Checks if the place is empty so the tile can't be place in the same position as another tile
        #TO DO...
        return True


    def isInBoard(self, positionTile, positionBoard, widthTile, heightTile, widthBoard, heightBoard):
        #check if the tile is in the board, if it's in the board or touching in returns True
        if ((positionTile[0] > positionBoard[0]) or (positionTile[0] > (positionBoard[0] + widthTile))) and \
           ((positionTile[1] > positionBoard[1]) or (positionTile[1] > (positionBoard[1] + heightTile))) and \
           ((positionTile[0] < (positionBoard[0] + widthBoard)) and (positionTile[1] < (positionBoard[1] + heightBoard))):
            return True
        else:
            return False

class ExchangeLetters(Letters):
    def __init__(self,exchangeWindow,text,x,y,frame):
        global exchangeLetters
        super(ExchangeLetters, self).__init__(exchangeWindow, text, x, y, frame)
        self.exchangeLetters = []

    def drawTile(self, size):
        """Draws the tile of letter """
        self.frame = Frame(self.rackFrame, bd=1, relief=RIDGE)
        self.frame.place(x=self.x, y=self.y, width=size, height=size)

        self.label = Label(self.frame, bd=1, relief=RAISED, \
                           text=self.text+self.getSubscript(self.letters[self.text]['val']),  #Puts the points for the letter on the label
                           height=size, width=size, bg="#ebc89b")
        self.label.pack(fill=X, padx=1, pady=1)     
        self.frame.lift()
        self.label.bind('<ButtonPress-1>', self.goToFrame)
        self.label.bind('<ButtonPress-2>', self.returnToOrigin)
    
    def goToFrame(self):
        self.x = 20
        self.y = 100
        self.frame.place_configure(exchangeWindow, x=20, y=100)
        self.exchangeLetters.append(self.text)

def getNewWord():
    for movable in movables:
        movable.snapToGrid()
        movable.frame.update()
        


root = Tk()
root.resizable(True, True) 
root.geometry('250x250') 
root.config(bg="#a1f0ea")
welcomeLabel = Label(root, text = "Welcome to Scrabble in Python!")
instructionsButton = Button(root, text = "Instructions", command = instructions)
playButton = Button(root, text = "Play", command = numberPlayes)
#playButton = Button(root, text = "Play", command = board)
exitButton = Button(root, text = "Exit", command = root.quit)
root.title("Scrabble")
root.iconbitmap("Scrabble.ico")

welcomeLabel.place(x = 40, y = 10)
instructionsButton.place(x = 90, y = 50)
playButton.place(x = 110, y = 100)
exitButton.place(x = 112, y = 150)

root.mainloop()
