from utils import timer, divisors_alter, fast_sieve

@timer
def solve(limit):

    primes = fast_sieve(limit)
    primes = set([x for x in primes if x <= limit])
    print("Checkpoint!")

    def check_num(n):
        for d, d_prime in divisors_alter(n):
            if d+d_prime not in primes:
                return False
        return True
    
    total = 0
    for n in primes:
        if check_num(n-1):
            total += n - 1
    
    return total

    

print(solve(10**8))
