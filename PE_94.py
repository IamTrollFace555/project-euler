from utils import timer
from math import sqrt

@timer
def almost_equi():

    limit = 1.3 * 10**8 * 3
    k = 1
    perim_sum = 0
    n1 = 0
    n2 = 0

    while 3*n1 - 1 < limit or 3*n2 - 1 < limit:
        n1 = (1 + sqrt((192*k**2 + 4)))/3
        n2 = (-1 + sqrt((3*(4*k+2)**2 + 4)))/3

        if n1 % 1 == 0 and 3*n1 - 1 < limit:
            print("n1: ", n1)
            perim_sum += 3*n1+1

        if n2 % 1 == 0:
            print("n2: ", n2)
            perim_sum += 3*n2-1

        k += 1
    
    return perim_sum


def is_square(n):
    r = int(sqrt(n))
    return n == r * r



@timer
def almost_equilateral():

    limit = 10**9
    perim_sum = 0

    for n in range(3, limit//3, 2):
        
        if is_square((3*n+1)*(n-1)):
            print("n1: ", n)
            perim_sum += 3*n+1

        if is_square((3*n-1)*(n+1)):
            print("n2: ", n)
            perim_sum += 3*n-1
            
    return perim_sum

print(almost_equilateral())