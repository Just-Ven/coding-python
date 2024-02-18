""" Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625 """

import math
pi = math.pi

def calcArea(n, s):
    return (n * s ** 2) / (4 * math.tan(math.pi / n))

print(calcArea(4, 25))