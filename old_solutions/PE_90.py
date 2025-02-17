from utils import timer

# We need to write the numbers:

# 01, 04, 09, 16, 25, 36, 49, 64 and 81

# Hence, we need to have the digits {0, 1, 2, 3, 4, 6, 8} on the left and {1, 4, 5, 6, 9} on the right

# In the end, we need our dice to include the numbers {0, 1, 2, 3, 4, 5, 6, 8, 9}.
# That is, numbers 0 through 9 except 7.

# we want to find all possible arrangements of two dice that meet the following requirements:


    # There must be a 0 and a 1 on opposite dice.

    # There must be a 0 and a 4 on opposite dice.

    # There must be a 0 and a 6 or 9 on opposite dice.

    # There must be a 1 and a 6 or 9 on opposite dice.

    # There must be a 2 and a 5 on opposite dice.

    # There must be a 3 and a 6 or 9 on opposite dice.

    # There must be a 4 and a 6 or 9 on opposite dice. *
    
    # There must be a 6 or 9 and a 4 on opposite dice. *

    # There must be a 8 and a 1 on opposite dice.


    #   (*) Equivalent statements 

# {0, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 6, 7}




def check_dice(dice1:set, dice2:set, conds=8) -> bool:

    pairs = [(0, 1), (0, 4), (0, 6), (1, 6), (2, 5), (3, 6), (4, 6), (8, 1)][:conds]

    for a, b in pairs:

        if not ((a in dice1 and b in dice2) or (b in dice1 and a in dice2)):

            if b == 6:
                b = 9
                if not ((a in dice1 and 9 in dice2) or (9 in dice1 and a in dice2)):
                    return False
            
            else:
                return False
            
    return True


# dice1 = set((0, 5, 6, 7, 8, 9))
# dice2 = set((1, 2, 3, 4, 6, 7))

# dice1 = set([1])
# dice2 = set([0])


# print(check_dice(dice1, dice2, conds=2))

@timer
def solve():

    visited = set()
    dice1 = set([1])
    dice2 = set([0])

    count = 0
    for a1 in range(10):
        for a2 in range(10):

            temp1_dice1 = dice1.copy()
            temp1_dice2 = dice2.copy()

            temp1_dice1.add(a1)
            temp1_dice2.add(a2)

            if check_dice(temp1_dice1, temp1_dice2, conds=2) and len(temp1_dice1) == len(temp1_dice2) and len(temp1_dice1) == 2:
                # ===========================================Break=========================================== #

                for a3 in range(10):
                    for a4 in range(10):

                        temp2_dice1 = temp1_dice1.copy()
                        temp2_dice2 = temp1_dice2.copy()

                        temp2_dice1.add(a3)
                        temp2_dice2.add(a4)

                        if check_dice(temp2_dice1, temp2_dice2, conds=4) and len(temp2_dice1) == len(temp2_dice2) and len(temp2_dice1) == 3:
                            # ===========================================Break=========================================== #

                            for a5 in range(10):
                                for a6 in range(10):

                                    temp3_dice1 = temp2_dice1.copy()
                                    temp3_dice2 = temp2_dice2.copy()

                                    temp3_dice1.add(a5)
                                    temp3_dice2.add(a6)

                                    if check_dice(temp3_dice1, temp3_dice2, conds=5) and len(temp3_dice1) == len(temp3_dice2) and len(temp3_dice1) == 4:
                                        # ===========================================Break=========================================== #

                                        for a7 in range(10):
                                            for a8 in range(10):

                                                temp4_dice1 = temp3_dice1.copy()
                                                temp4_dice2 = temp3_dice2.copy()

                                                temp4_dice1.add(a7)
                                                temp4_dice2.add(a8)

                                                if check_dice(temp4_dice1, temp4_dice2, conds=6) and len(temp4_dice1) == len(temp4_dice2) and len(temp4_dice1) == 5:
                                                    # ===========================================Break=========================================== #

                                                    for a9 in range(10):
                                                        for a10 in range(10):

                                                            temp5_dice1 = temp4_dice1.copy()
                                                            temp5_dice2 = temp4_dice2.copy()

                                                            temp5_dice1.add(a9)
                                                            temp5_dice2.add(a10)


                                                            temp1 = list(temp5_dice1)
                                                            temp2 = list(temp5_dice2)
                                                            temp1.sort()
                                                            temp2.sort()
                                                            temp_a = tuple(temp1+temp2)
                                                            temp_b = tuple(temp2+temp1)

                                                            if check_dice(temp5_dice1, temp5_dice2) and len(temp5_dice1) == len(temp5_dice2) and len(temp5_dice1) == 6 and temp_a not in visited:
                                                                # print(temp5_dice1, temp5_dice2)
                                                                visited.add(temp_a)
                                                                visited.add(temp_b)
                                                                # print(temp_a)
                                                                # print(temp5_dice1, temp5_dice2)
                                                                count += 1
                            

    return count

print(solve())






             
