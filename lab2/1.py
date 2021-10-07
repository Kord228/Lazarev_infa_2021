import turtle
import math
from random import *
turtle.shape('turtle')
turtle.speed(5)

for i in range(100):
    turtle.left(randint(1, 360))
    turtle.forward(randint(5, 40))
