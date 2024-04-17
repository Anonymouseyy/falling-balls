from audioop import add
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

shoot_time = True
level = 1
balls_yet_to_shoot = 0
angle = None
time_since_last_shoot = 0
added_line = False
move_line = 0

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


def spawn_line_of_obstacles():
    number_of_obstacles = random.randint(1, 4)

    if number_of_obstacles == 4:
        for i in range(number_of_obstacles):
            obstacles.append(Obstacle((i*125)+75, 850, random.choice(shapes),
                                      round((random.randint(1, 10)+random.random())*level), screen,
                                      random.choice(colors)))
    elif number_of_obstacles == 1:
        obstacles.append(Obstacle(random.randint(55, 445), 850, random.choice(shapes),
                                  round((random.randint(1, 10)+random.random())*level), screen, random.choice(colors)))
    else:
        space_per_ob = width//number_of_obstacles
        for i in range(number_of_obstacles):
            obstacles.append(Obstacle(random.randint((i*space_per_ob)+55, ((i+1)*space_per_ob)-55), 850,
                                      random.choice(shapes), round((random.randint(1, 10)+random.random())*level),
                                      screen, random.choice(colors)))


while True:
    clock.tick(60)
    events = pg.event.get()

    for e in events:
        if e.type == pg.QUIT:
            sys.exit()
            #obstacles.append(Obstacle(mouse_x, mouse_y, random.choice(shapes), random.randint(1, 100), screen, random.choice(colors)))
    
    screen.fill(black)

    update_balls(balls, obstacles)
    update_obstacles(obstacles)
    if shoot_time:
        draw_aimer()
        shoot_time = False
        click, _, _ = pg.mouse.get_pressed()
        if click == 1:
            mouse_x, mouse_y = pg.mouse.get_pos()
            mouse_pt = pg.math.Vector2(mouse_x, mouse_y)
            start_pt = pg.math.Vector2(width//2, 0)
            angle = pg.math.Vector2().angle_to(mouse_pt-start_pt)
            balls.append(Ball(width//2, 0, 10, screen, cos(radians(angle))*10))
            balls_yet_to_shoot = level - 1
            level += 1
            added_line = False
    
    if not shoot_time and balls_yet_to_shoot and time_since_last_shoot == 5:
        balls.append(Ball(width//2, 0, 10, screen, cos(radians(angle))*10))
        balls_yet_to_shoot -= 1
        time_since_last_shoot = 0
    
    if not shoot_time and balls_yet_to_shoot:
        time_since_last_shoot += 1
    
    if move_line < 150:
        for obstacle in obstacles:
            obstacle.y -= 2
        move_line += 2

    if not balls:
        if not added_line:
            spawn_line_of_obstacles()
            added_line = True
            move_line = 0
        shoot_time = True

    pg.display.flip()