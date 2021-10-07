import turtle as tr
import math as mt

tr.shape('circle')

tr.speed(0)
tr.width(5)
tr.goto(650, 0)
tr.goto(-350, 0)
tr.width(2)
vx= 30
vy = 60
a = 13
x = -350
y = 0
for t in range(10000):
    x += vx*1/20
    y += vy*1/20-a*(1/20)**2/2
    vy -= a/20
    tr.goto(x, y)
    if (y <= 0 and vy <= 0):
        
        vy = -1*vy*6/8
        vx = vx*6/8
