#!/usr/bin/python3

import pygame as pg
from pygame.locals import *
import argparse
from datetime import datetime

from vec import Vec
from fade import rainbow, hsv2rgb
from sequence import Seq


parser = argparse.ArgumentParser(prog='python collatz.py', description='Animations based on collatz sequences')
parser.add_argument("-a", default=0, type=int, help='Animation number 0-4')
parser.add_argument("-s", default=0, type=int, help='Color scheme number 0-8')
parser.add_argument("-l", default=5, type=int, help='Line length - size of pattern')
parser.add_argument("-d", default=1, type=int, help='Initial angle in degress')
parser.add_argument("-c", default=0.75, type=float, help='Color (range 0-1). Run `python fade.py` to see why')
parser.add_argument("-f", default=False, type=bool, help='Save currently displayed pattern to the file when you close the window')
parser.add_argument("-x", default=100, type=int, help='x position')
parser.add_argument("-y", default=350, type=int, help='y position')

args = parser.parse_args()

pg.init()
pg.display.set_caption('Collatz conjecture')
clock = pg.time.Clock()
screen = pg.display.set_mode((700, 700))

seq = Seq(screen, args.a, args.s, args.l, args.d, args.c, args.x, args.y)

while(True):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            if args.f:
                pg.image.save(screen, 'pattern{}.png'.format(datetime.now().strftime('%b%d%H%M%S')))
            quit()

    seq.draw()

    pg.display.flip()
    clock.tick(60)
