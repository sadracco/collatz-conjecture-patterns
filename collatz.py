#!/usr/bin/python3

import pygame as pg
from pygame.locals import *

from vec import Vec
from fade import rainbowColor, hsv2rgb

pg.init()
pg.display.set_caption('Collatz conjecture')
clock = pg.time.Clock()
screen = pg.display.set_mode((1300, 700))


def collatz(n, r=45):
    v = Vec(10,0)
    angle = 0
    rotate = r
    while n>1:
        if n%2:
            angle += rotate 
            n=3*n+1
        else:
            angle -= rotate 
            n/=2
        v.setAngle(angle)
        yield (v.x,v.y)

r = 1

on = True
while(on):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
            on = False

#    screen.fill((0,0,0))
    for n in range(50):
        line = list(collatz(n, r))
        ppos = [300,350]
        for i, v in enumerate(line):
            cpos = [ppos[0] + v[0], ppos[1] + v[1]]
            pg.draw.aaline(screen, hsv2rgb(i/len(line),1,1-i/len(line)), ppos, cpos, 7)
            ppos = cpos

    r+=1

    pg.display.flip()
    clock.tick(60)
