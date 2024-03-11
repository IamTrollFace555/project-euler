
from utils import timer, fast_sieve
from math import log


@timer
def find_number(num):

    sieve = fast_sieve(10**5)

    prime = 0
    for p in sieve:
        if (2*log(p) + p*log(2)) < num:
            prime = p
        else:
            return prime



@timer
def solve():
    num = 800 * log(800)
    # print(num)

    # k = find_number(int(num))
    k = 194129
    # print(k)
    sieve = fast_sieve(k)
    print(len(sieve))
   
    count = 0
    for p in sieve:
        for q in sieve:

            if p != q:
                if (p*log(q) + q*log(p)) < num:
                    count += 1
                    # print(p, q)
    
    return count//2



def bin_search(lower, upper, objective):

    found = False
    f = lambda p: p*log(p)

    while not found:
        mid = (lower + upper)/2
        print("upper: ", upper)
        print("mid: ", mid)
        print("lower: ", lower)

        if f(mid) < objective:
            lower = mid

        elif f(mid) > objective:
            upper = mid        

        else:
            found = True
    
    return mid



# print(bin_search(0, 2363771, 2363771))
print(solve())