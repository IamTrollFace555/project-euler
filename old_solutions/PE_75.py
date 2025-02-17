from utils import timer, gcd

@timer
def solve(limit):

    a, b, c  = 0, 0 ,0
    perims = {}
    for r in range(1, int(limit**.5)):

        options = [x for x in range(r%2 + 1, r, 2) if gcd(x, r) == 1]
        for s in options:
            a = r**2 - s**2
            b = 2*r*s
            c = r**2 + s**2
            
            a1, b1, c1 = a, b, c
            while a1 + b1 + c1 <= limit:
                if a1+b1+c1 in perims and a1+b1+c1 <= limit:
                    perims[a1+b1+c1] += 1
                else:
                    perims[a1+b1+c1] = 1

                a1, b1, c1 = a1 + a, b1 + b, c1 + c


    sum = 0
    vals = []
    for key, value in perims.items():
        if value == 1:
            # print(key)
            sum += key
            vals.append(key)

    vals.sort()
    return vals

print(len(solve(1.5 * 10**6)))