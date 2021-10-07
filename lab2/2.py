import turtle as tr
import math as mt
tr.shape('turtle')

def paint (number, n):
    coords = [
    (0, 0, 50, 0, 50, 100, 0, 100, 0, 0),
    (0, 50, 50, 100, 50, 0),
    (0, 100, 50, 100, 50, 50, 0, 0, 50, 0),
    (0, 100, 50, 100, 0, 50, 50, 50, 0, 0),
    (0, 100, 0, 50, 50, 50, 50, 0, 50, 100),
    (50, 100, 0, 100, 0, 50, 50, 50, 50, 0, 0, 0),
    (50, 100, 0, 50, 0, 0, 50, 0, 50, 50, 0, 50),
    (0, 100, 50, 100, 0, 50, 0, 0),
    (0, 100, 50, 100, 50, 0, 0, 0, 0, 100, 0, 50, 50, 50),
    (0, 0, 50, 50, 50, 100, 0, 100, 0, 50, 50, 50,)]
    tr.penup()
    tr.goto(n*100-350+coords[number][0], coords[number][1])
    tr.pendown()
    for i in range(2, len(coords[number]), 2):
         tr.goto(n*100-350+coords[number][i], coords[number][i+1])
k = 0
for i in [1, 4, 1, 7, 0, 0]:
    paint(i, k)
    k=k+1
    
