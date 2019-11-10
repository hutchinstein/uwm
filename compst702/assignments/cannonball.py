import math


class Projectile:
    """Simulates the flight of simple projectiles near the earth's surface,
    ignoring wind resistance.  Tracking is done in two dimensions, height (y)
    and distance (x)."""

    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = height
        theta = math.radians(angle)
        self.xvel = velocity * math.cos(theta)
        self.yvel = velocity * math.sin(theta)

    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self. yvel - time * 9.8
        self.ypos = self.ypos + time * (self.yvel + yvel1)/2.0
        self.yvel = yvel1

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos


def getInputs():
    a = float(input("Enter the launch angle (in degrees): "))
    v = float(input("Enter the initial velocity (in meters/sec): "))
    h = float(input("Enter the initial height (in meters): "))
    t = float(input("Enter the time interval between position calculations (in seconds): "))
    return a, v, h, t


def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    while cball.getY() > 0:
        cball.update(time)
        print("Distance traveled: {0:0.1f} meters.".format(cball.getX()))
        print("Current height {0:0.1f}".format(cball.getY()))
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))

main()

print(Projectile.__doc__)