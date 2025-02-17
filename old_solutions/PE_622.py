from utils import timer
from sympy import divisors


@timer
def solve(n:int):

    divs = divisors(2**n-1)
    pows = [2**n for n in range(1, n)]

    new_divs = []
    for div in divs:
        cond=True
        for pow in pows:
            if pow%div == 1:
                cond=False
                break
        if cond:
            new_divs.append(div)

    return sum(new_divs) + len(new_divs) - 2 
print(solve(60))



