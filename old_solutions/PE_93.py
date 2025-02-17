from utils import timer
from itertools import permutations

def create_expressions() -> list:
    """
        Generate all possible arithmetic expressions for 4 numbers and 3 operations.
        Here numbers are replaced with A's.
    """

    operators = ["+", "-", "*", "/"]

    expressions = []

    for op1 in operators:
        for op2 in operators:
            for op3 in operators:
                    
                expressions += [f"(A {op1} A)  {op2}  (A {op3} A)"]
                expressions += [f"A {op1}  (A {op2} A)  {op3} A"]

                expressions += [f"A {op1} A {op2}  (A{op3}A)"]
                expressions += [f"(A{op1}A)  {op2} A {op3} A"]

                expressions += [f"(A {op1} A {op2} A)  {op3} A"]
                expressions += [f"A {op1}  (A {op2} A {op3} A)"]

                expressions += [f"A {op1} A {op2} A {op3} A"]

    return expressions


def create_candidates():
    """
        Creates all possible candidates of the form [a, b, c, d] where:
        a < b < c < d and a, b, c, d are digits.
    """

    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    candidates = []

    for d1 in digits:
        rest1 = [x for x in digits if x > d1]

        for d2 in rest1:
            rest2 = [x for x in rest1 if x > d2]

            for d3 in rest2:
                rest2 = [x for x in rest2 if x > d3] 

                for d4 in rest2:
                    candidates.append([d1, d2, d3, d4])
    
    return candidates

def populate_expressions(l:list, expressions:list) -> list:
    """
        Takes a candidate and replaces all A's in every expression
        with the digits of the candidate.
    """

    populated = []

    for exp in expressions:
        new_exp = exp
        for digit in l:
            new_exp = new_exp.replace("A", str(digit), 1)
        
        # print(new_exp)
        populated.append(new_exp)
    
    return populated


def evaluate_candidate(candidate:list):
    """
        Calculates the score for each candidate.
    """
    
    expressions = create_expressions()
    perms = list(permutations(candidate))

    results = []

    for perm in perms:
        populated = populate_expressions(perm, expressions)
        for pop in populated:
            
            try:
                num = eval(pop)
                if num % 1 == 0 and num >= 1:
                    results.append(int(num))
            except:
                pass

    results = list(set(results))
    results.sort()

    score = 1
    while score in results:
        score += 1
    return score - 1 


@timer
def solve():
    """
        Finds the best candidate and returns it.
    """
    candidates = create_candidates()

    max_score = 0
    best_cand = []

    for cand in candidates:
        score = evaluate_candidate(cand)

        if score > max_score:
            max_score = score
            best_cand = cand

    return best_cand

print(solve())