import math
def quadratic (a, b, c):
    dr = b*b-4*a*c
    x1 = (-b+math.sqrt(dr))/(2*a)
    x2 = (-b-math.sqrt(dr))/(2*a)
    return x1, x2
