from utils import timer, gcd, is_square

def pitagorean_triplets(limit):

    a, b, c  = 0, 0 ,0
    triplets = set()
    for r in range(1, 2*int(limit**.5)):
        # print(r)

        options = [x for x in range(r%2 + 1, r, 2) if gcd(x, r) == 1]
        for s in options:
            a = r**2 - s**2
            b = 2*r*s
            c = r**2 + s**2
            
            if (a <= limit and b <= 2*limit) or (b <= limit and a <= 2*limit):
                triplets.add((a, b, c))

                # print((a, b, c))

            a1, b1, c1 = a, b, c
            while (a1 <= limit and b1 <= 2*limit) or (b1 <= limit and a1 <= 2*limit):
                triplets.add((a1, b1, c1))

                a1, b1, c1 = a1 + a, b1 + b, c1 + c

    return triplets


def check(t:tuple) -> bool:

    return is_square(min((t[0] + t[1])**2 + t[2]**2, (t[1] + t[2])**2 + t[0]**2, (t[0] + t[2])**2 + t[1]**2))

@timer
def count_solutions(n:int) -> int:

    triplets = pitagorean_triplets(n)

    boxes = set()
    for trip in triplets:
        for i in range(1, trip[0]):
            box = [i, trip[0]-i, trip[1]]
            box.sort()

            
            if not sum([1 for x in box if x > n]):
                if check(box):
                    boxes.add(tuple(box))

        for i in range(1, trip[1]):
            box = [i, trip[1]-i, trip[0]]
            box.sort()

            if not sum([1 for x in box if x > n]):
                if check(box):
                    boxes.add(tuple(box))


    return len(boxes)


# Probé con varios valores e hice una regresión y llegué a que count_solutions(x) es más o menos x**2 / 3.4 ---> Si y = 10**6, x = sqrt(3.4) * 1000 
# que es más o menos 1843.

# Después fui probando valores a mano hasta que llegué a la respuesta.

values = [1817, 1818]

for i in values:
    print(print("i: ", i, "value: ", count_solutions(i)))



