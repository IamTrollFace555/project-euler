from utils import timer
from decimal import Decimal, getcontext

PRECISION = 20
getcontext().prec = PRECISION

def step(numbers, exp, modulus):

    sums = [196, 289, 485]

    for s in sums:
        
        l = len(numbers)
        num = 2 ** ((exp+s) % modulus) * 100 
        if str(num)[:l] == numbers:
            return exp + s

@timer
def solve(numbers, count):

    sols = 0
    exp = -106
    modulus = Decimal(10).ln()/Decimal(2).ln()
    while sols < count:
        exp = step(numbers, exp, modulus)
        sols+=1
        # print(exp)
    
    return exp
        
        
# print(solve("123", 45))
print(solve("123", 678910))



