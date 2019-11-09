""" A program that uses a cylinder class. """

from math import pi


# define the cylinder class with module documentation

class cylinder():
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def getRadius(self):
        return self.radius

    def getHeight(self):
        return self.height

    def volume(self):
        return pi * self.radius**2 * self.height

    def surfaceArea(self):
        return 2 * pi * self.radius * self.height + 2 * pi * self.radius**2


def writeCylinder(c):
    """ A function that takes a cylinder as a parameter and
        prints its information."""
    print("Radius =", c.getRadius())
    print("Height =", c.getHeight())
    print("Volume =", c.volume())
    print("Surface Area =", c.surfaceArea())


def main():
    """ A function that tests the cylinder class. """
    c1 = cylinder(5.1, 5.6)  # cylinder with 5.1 radius and 5.6 height
    c2 = cylinder(3.9, 7.8)  # cylinder with 3.9 radius and 7.8 height

    print("Cylinder 1:")
    writeCylinder(c1)
    print()
    print("Cylinder 2:")
    writeCylinder(c2)


main()

