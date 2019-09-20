import math

def main():
    a,b = int, input("Enter coordinates of your first point. Format: x,y ").split(",")
    c,d = int, input("Enter coordinates of your second point. Format: x,y ").split(",")
    # e holds value of x coordinates
    if a > c:
        e = (a - c)**2
    else:
        e = (c - a)**2
    # f holds value of y coordinates
    if b > d:
        f = (b - d)**2
    else:
        f = (d - b)**2
    # calculate solution
    g = math.sqrt(e + f)
    print(g)

main()
