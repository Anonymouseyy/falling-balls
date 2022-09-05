from importlib.machinery import OPTIMIZED_BYTECODE_SUFFIXES
import pygame as pg
from math import sin, cos, pi

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
    

    def bounce(self, lp0, lp1):
        pt = pg.math.Vector2(self.x, self.y)
        dir = pg.math.Vector2(self.xvel, self.yvel)
        l_dir = (lp1 - lp0).normalize()                 # direction vector of the line
        nv = pg.math.Vector2(-l_dir[1], l_dir[0])       # normal vector to the line
        d = (lp0-pt).dot(nv)                            # distance to line
        r_dir = dir.reflect(nv)                         # reflect the direction vector on the line (like a billiard ball)                       
        self.xvel, self.yvel = r_dir


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
        self.lines = list()
        if shape == 'tri':
            self.sides = 3
        elif shape == 'sq':
            self.sides = 4
        elif shape == 'pent':
            self.sides = 5
        elif shape == 'hex':
            self.sides = 6
        self.draw()
    

    def draw(self):
        pts = []
        for i in range(self.sides):
            x = self.x + (cos(self.rot + pi * 2 * i / self.sides) * self.radius)
            y = self.y + (sin(self.rot + pi * 2 * i / self.sides) * self.radius)
            pts.append([int(x), int(y)])
        
        for i in range(self.sides):
            if i == self.sides-1:
                self.lines.append((pts[i], pts[0]))
            else:
                self.lines.append((pts[i], pts[i+1]))
        
        self.obj = pg.draw.polygon(self.surf, self.color, pts)
    
        health = pg.font.Font('Roboto-Black.ttf', 40).render(f'{self.hp}', True, black)
        health_rect = health.get_rect()
        health_rect.center = (self.x, self.y)
        self.surf.blit(health, health_rect)



def update_balls(balls, obstacles):
    for ball in balls:
        ball.yvel += 0.5
        if not ball.y > height+(2*ball.radius):
            ball.y += ball.yvel
        else:
            balls.remove(ball)
            continue
        
        ball.x += ball.xvel
        if ball.x <= ball.radius or ball.x >= width-ball.radius:
            ball.xvel *= -1
        
        obstacles_rects = [obstacle.obj for obstacle in obstacles]
        
        x = pg.Rect.collidelist(ball.obj, obstacles_rects)
        if x >= 0:
            obstacle = obstacles[x]
            obstacle.hp -= 1
            if obstacle.hp <= 0:
                obstacles.remove(obstacle)

            ball.xvel *= -0.9
            ball.yvel *= -0.9

        ball.draw()
    

def update_obstacles(obstacles):
    for obstacle in obstacles:
        obstacle.rot += 0.05
        obstacle.draw()
