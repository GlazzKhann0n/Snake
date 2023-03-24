#Repositorio creado por Sergio Morales
#Modificado por Othón Berlanga
#Modificado por Patricio Hernández

from random import randrange, choice
from turtle import *
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

colors = ['cyan','pink','orange','blue','purple']
n1 = randrange (0,4)
snek_color = colors[n1]
n2 = randrange (0,4)
fud_color = colors[n2]
if n1 == n2:
    n2 = randrange (0,4)
    fud_color = colors[n2]

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def inside(food):
    """Return True if head inside boundaries."""
    return -200 < food.x < 190 and -200 < food.y < 190

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
    #Prevents food from going out of bounds
    if not inside(food):
        food.x =  randrange(-15,15) * 10
        food.y =  randrange(-15,15) * 10
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snek_color)
    square(food.x, food.y, 9, fud_color)
    update()
    
   #Food Moves
    if randrange(10) == 0:
        food.x += (randrange (-1,1))*10
        food.y += (randrange (-1,1))*10  #awevo_furuló.exe
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
