import sys

sys.path.append("../")
from utils import timer, digit_sum


@timer
def solve() -> list:
    digit_lim = 10  # Suponiendo que el número no tenga más de 10 dígitos (tampoco es tan importante)
    sum_lim = 9 * digit_lim  # Si todos los dígitos son 9 la suma de los dígitos sería máx 90
    exponent_lim = 25  # Potencias de más de 25 implicarían una solución más loca que esta la verdad (este sí es importante)
    numbers = []

    for n in range(3, sum_lim):
        for exp in range(2, exponent_lim):
            temp = n ** exp
            if digit_sum(temp) == n:
                numbers.append(temp)

    return sorted(numbers)


print(solve()[29])
