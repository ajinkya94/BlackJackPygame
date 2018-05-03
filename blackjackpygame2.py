import sys, pygame,random,time

PlayerCard = []
ComputerCard=[]
suits = ('hearts', 'diamonds', 'spades', 'clubs')
ranks = ('2', '3', '4', '5','6','7', '8', '9','10','jack', 'queen', 'king','ace')
value = {'2':2, '3':3, '4':4, '5':5,'6':6,'7':7, '8':8, '9':9, '10':10, 'jack':10, 'queen':11, 'king':12,'ace':13}
clock = pygame.time.Clock()
FPS = 20
size = width, height = 900, 480
green = (0, 175, 0)
set_of_card = []
###########################################
#### Game initialized! ###
pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()
screen = pygame.display.set_mode(size)
iconimg = pygame.image.load("PlayingCards/iconsmall.png")
pygame.display.set_icon(iconimg)
########################################
# PLay background music

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

###################################
cardimg = pygame.image.load("PlayingCards/deck.png")
cardimgdeck = pygame.image.load("PlayingCards/deck.png")
cardimgdeck = pygame.transform.scale(cardimgdeck, (70,90))

handimg = pygame.image.load("PlayingCards/hand.png")
handimg = pygame.transform.scale(handimg, (70,90))



startposition = (500,200)
######################################
### CardDistribution Animation Work ###

##declaration for card1 from centerright to topleft
xplayer1 = 70
yplayer1 = 350
PlayerCard1 = True
PlayerCard2 = True
ComputerCard1 = True
ComputerCard2 = True
x,y = startposition
cardsshuffled=0
##############################################################

def checkevent(sum_of_player,sum_of_computer):
    global gameloop,StartAnimationLoop,cardsshuffled
    cardsshuffled +=1
    if cardsshuffled >= 5:
        if sum_of_player < sum_of_computer and sum_of_computer <= 21:
            print('Game OVER! Computer Wins! Total more than sum_of_player less than 21')
            print('Lost your Money!')
            print("----------------------------------------")
            gameloop = False
            StartAnimationLoop = False
        elif sum_of_player > sum_of_computer and sum_of_player == 21:
            print('Congratulations! Perfect 21!')
            print("----------------------------------------")
            gameloop = False
            StartAnimationLoop = False
        elif sum_of_player>21:
            print('Ooops! Over 21. Lost!')
            print('Lost your Money!')
            print("----------------------------------------")
            gameloop = False
            StartAnimationLoop = False
        elif sum_of_computer>21:
            print('sum_of_computer over 21. Congratulations!')
            print("----------------------------------------")
            gameloop = False
            StartAnimationLoop = False
        else:
            print("----------------------------------------")

###################################################################
sum_of_player = 0
sum_of_computer = 0
def randomize(y1):
    global sum_of_player,sum_of_computer
    suitschoice = "".join(random.sample(suits,1))
    rankschoice = "".join(random.sample(ranks,1))
    cardchoosen = rankschoice+"_of_"+suitschoice
    if cardchoosen in set_of_card:
        randomize()
    else:
        if y1==350:
            sum_of_player = sum_of_player+value[rankschoice]
            print("PlayerCard: {}".format(sum_of_player))
        else:
            sum_of_computer =sum_of_computer + value[rankschoice]
            print("ComputerCard: {}".format(sum_of_computer))
        checkevent(sum_of_player,sum_of_computer)
        return cardchoosen

    ##################################################################

def createbutton():
    buttonimghit = pygame.image.load("hitbutton.png")
    buttonimghit = pygame.transform.scale(buttonimghit, (150,40))
    screen.blit(buttonimghit,(750,200))
    pygame.display.update()
    buttonimgstay = pygame.image.load("staybutton.png")
    buttonimgstay = pygame.transform.scale(buttonimgstay, (150,40))
    screen.blit(buttonimgstay,(750,300))
    pygame.display.update()


####################################################################
def CardDistribution():
    global StartAnimationLoop,gameloop,x,y,PlayerCard1,PlayerCard2,ComputerCard1,ComputerCard2
    pygame.time.delay(1000)
    if PlayerCard1==True:
        screen.fill(green)
        animation(500,200,50,350)
        animation(500,200,50,100)
        animation(500,200,150,350)
        animation(500,200,150,100)
        PlayerCard1 = False
        createbutton()
    else:
        pass

###############################
def animation(x,y,x1,y1):
    #### Try with
    cardchoice = randomize(y1)
    cardimg = pygame.image.load("PlayingCards/png/"+cardchoice+".png")
    cardimg = pygame.transform.scale(cardimg, (70,90))
    screen.blit(cardimg,(x,y))
    pygame.display.update()
    while(y!=y1):
        while(x!=x1):
            clock.tick(FPS)
            pygame.draw.rect(screen,green,[x,y,70,95])
            pygame.display.update()
            x=x+10 if x<x1 else (x-10 if x>x1 else x)
            screen.blit(cardimg,(x,y))
            screen.blit(handimg,(x-10,y-5))
            pygame.display.update()
            if event.type == pygame.QUIT:
                gameloop = False
                StartAnimationLoop = False
                break
        clock.tick(FPS)
        pygame.draw.rect(screen,green,[x-5,y,80,95])
        pygame.display.update()
        y=y+10 if y<y1 else (y-10 if y>y1 else y)
        screen.blit(cardimg,(x,y))
        screen.blit(handimg,(x-10,y-5))
        pygame.display.update()
    pygame.draw.rect(screen,green,[x,y,70,90])
    screen.blit(cardimg,(x,y))
    screen.blit(cardimgdeck,startposition)
    pygame.display.update()
########################################
## GAME LOOP ###
newcoord = 250
gameloop = True
StartAnimationLoop = True
scenrioset = True
while gameloop==True:
    #### Loop ahead to set animation. No user input expected
    while StartAnimationLoop==True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
                StartAnimationLoop = False

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        pygame.display.update()
        if scenrioset == True:
            CardDistribution()
            scenrioset = False
        clock.tick(FPS)
        if 750+150>mouse[0]>150 and 200+40>mouse[1]>200:
            if click[0]==1:
                animation(500,200,newcoord,100)
                animation(500,200,newcoord,350)
                newcoord+=100

        elif 750+150>mouse[0]>750 and 300+40>mouse[1]>300:
            if click[0]==1:
                animation(500,200,newcoord,100)
                newcoord+=100

    #### Loop for animation ends here###

pygame.quit()
quit()
