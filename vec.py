import math

class Vec:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.r = math.hypot(self.x, self.y)
        self.angle = math.atan2(self.y,self.x)

    def setLen(self, l):
        self.r = l
        self.x = math.cos(self.angle) * self.r
        self.y = math.sin(self.angle) * self.r

    def setAngle(self, a):
        self.angle = math.radians(a)
        self.x = math.cos(self.angle) * self.r
        self.y = math.sin(self.angle) * self.r

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __lt__(self, other):
        if self.r < other.r:
            return True
        return False

    def __gt__(self, other):
        if self.r > other.r:
            return True
        return False

    def __le__(self, other):
        if self.r <= other.r:
            return True
        return False

    def __ge__(self, other):
        if self.r >= other.r:
            return True
        return False

    def __ne__(self, other):
        if self.x != other.x or self.y != other.y:
            return True
        return False

    def __str__(self):
        return str((self.x, self.y))


def main():
    pass

if __name__ == "__main__":
    main()
