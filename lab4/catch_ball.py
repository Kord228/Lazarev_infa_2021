
import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 20
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


global count
count = 0
global time
time = 0
global balls
global gor, ver

balls = list()
for i in range(10):
    x = randint(-1000000, 1000000)
    y = randint(-1000000, 1000000)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (randint(100, 900), randint(100, 900)), r)
    balls.append([x, y, r, color])
def new_balls():
    '''рисует новый шарик '''
    global balls
    global time
    #balls = list()
    for i in range(10):
        x = balls[i][0]/10000*time+600
        y = balls[i][1]/10000*time+450
        r=balls[i][2]
        if (x>=1200):
            balls[i][0]=2*1200-balls[i][0]
        elif (x<= 0):
            balls[i][0]=-balls[i][0]
        elif (y>=900):
            balls[i][1]=2*900-balls[i][1]
        elif (y<= 0):
            balls[i][1]=-balls[i][1]
        circle(screen, balls[i][3], (balls[i][0]/100000*time+600, balls[i][1]/100000*time+450), balls[i][2])
        
def click(event):
    global count
    #print(x, y, r)
    for ball in balls:
        if ((event.pos[0]-ball[0])**2+(event.pos[1]-ball[1])**2<=ball[2]**2):
            count+=1
            print(count)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
#new_balls()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    new_balls()
    time+=1
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
