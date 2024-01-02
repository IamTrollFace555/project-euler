import sys

sys.path.append("../")
from utils import digit_sum


def solve() -> list:
    digit_lim = 10
    sum_lim = 9 * digit_lim
    exponent_lim = 25
    numbers = []

    for n in range(3, sum_lim):
        for exp in range(2, exponent_lim):
            temp = n ** exp
            if digit_sum(temp) == n:
                numbers.append(temp)

    return sorted(numbers)


print(solve()[29])
