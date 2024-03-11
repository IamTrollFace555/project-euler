from utils import fast_sieve, timer, is_square

@timer
def solve(n):

    nums = set()
    primes1 = fast_sieve(int(n**.5))

    for p1 in primes1:

        primes2 = [x for x in primes1 if x < n - p1**4]
        if primes2:
            for p2 in primes2:

                primes3 = [x for x in primes2 if x < n - p1**4 - p2**3]
                if primes3:
                    for p3 in primes3:
                        if n - p1**4 - p2**3 - p3**2 > 0:
                            nums.add(p1**4 + p2**3 + p3**2)
            
    return len(nums)

# print(908**3)
print(solve(5*10**7))


