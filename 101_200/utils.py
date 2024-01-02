def digit_sum(number:int) -> int:
    total = 0
    while number != 0:
        total += number % 10
        number = number // 10
    return total


if __name__ == "__main__":

    pass



