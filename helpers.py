import pygame as pg
from math import sin, cos, pi, radians

white = (255, 255, 255)
gray = (138, 135, 128)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)

size = width, height = 500, 750


class Ball():
    def __init__(self, x, y, radius, screen, xvel=0, color=white):
        self.surf = screen
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.yvel = 0
        self.xvel = xvel
        self.draw()
    
    
    def draw(self):
        self.obj = pg.draw.circle(self.surf, self.color, (self.x, self.y), self.radius)


class Obstacle():
    def __init__(self, x, y, shape, hp, screen, color):
        self.surf = screen
        self.x = x
        self.y = y
        self.rot = 0
        self.shape = shape
        self.color = color
        self.max_hp = hp
        self.hp = hp
        self.radius = 50
        self.draw()
    

    def draw(self):
        if self.shape == 'tri':
            pts = []
            for i in range(3):
                x = self.x + (cos(self.rot + pi * 2 * i / 3) * self.radius)
                y = self.y + (sin(self.rot + pi * 2 * i / 3) * self.radius)

                pts.append([int(x), int(y)])
            
            self.obj = pg.draw.polygon(self.surf, self.color, pts)
        elif self.shape == 'sq':
            pts = []
            for i in range(4):
                x = self.x + (cos(self.rot + pi * 2 * i / 4) * self.radius)
                y = self.y + (sin(self.rot + pi * 2 * i / 4) * self.radius)

                pts.append([int(x), int(y)])
            
            self.obj = pg.draw.polygon(self.surf, self.color, pts)
        elif self.shape == 'pent':
            pts = []
            for i in range(5):
                x = self.x + (cos(self.rot + pi * 2 * i / 5) * self.radius)
                y = self.y + (sin(self.rot + pi * 2 * i / 5) * self.radius)

                pts.append([int(x), int(y)])
            
            self.obj = pg.draw.polygon(self.surf, self.color, pts)
        elif self.shape == 'hex':
            pts = []
            for i in range(6):
                x = self.x + (cos(self.rot + pi * 2 * i / 6) * self.radius)
                y = self.y + (sin(self.rot + pi * 2 * i / 6) * self.radius)

                pts.append([int(x), int(y)])
            
            self.obj = pg.draw.polygon(self.surf, self.color, pts)



def update_balls(balls):
    for ball in balls:
        ball.yvel += 0.5
        if not ball.y > height+(2*ball.radius):
            ball.y += ball.yvel
        else:
            balls.remove(ball)
        
        ball.x += ball.xvel
        if ball.x <= ball.radius or ball.x >= width-ball.radius:
            ball.xvel *= -1
        
        ball.draw()
    

def update_obstacles(obstacles):
    for obstacle in obstacles:
        obstacle.rot += 0.05
        obstacle.draw()