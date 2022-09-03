import pygame as pg

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
        self.draw()
        self.yvel = 0
        self.xvel = xvel
    
    def draw(self):
        self.obj = pg.draw.circle(self.surf, self.color, (self.x, self.y), self.radius)

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