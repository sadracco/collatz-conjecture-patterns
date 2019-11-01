import pygame as pg
import pygame.gfxdraw
from math import sin

from vec import Vec
from fade import hsv2rgb


class Seq:
    def __init__(self, screen, a, s, l, d, c, x, y):
        self.screen = screen
        self.angleChange = d  # Current angle change
        self.seqL = 200  # Length of collatz sequence
        self.length = l  # Length of each line
        self.startV = Vec(self.length, 0) # Initial vector for each line
        self.maxn = 50 # Max number of lines
        self.n = 0 # Current line number (for coloring)

        self.schemes = [
                self.scheme1, self.scheme2, self.scheme3,
                self.scheme4, self.scheme5, self.scheme6,
                self.scheme7, self.scheme8, self.scheme9,
                ]
        self.colorScheme = self.schemes[s]
        self.color = c # Line color (range 0 - 1). Run `python fade.py` to see why

        self.animations = [
                self.anim1, self.anim2, self.anim3,
                self.anim4, self.anim5,
                ]
        self.animation = self.animations[a]
        self.startPos= (x,y) # Where each line begins


    # Collatz sequence generator
    # If n is odd the lines turns to the right by some angle
    # and if its even it does the opposite
    def collatz(self, n):
        v = self.startV
        angle = 0
        while n>1:
            if n%2:
                angle += self.angleChange
                n=3*n+1
            else:
                angle -= self.angleChange
                n/=2
            v.setAngle(angle)
            yield (v.x,v.y)


    # Rendering

    def draw(self):
        self.animation()

    def drawSeq(self, seq):
        ppos = self.startPos
        for i, v in enumerate(seq):
            cpos = (ppos[0] + v[0], ppos[1] + v[1])

            # Sometimes wierd gaps between lines can be seen. That's becouse of the code bellow.
            # It can be fixed using line instead of aaline but antialiasing makes things look
            # a lot better so it's a tradeoff
            #pg.draw.line(self.screen, self.colorScheme(i, v, len(seq), cpos), ppos, cpos, 1)
            pg.draw.aaline(self.screen, self.colorScheme(i, v, len(seq), cpos), ppos, cpos, 1)
            ppos = cpos


    # Animations

    # Maxn lines changing angle each frame. It makes a cool pattern similar to mandelbrot fractal
    def anim1(self):
        for n in range(self.maxn):
            self.drawSeq(list(self.collatz(n)))
            self.n = n
        self.angleChange += 1

    # Same as anim1 but screen is cleared each frame. Also cool
    def anim2(self):
        self.screen.fill((0,0,0))
        self.anim1()

    # Just a single line - super boring
    def anim3(self):
        self.drawSeq(list(self.collatz(self.seqL)))

    # Multiple lines on top of eachother. Huge mess at biger angles but it looks super cool at 90 deg.
    def anim4(self):
        self.anim3()
        self.seqL += 1

    # Single line changing the angle - also boring
    def anim5(self):
        self.screen.fill((0,0,0))
        self.drawSeq(list(self.collatz(self.seqL)))
        self.angleChange += 1
        

    # Color schemes
    # Some of them are completely random
    # Color of the line can depend on its index in the sequence, vector by which that line is changed
    # total length of the sequence, positon of the lines end, etc.

    # Rainbow !!!
    def scheme1(self, i, v, l, cpos):
        return hsv2rgb(i/l, 1, 1-i/l)
    
    # Single color - lame
    def scheme2(self, i, v, l, cpos):
        return hsv2rgb(self.color, 1, 1)

    # Single color but it fades at the end
    def scheme3(self, i, v, l, cpos):
        return hsv2rgb(self.color, 1, 1 - i/l)

    # Also rainbow but different
    def scheme4(self, i, v, l, cpos):
        if cpos[0] > cpos[1]:
            return hsv2rgb(abs(cpos[1]/cpos[0]), 1, 1 - i/l)
        return hsv2rgb(abs(cpos[0]/cpos[1]), 1, 1 - i/l)

    # White - Color - Black transition
    def scheme5(self, i, v, l, cpos):
        return hsv2rgb(self.color, i/l, 1 - i/l)

    # Another rainbow but super messy
    def scheme6(self, i, v, l, cpos):
        return hsv2rgb(abs(sin(cpos[0]*cpos[1])), 1, 1 - i/l)

    # This one is super cool but I don't know how to describe it
    def scheme7(self, i, v, l, cpos):
        return hsv2rgb(self.n/self.maxn, 1, 1 - i/l)

    # Red - Green - Blue
    def scheme8(self, i, v, l, cpos):
        return hsv2rgb(sin(i/l), 1, 1 - i/l)

    # Pink mess. Similar to scheme6
    def scheme9(self, i, v, l, cpos):
        return hsv2rgb(abs(sin(i**2/l)), 1, 1 - i/l)
