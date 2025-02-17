from utils import timer
from sympy import divisors

def prod(l:list) -> int:
    p = 1
    for n in l:
        p *= n
    return p

def decompose_number(n):

    
    divs = [x for x in divisors(n, proper=True) if x != 1]

    def decompose(l:tuple=[[0, 0], 1, 1]):

        decompositions = []

        if l[1] > n:
            return []
        
        if l[1] == n:
            return [l]

        if l:
            temp = [x for x in divs if x <= n - l[0][0] and x*l[1] <= n and x >= l[2]]
        else:
            temp = divs

        for d in temp:
            decompositions += decompose([[l[0][0] + d, l[0][1] + 1], l[1]*d, d])

        return decompositions
    
    dec =  decompose()

    return [x[0] for x in dec]


# print(decompose_number(8))

@timer
def solve(limit1, limit2):

    bests = [0, 0] + [2*n for n in range(2, limit1 + 1)]
    for i in range(2, limit2 + 1):

        decs = decompose_number(i)
        for d in decs:

            idx = i - d[0] + d[1]
            if idx <= limit1:
                if i < bests[idx]:
                    bests[idx] = i

    return sum(set(bests))
    
print(solve(12000, 15000))

