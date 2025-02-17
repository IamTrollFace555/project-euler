from utils import timer
from decimal import Decimal, getcontext

PRECISION = 25
getcontext().prec = PRECISION


def seq(init, iters):

    b1 = init
    concat = "2."

    for i in range(iters):
        b2 = Decimal(int(b1)) * Decimal(b1 - int(b1) + 1)
        an = int(b2)
        concat += str(an)

        b1 = b2

        # print("===================")
        # print("bn: ", b2)
        # print("an: ", an)
        # print("string: ", concat)
    
    return Decimal(concat)

def solve():

    iters = 20
    init = Decimal(2.956938891377988)
    epochs = 10

    for i in range(epochs):
        print(init)
        init = seq(init, iters)

solve()