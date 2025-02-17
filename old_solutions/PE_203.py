from utils import timer

def fact(num: int) -> int:
    """
    Returns the factorial of num
    """
    fact = 1
    while num > 0:
        fact = fact * num
        num -= 1
    return fact

def comb(n: int, k: int) -> int:
    """
    Returns the combination
    of n taken k
    """
    return int(fact(n)/(fact(k)*fact(n - k)))

def factors(num: int) -> list:
    """
    Returns the factoring of num
    """
    facs = []
    a = 2
    while num > 1:
        while num % a == 0:
            num /= a
            facs.append(a)
        a += 1
    return facs

def check(n):
    facts = factors(n)
    # if facts != list(set(facts)):
    #     print("=============")
    #     print(n)
    #     print("False")
    #     print(facts)
    return len(facts) == len(set(facts))

@timer
def Square_Free_Binomial_Coefficients(max):
    uniqs = set()
    for n in range(max):
        for k in range(n//2+1):
            temp = comb(n, k)
            if check(temp):
                uniqs.add(temp)
    return sum(uniqs)

# print(factors(20))
# print(Square_Free_Binomial_Coefficients(8))
print(Square_Free_Binomial_Coefficients(51))