from utils import timer, get_continued_frac_sqrt
@timer
def odd_period_square_roots(N):

    count = 0
    for n in range(1, N+1):
        if n**0.5 % 1 != 0:
            if len(get_continued_frac_sqrt(n)[1]) % 2 == 1:
                count += 1

    return count

print(odd_period_square_roots(10**4))