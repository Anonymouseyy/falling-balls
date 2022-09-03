import pygame as pg
from helpers import Ball, update_balls
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

screen = pg.display.set_mode(size)
pg.display.set_caption('Falling Balls')

# Fonts
smallFont = pg.font.Font('Roboto-Black.ttf', 14)
mediumFont = pg.font.Font('Roboto-Black.ttf', 28)
largeFont = pg.font.Font('Roboto-Black.ttf', 40)

while True:
    clock.tick(60)
    events = pg.event.get()

    for e in events:
        if e.type == pg.QUIT:
            sys.exit()
        elif e.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            balls.append(Ball(mouse_x, mouse_y, 10, screen, random.randint(-10, 10)))
            print(mouse_x, mouse_y)
    
    screen.fill(black)

    update_balls(balls)

    pg.display.flip()