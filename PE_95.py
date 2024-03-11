from utils import timer
from sympy import divisors

@timer
def solve(limit):
    
    next = lambda x: sum(divisors(x, proper=True))

    max_length = 0
    min_in_max_chain = 0
    max_chain = []

    go_to_chain = set()
    go_to_0_or_past_limit = set()

    for n in range(1, limit + 1):
        # print(n)

        chain = [n]
        cond = True

        while True:
            

            if chain[-1] in go_to_0_or_past_limit or chain[-1] in go_to_chain:
                cond = False
                break

            chain.append(next(chain[-1]))

            if chain[-1] > limit or chain[-1] == 0:
                for elem in chain:
                    go_to_0_or_past_limit.add(elem)
                    cond = False
                break

            if chain[-1] in chain[:-1]:
                idx = chain.index(chain[-1])
                chain = chain[idx:-1]

                for elem in chain:
                    go_to_chain.add(elem)

                break

        if cond:
            if len(chain) > max_length:

                print(chain)
                max_length = len(chain)
                max_chain = chain
                min_in_max_chain = min(chain)


    return min_in_max_chain, max_chain





print(solve(10**6))


