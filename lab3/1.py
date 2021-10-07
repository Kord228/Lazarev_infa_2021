import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

(x0, y0) = (200,200)

black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
grey = (192, 192, 192)
width = 1

screen.fill(grey)
circle(screen, yellow, (x0, y0), 100)
circle (screen, black, (x0, y0), 100, width)

circle (screen, red, (x0-40, y0-30), 25)
circle (screen, black, (x0-40, y0-30), 25, width)

circle (screen, black, (x0-40, y0-30), 10)

circle (screen, red, (x0+40, y0-30), 20)
circle (screen, black, (x0+40, y0-30), 20, width)

circle (screen, black, (x0+40, y0-30), 8)

polygon (screen, black, [(x0+16, y0-34), (x0+8, y0-44),(x0+50, y0-95), (x0+60,y0-85)])

polygon (screen, black, [(x0-16,y0-34),(x0-8,y0-44),(x0-50, y0-95),(x0-60, y0-85)])


rect (screen, black,(x0-50, y0+50, 100, 20))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
