from utils import timer

def rec(a):
    x=0
    b= str(a)
    for i in range(len(b)):
        x=x+int(b[i])**2
    if x==89:
        return 89
    elif x==1:
        return 1
    else:
        return rec(x)

@timer
def solve():

    a=0
    for i in range(1, 10**7):
        if rec(i) == 89:
            a=a+1
            
    print(a)

solve()