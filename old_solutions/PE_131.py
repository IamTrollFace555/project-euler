import sys

sys.path.append("../")
from utils import timer, prime_sieve


@timer
def solve():
    limit = 10 ** 6                         # Searching for numbers until 10**6
    primes = set(prime_sieve(limit))        # Generating primes until 10**6
    count = 0
    for x in range(int(limit ** 0.5) + 1):
        temp = 3 * x ** 2 + 3 * x + 1       # Formula rara de Jaider
        if temp in primes:
            # print("found: ", temp)
            count += 1

    return count


print(solve())
