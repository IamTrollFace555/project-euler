from utils import timer
from decimal import Decimal, getcontext

PRECISION = 200
getcontext().prec = PRECISION


def digit_sum_100(n):
    string = str(n).split(".")
    int_part = int(string[0])
    string = string[1]
    # print(string[:101])
    return sum([int(x) for x in string[:99]]) + int_part


@timer
def solve():
    total = 0
    for i in range(2, 100):
        if i**.5 % 1 != 0:
            total += digit_sum_100(Decimal(i).sqrt())

    return total
    
print(digit_sum_100(Decimal(2).sqrt()))
print(solve())

print((int(i) for i in str(Decimal(2).sqrt()).replace(".", "0")))
#print(*(int(i) for j in range(100) for i in str(round(j**0.5, 100)).replace(".", "0")  if (j**0.5)%1))