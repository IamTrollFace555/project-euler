from utils import timer
from decimal import *
from math import floor

getcontext().prec = 100

def find_x(D):

    # print("============start=================")
    num = Decimal(D).sqrt()
    cf = Decimal(floor(num))
    f = num - cf

    x_0 = 1
    y_0 = 0
    x_1 = cf
    y_1 = 1

    while True:
        # print((x_1, y_1))
        # if D == 61:
        # print(num)
        # print(x_1)
        if x_1**2 - D*y_1**2 == 1:
            return x_1
        
        num = Decimal(1)/f
        cf = Decimal(floor(num))
        f = num - cf
        
        x_1, x_0 = Decimal(x_1) * Decimal(cf) + Decimal(x_0), Decimal(x_1)
        y_1, y_0 = Decimal(y_1) * cf + Decimal(y_0), Decimal(y_1)


@timer
def Diophantine_Equation(max_D):
    Ds = [x for x in range(max_D+1) if x**.5 % 1 != 0]
    # print(Ds)

    max_x = 0
    max_D = 0
    for D in Ds:
        print(D)
        x = find_x(D)
        if x > max_x:
            max_D = D
            max_x = x
    
    return max_D




@timer
def Diophantine_Equation_1(max_D):
    Ds = [x for x in range(max_D+1) if x**.5 % 1 != 0]
    ys = [1]*len(Ds)
    print(len(Ds))
    # alive = [1]*len(Ds)

    while len(Ds) > 10:
        for idx, D in enumerate(Ds):
            x = (D * ys[idx]**2 + 1)**.5
            if x % 1 == 0:
                Ds.pop(idx)
                ys.pop(idx)
                # print(Ds)
                print(len(Ds))
                continue
        
        for i in range(len(ys)):
            ys[i] += 1


    return Ds



print(Diophantine_Equation(1000))
# print(find_x(61))