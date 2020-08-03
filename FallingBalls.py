import math
import random
from pyglet import *
import time

colours = ['red', 'green', 'black', 'blue', 'pink', 'orange']

balls = []
ballWindow = window.Window(600, 600)
heightW = ballWindow.height
widthW = ballWindow.width
class Ball:
    def __init__(self, size, speed, batch):
        R = random.randint(0, 255)
        B = random.randint(0, 255)
        G = random.randint(0, 255)
        self.pickedUp = False
        self.size = size
        self.gravity = 1
        self.speedHorz = speed[0]
        self.speedVert = speed[1]
        location = [random.randint(0, widthW), random.randint(0, heightW)]
        self.ball = shapes.Circle(location[0], location[1], self.size, color = (R, B, G), batch = batch)

    def MoveBall(self):
        self.TouchingBounds()
        self.speedVert -= self.gravity
        self.speedVert += -self.speedVert / 50
        self.ball.x += self.speedHorz
        self.ball.y += self.speedVert

    def TouchingBounds(self):
        if self.ball.y + self.size >= heightW:
            self.BounceVert()

        elif self.ball.y - self.size <= 0:
            self.ball.y = self.size
            self.BounceVert()

        if self.ball.x + self.size >= widthW:
            self.ball.x = widthW - self.size
            self.BounceHorz()
 
        elif self.ball.x - self.size <= 0:
            self.ball.x = self.size
            self.BounceHorz() 

    def BounceVert(self):
        self.speedVert = round((-self.speedVert / (self.size * 0.1)), 1)  
        self.speedHorz = math.floor(self.speedHorz / (self.size * 0.1))

    def BounceHorz(self):
        self.speedHorz = -self.speedHorz
        self.speedVert = math.floor(self.speedVert * 0.9)


#----------------------Balls With Gravity-------------------------
batch = graphics.Batch()

#numOfBalls = int(input("How many balls: "))
for x in range(0, 10):
    size = random.randint(10, 20)
    speed = (random.randint(-5, 5), random.randint(-5, 5))
    newBall = Ball(size, speed, batch)
    balls.append(newBall)

@ballWindow.event
def on_draw():
    ballWindow.clear()
    batch.draw()

def update(t):
    for bball in balls:
        bball.MoveBall()

clock.schedule(update)
app.run()