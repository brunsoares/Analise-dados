from math import sqrt

class Rocket():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment

    def print_rocket(self):
        print(self.x, self.y)
