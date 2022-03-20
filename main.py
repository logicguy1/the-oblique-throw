import csv
import time
import math
import sympy as sym

def calc_dist(v, a, h = 10):
    """
    Take in an velocety, angle and a height and calculate the distance it will travel
    """
    g = 9.82 # Gravatational constant

    x = sym.Symbol('x')

    c1 = -1 * h
    c2 = v * math.sin(math.radians(a)) * x - 1/2 * g * x**2
    t = max(sym.solve(sym.Eq(c1, c2), (x,)))

    s = v * math.cos(math.radians(a)) * t

    return s

data = []
velRange = [i/5 for i in range(1,51*5,1)]
angRange = list(range(0,90,1))
timediff = 0

with open("data.csv", 'w') as file:
    writer = csv.writer(file) 
    fields = ['vel', 'ang', 'dist']

    writer.writerow(fields)

    indx = 0
    for vel in velRange:
        t1 = time.time()
        for ang in angRange:
            indx += 1
            line = (vel, ang, calc_dist(vel, ang))
            print(f"{str([int(i) for i in line]):<20} [ {'#' * int((indx / (len(velRange) * len(angRange)) * 100)/4):<25} ] {int(timediff / 60)}:{int(timediff % 60)}")
            data.append(line)

        writer.writerows(data)
        data = []

        t2 = time.time()

        timediff = (t2 - t1) * (len(velRange) - vel)


    print(data)
