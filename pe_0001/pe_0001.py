"""
Implementation of the solutions for the problem 1 of Project Euler

See the README file for the explanation of the solutions

"""

# Solution 1

def solution_1(limit: int) -> int:

    multiples_sum = 0
    for number in range(1, limit):
        if number % 3 == 0 or number % 5 == 0:
            multiples_sum += number

    return multiples_sum

# Solution
def solution_2(limit: int) -> int:

    def sum_first_n(n:int) -> int:
        return n*(n+1)//2
    
    def S(n: int) -> int:
        return n * sum_first_n((limit-1)//n) 

    return S(3) + S(5) - S(15)

if __name__ == "__main__":

    limit = 1000
    print(solution_1(limit))
    print(solution_2(limit))