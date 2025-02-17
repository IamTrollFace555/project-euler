from utils import timer

def dot_prod(u:tuple, v:tuple) -> float:
    """Takes two tuples of the same length and calculates the dot product between them"""

    if len(u) != len(v):
        raise ValueError("The length of the tuples must be the same!")
    
    result = 0
    for u_i, v_i in zip(u, v):
         result += u_i * v_i

    return result


@timer
def triangles(n):

    count = 0
    for x1 in range(n+1):
        for y1 in range(n+1):
            for x2 in range(n+1):
                for y2 in range(n+1):
                    
                    if (x1, y1) != (x2, y2) and (x1, y1) != (0, 0) and (x2, y2) != (0, 0): # We must make sure all three points are different.
                        PQ = (x1, y1)
                        PR = (x2, y2)
                        QR = (x1-x2, y1-y2)

                        if dot_prod(PQ, PR) == 0 or dot_prod(PQ, QR) == 0 or dot_prod(QR, PR) == 0:
                            count += 1
        
    return count//2 # We are counting each triangle two times. Hence, we halve the result and return that.
                    

print(triangles(50))