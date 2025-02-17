from utils import SieveOfEratosthenes, timer


@timer
def prime_digit_replacements(n):


    primes = SieveOfEratosthenes(10 ** 6)
    primes_set = set(primes)

    for p in primes:
        
        options = set([*str(p)])
        
        for d in options:
            nums = generate_nums(p, d)

            count = sum([1 for x in nums if x in primes_set])

            if count >= n:
                return p
    return -1

def generate_nums(p:int, d:str) -> list:

    nums = []
    p_list = [*str(p)]  # Unpacking the string

    for digit in range(10):

        temp = [str(x) for x in p_list]

        for idx, elem in enumerate(p_list):

            if elem == d:

                temp[idx] = str(digit)

        temp = int("".join(temp))
        if len(str(temp)) == len(str(p)):
            nums.append(temp)

    return nums


print(prime_digit_replacements(8))
