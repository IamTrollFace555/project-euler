from utils import timer

# Helper functions:
def triangular(n):

    return int(n*(n+1)/2)

def square(n):
    
    return int(n**2)

def pentagonal(n):

    return int(n*(3*n-1)/2)

def hexagonal(n):
    
    return int(n*(2*n+1))

def heptagonal(n):
    
    return int(n*(5*n-3)/2)

def octagonal(n):

    return int(n*(3*n-2))

def find_start_indexes():

    fig_dict = {3:triangular, 
                4:square,
                5:pentagonal,
                6:hexagonal,
                7:heptagonal,
                8:octagonal}
    
    start_n = []
    for i in range(3, 9):

        n = 1
        num = 0
        while num < 1000:

            num = fig_dict[i](n)        
            n += 1
        
        start_n.append(n - 1)

    return start_n

def find_end_indexes():

    fig_dict = {3:triangular, 
                4:square,
                5:pentagonal,
                6:hexagonal,
                7:heptagonal,
                8:octagonal}
    
    start_n = find_start_indexes()
    for i in range(3, 9):

        n = 1
        num = 0
        while num < 10000:

            num = fig_dict[i](n)        
            n += 1
        
        start_n[i - 3] = n - 2

    return start_n

def create_figs():
    fig_dict = {3:triangular, 
                    4:square,
                    5:pentagonal,
                    6:hexagonal,
                    7:heptagonal,
                    8:octagonal}

    # figs = [[] for x in range(6)]
    # figs = [[] for x in range(6)]
    figs = []
    idx = 0
    for start, finish in zip(find_start_indexes(), find_end_indexes()):

        for n in range(start, finish + 1):
            # figs[idx].append((idx+3, fig_dict[idx+3](n)))
            figs.append((idx+3, fig_dict[idx+3](n)))
        
        idx += 1

    return figs


def check(left:int, right:int):
    return str(left)[2:] == str(right)[:2]


def find_next(l:list=[], figs:list=create_figs()):

    num = l[-1][1]
    for fig, number in figs:
        visited_idxs = [x[0] for x in l]
        if fig not in visited_idxs and check(num, number):
            return (fig, number)
    
    return -1

def solve(l:list=[], figs:list=create_figs(), visited:list=[]):

    visited = [[] for x in range(6)]
    while True:
        
        n = len(l)

        if n == 0:
            temp_figs = [x for x in figs if x not in visited[0] and x[0] == 8]
            l.append(temp_figs[0])
            n += 1
        
        # print("visited:", visited)
        # print("l:", l)
        
        if n < 6:
            temp_figs = [x for x in figs if x not in visited[n]]
        else:
            temp_figs = []

        new_num = find_next(l, temp_figs)
        # print("new_num:", new_num)

        if n == 6:
            if check(l[-1][1], l[0][1]):
                return l
            else:
                visited[5].append(l.pop())
                n -= 1
            
            
        if new_num != -1 and new_num not in visited[n]: 
            l.append(new_num)
            visited[n-1] = []

        else:
            visited[n-1].append(l.pop())
    
@timer
def cyclical_figurate_numbers():

    solution = solve()
    return sum([x[1] for x in solution])

print(cyclical_figurate_numbers())