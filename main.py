from math import sin, cos, radians
import pygame as pg
from helpers import Ball, Obstacle, update_balls, update_obstacles
import sys, time, random

pg.init()
size = width, height = 500, 750
clock = pg.time.Clock()
text_clock = pg.time.Clock()

# Colors
white = (255, 255, 255)
gray = (138, 135, 128)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)

balls = []
obstacles = []
shapes = ['tri', 'sq', 'pent', 'hex']
colors = [white, red, green, yellow, blue]

screen = pg.display.set_mode(size)
pg.display.set_caption('Falling Balls')

# Fonts
smallFont = pg.font.Font('Roboto-Black.ttf', 14)
mediumFont = pg.font.Font('Roboto-Black.ttf', 28)
largeFont = pg.font.Font('Roboto-Black.ttf', 40)


def draw_aimer():
    mouse_x, mouse_y = pg.mouse.get_pos()
    length = 100
    mouse_pt = pg.math.Vector2(mouse_x, mouse_y)
    start_pt = pg.math.Vector2(width//2, 0)
    angle = pg.math.Vector2().angle_to(mouse_pt-start_pt)

    endx, endy = (cos(radians(angle))*length) + width//2, sin(radians(angle))*length
    pg.draw.line(screen, white, start_pt, (endx, endy), 5)


while True:
    clock.tick(60)
    events = pg.event.get()

    for e in events:
        if e.type == pg.QUIT:
            sys.exit()
        elif e.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            balls.append(Ball(width//2, 0, 10, screen, random.randint(-10, 10)))
            obstacles.append(Obstacle(mouse_x, mouse_y, random.choice(shapes), random.randint(1, 100), screen, random.choice(colors)))
    
    screen.fill(black)

    update_balls(balls, obstacles)
    update_obstacles(obstacles)
    draw_aimer()

    pg.display.flip()