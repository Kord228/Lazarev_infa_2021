from random import randint
import turtle

def rand ( a, b):
    if (randint(0, 1) == 0):
        return a
    else:
        return b

number_of_turtles = 75
steps_of_time_number = 10000
turtle.tracer(0, 0)

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(8)
    unit.goto(randint(-297, 297), randint(-297, 297))
pool[1].width(4)
pool[1].goto(-300, -300)
pool[1].pendown()
pool[1].goto(300, -300)
pool[1].goto(300, 300)
pool[1].goto(-300, 300)
pool[1].goto(-300, -300)
pool[1].penup()
pool[1].goto(randint(-300, 300), randint(-300, 300))

A = [[rand(randint(-100000, 0), randint(0, 100000)), rand(randint(-100000, 0), randint(0, 100000))] for i in range(number_of_turtles)]

for i in range(steps_of_time_number):
    j = 0
    turtle.tracer(1,1)
    for unit in pool:
        turtle.tracer(0,0)
        unit.goto(unit.pos()[0]+A[j][0]/20000, unit.pos()[1]+A[j][1]/20000)
        if (unit.pos()[0] >= 295):
            A[j][0] = 2*295-A[j][0]
            unit.goto(294,unit.pos()[1])
        elif (unit.pos()[0] <= - 295):
            A[j][0]=2*(-295)-A[j][0]
            unit.goto(-294,unit.pos()[1])
        elif (unit.pos()[1] >= 295):
            A[j][1] = 2*295-A[j][1]
            unit.goto(unit.pos()[0], 294)
        elif (unit.pos()[1] <= - 295):
            A[j][1]=2*(-295)-A[j][1]
            unit.goto(unit.pos()[0], -294)
        
        
        j+=1
