from utils import timer
from random import sample
from collections import Counter

@timer
def solve(tries):
    avg = 0

    urn = 10*[1] + 10*[2] + 10*[3] + 10*[4] + 10*[5] + 10*[6] + 10*[7]

    for i in range(tries):
        S = set(sample(urn, 20))
        avg += len(S)

    return avg/tries

print(solve(10**8))


