import math


def main():
    x1, y1 = map(float, input("Enter coordinates of your first point. Format: x,y ").split(","))
    x2, y2 = map(float, input("Enter coordinates of your second point. Format: x,y ").split(","))
    x = abs(x1 - x2)**2
    y = abs(y1 - y2)**2
    g = math.sqrt(x + y)
    g = round(g, 2)
    print(g)

main()
