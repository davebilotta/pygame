import pygame, sys, time
from random import randint
from pygame.locals import *
global resultText 

question = 0
answer = ""
maxNum = 0
gameLevel = 1
difficulty = 1
score = 0
resultText = ""
questionWidth = questionHeight = 0
margin = 15

# set up pygame
pygame.init()

# set up the window
WINDOWWIDTH = 1024
WINDOWHEIGHT = 768
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Learning Math Game')

BLACK = (0,0,0)
WHITE = (255,255,255)
BKG = (234,234,234)
QUESTIONCOLOR = (255,127,36)
ANSWERCOLOR = (238,0,0)

SCORECOLOR = (139,134,130)
RESULTCOLOR = (100,149,237)

# Display some text
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(WHITE)

font = pygame.font.Font(None,64)
fontLarge = pygame.font.Font(None,200)

screen.blit(background, (0, 0))
pygame.display.flip()

def setup():
    global maxNum
    
    maxNum = 20
    mode = "+"

def checkAnswer():
    global score 

    if (len(answer)>0):
        if eval(question) == eval(answer):
            score += 1
            return True
        else: 
            return False

def newQuestion():
    global question
    global answer

    answer = ""
    if (randint(0,1) == 0):
        oper = " + "
    else:
        oper = " - "

    question = str(randint(0,maxNum)) + oper + str(randint(0,maxNum))
    return question

def renderQuestion():
    global questionWidth
    global questionHeight 

    text = fontLarge.render(question + " = ", 1, QUESTIONCOLOR)

    questionWidth = text.get_width()
    questionHeight = text.get_height()
    screen.blit(text,(0, WINDOWHEIGHT/2 - questionHeight/2))
   
def renderAnswer():
    text = fontLarge.render(answer, 1, ANSWERCOLOR)
    screen.blit(text,(questionWidth, WINDOWHEIGHT/2 - text.get_height()/2))

def renderScore():
    text = font.render("Score: " + str(score), 1, SCORECOLOR)
    screen.blit(text,(WINDOWWIDTH - text.get_width() - margin,margin))

def renderResult():
    text = font.render(resultText, 1, RESULTCOLOR)
    screen.blit(text,(margin,margin))
    
def positive():
    pos = ["Great!","Correct","Good job!","Awesome!","You did it!"]
    return pos[randint(0,len(pos)-1)]

def negative():
    neg = ["Whoops!","Try again","Close!","Almost!","Sorry"]
    return neg[randint(0,len(neg)-1)]

setup()
question = newQuestion()

while True:
    # check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            #print event.key
            resultText = ""

            if event.key == pygame.K_ESCAPE: 
                pygame.quit()
                sys.exit()

            # TODO: add Delete keycode as well?
            if event.key == pygame.K_BACKSPACE:
                if (len(answer) > 0):
                    answer = answer[0:len(answer)-1]
                    #print answer

            if event.key == pygame.K_RETURN:
                if (len(answer)>0):
                    if checkAnswer():
                        resultText = positive()
                        newQuestion()
                    else:
                        resultText = negative()
                
            # Numbers 48-57 (inclusive)
            # May need to differentiate between keypad and regular?
            if ((event.key == 45) or (event.key in range(48,58))):
                answer += str(chr(event.key))
                #print answer

    screen.fill(BKG)

    renderQuestion()
    renderAnswer()
    renderScore()
    renderResult()

    pygame.display.update()
   