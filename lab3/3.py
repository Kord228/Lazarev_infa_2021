import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 700))

(x0, y0) = (0, 0)

black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
grey = (128, 128, 128)
green = (0, 255, 0)
skyblue = (135, 206, 250)
olive = (128, 128, 0)
brown = (184, 134, 11)
ckota = (205, 133, 63)
pink = (255, 192, 203)

width = 1

screen.fill(brown)

rect (screen, olive,(x0, y0+300, 500, 400))
rect (screen, white, (x0+300,y0+20, 180, 260))
rect (screen, skyblue, (x0+320, y0+40, 60, 60))
rect (screen, skyblue, (x0+400, y0+40, 60, 60))
rect (screen, skyblue, (x0+320, y0+120, 60, 140))
rect (screen, skyblue, (x0+400, y0+120, 60, 140))

ellipse (screen, ckota, (340, 330, 120, 80))#hvost
ellipse (screen, black, (340, 330, 120, 80), width)


ellipse(screen, ckota, (100, 320, 280, 160))#tulovische
ellipse(screen, black, (100, 320, 280, 160), width)

circle(screen, ckota, (340, 460), 50)#pravlap
circle(screen, black, (340, 460), 50, width)

ellipse(screen, ckota, (360, 480, 30, 80))#pravlap
ellipse(screen, black, (360, 480, 30, 80), width)

ellipse(screen, ckota, (110, 445, 100, 60))#levay lapa
ellipse(screen, black, (110, 445, 100, 60), width)

ellipse(screen, ckota, (60, 400, 30, 80))#lapapodgolovoi
ellipse(screen, black, (60, 400, 30, 80), width)


circle (screen, ckota, (100, 400), 60)#golova
circle (screen, black, (100, 400), 60, width)

circle (screen, green, (70, 400), 15)#levglaz
circle (screen, black, (70, 400), 15, width)

circle (screen, green, (130, 400), 15)#pravglaz
circle (screen, black, (130, 400), 15, width)

ellipse (screen, black, (72, 388, 8, 20))#levzrach(OK)

ellipse (screen, black, (132, 388, 8, 20))#pravzrach(OK)

polygon (screen, pink, [(100, 418),(94, 410),(106, 410)])#nose
polygon (screen, black, [(100, 418),(94, 410),(106, 410)], width)

polygon (screen, ckota, [(40, 330), (80, 350), (60,370)])#levyxo
polygon (screen, black, [(40, 330), (80, 350), (60,370)], width)

polygon (screen, ckota, [(120, 350), (140, 370), (160,330)])#pravyxo
polygon (screen, black, [(120, 350), (140, 370), (160,330)], width)

polygon (screen, pink, [(50, 340), (70, 350), (60,360)])#levyxovnutr
polygon (screen, black, [(50, 340), (70, 350), (60,360)], width)

polygon (screen, pink, [(150, 340), (130, 350), (140,360)])#pravyxovnutr
polygon (screen, black, [(150, 340), (130, 350), (140,360)], width)

line (screen, black, [100, 418], [100, 432])#huinypodnosom

arc (screen, black, (86, 425, 14, 14), 7*(math.pi)/6, 2*math.pi)#levus

arc (screen, black, (100, 425, 14, 14), math.pi, 11*math.pi/6)#prus

circle (screen, grey, (280, 580), 60)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
