from utils import timer, flatten
# from functools import reduce


def prod(l:list) -> int:
    p = 1
    for n in l:
        p *= n
    return p

def minus1(l:list) -> list:
        idx = l.index(l[-1])
        l[idx] -= 1
        return l

def minus2(l:list) -> list:
        idx = l.index(l[-1])
        l[idx] -= 2
        l.sort()
        return l

def plus1_minus1(l:list, index) -> list:
        
    new_list = [x for x in l]

    # Check if i'm reducing a 1 or a 2.
    if new_list[index] == 1 or new_list[index] == 2:
        return [0]
    
    # print("First check passed!")

    substract_idx = new_list.index(new_list[index])
    add_idx = substract_idx - 1
    # print("substract_idx: ", substract_idx)
    # print("add_idx: ", add_idx)
    
    # Check if doing +1 -1 alters the ordered condition of the list.
    temp_add = add_idx
    # print("Entering while loop!")
    while new_list[temp_add] + 1 >= new_list[substract_idx]:

        num = new_list[temp_add] - 1
        # print("num: ", num)
        # print("temp_add: ", temp_add)
        # print("list: ", new_list)


        if num < 1:
            return [0]     
        
        try:
            temp_add = new_list.index(num)
        except:
            # print("Did not find an element with that index!")
            if temp_add >= 1:
                temp_add -= 1
                # print("temp_add updated!")
                # print("new temp_add: ", temp_add)
            else:
                return [0]
    
    add_idx = temp_add
        
    if new_list[add_idx] == 1:
        add_idx = -new_list[::-1].index(1) - 1
        
    new_list[substract_idx] -= 1
    new_list[add_idx] += 1

    return new_list



VISITED = set()
# def reduce(l:list):

#     sols = []
#     # if l != [0]:
#     #     print("l: ", l)

#     if 0 in l or tuple(l) in VISITED or sum(l) <= len(l):
#         return []
    
    
    
#     if sum(l) == prod(l):
#         # print("l: ", l)
#         temp = [x for x in l]
#         sols += [temp]
#         # print("SOLUTIONS FOUND: ", len(sols))
    

#     l = [x for x in minus2(l)]



#     for idx in range(1, len(l) - l.count(1) + 1):
#         sols += [x for x in reduce([x for x in plus1_minus1([x for x in l], -idx)])]
#         sols += [x for x in reduce(l)]

#     return sols


def reduce(n:int):

    sols = [[1]*(n-2) + [2, n]]
    best_sol = sols[0]

    while sols and len(sols) < 100:

        sol = sols.pop()
        # print(len(sols))
        # print("sols: ", sols)
        # print(sol)

        if 0 in sol or tuple(sol) in VISITED or sum(sol) <= len(sol):
            continue

        VISITED.add(tuple(sol))

        if sum(sol) == prod(sol) and sum(sol) <= sum(best_sol):
            best_sol = [x for x in sol]
            sols.append(sol)

        sol = [x for x in minus1(sol)]

        for idx in range(1, len(sol) - sol.count(1) + 1):
            temp = [x for x in plus1_minus1([x for x in sol], -idx)]
            if tuple(temp) not in VISITED:
                sols.append(temp)
            
            if tuple(sol) not in VISITED:
                sols.append(sol)

    return best_sol

@timer
def min_product_sum(n):

    # sols1 = reduce([1]*(n-2) + [2, n])
    # sols2 = reduce([1]*(n-2) + [2, n-1])

    # sols = [reduce([1]*(n-2) + [2, n-i])  for i in range(100)]
    sols = reduce(n)
    # print(sols)
    # return min([sum(x) for x in sols if sum(x) == prod(x)])
    return(sols)


for i in range(1, 101):
    VISITED = set()
    print("i:", i,  "min product sum: ", min_product_sum(i))
    print(min_product_sum(i))


# print(min_product_sum(34))


# print(reduce(34))