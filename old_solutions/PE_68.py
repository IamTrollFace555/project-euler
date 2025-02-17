from utils import timer


def check(sol:list) -> bool:

    sum1 = sol[0] + sol[5] + sol[6]
    sum2 = sol[1] + sol[6] + sol[7]
    sum3 = sol[2] + sol[7] + sol[8]
    sum4 = sol[3] + sol[8] + sol[9]
    sum5 = sol[4] + sol[9] + sol[5]

    return sum1 == sum2 and sum2 == sum3 and sum3 == sum4 and sum4 == sum5


def find_solutions(sol:list=[]) -> list:

    if len(sol) == 10:
        if check(sol):
            return [sol]
        return []
     

    if sol.count(10) > 1:    # Turn to  1 dimention
        return []

    vals = [x for x in range(1, 11) if x not in sol]
    if len(sol) >= 5:
        vals = [x for x in range(1, 10) if x not in sol]

    sols = []
    for val in vals:
        sols += find_solutions(sol+[val])
    
    return sols


def generate_unique(solutions:list) -> list:

    unique = []
    for sol in solutions:
        s = []
        
        s.append([sol[0], sol[5], sol[6]])
        s.append([sol[1], sol[6], sol[7]])
        s.append([sol[2], sol[7], sol[8]])
        s.append([sol[3], sol[8], sol[9]])
        s.append([sol[4], sol[9], sol[5]])

        unique.append(s)

    return unique

def find_max(uniques:list):

    max_num = 0
    max_uni = []
    for uni in uniques:

        u = [x for x in uni]

        u.sort()
        u = sum(u, [])
        num = int("".join([str(x) for x in u]))

        if num > max_num:
            max_num = num
            max_uni = uni
    
    return max_num, max_uni


print(find_max(generate_unique(find_solutions())))
