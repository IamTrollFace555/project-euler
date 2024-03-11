from utils import timer, read_file

hand_dict = {"NA":0,
             "HC":1,
             "OP":2,
             "TP":3,
             "TK":4,
             "ST":5,
             "FL":6,
             "FH":7,
             "FK":8,
             "SF":9,
             "RF":10}

def parse_line(line:str) -> tuple:

    card_dict = {"T":10,
                 "J":11,
                 "Q":12,
                 "K":13,
                 "A":14}
    
    cards = line.split(" ")
    cards = [(int(x[0]), x[1]) if x[0] not in ["T", "J", "Q", "K", "A"] else (card_dict[x[0]], x[1]) for x in cards]

    return cards[:5], cards[5:]


def high_card(hand1, hand2):

    h1 = [x[0] for x in hand1]
    h2 = [x[0] for x in hand2]

    h1.sort()
    h2.sort()
    while True:
        m1 = h1.pop()
        m2 = h2.pop()

        print(m1, m2)

        if m1 > m2:
            return True
        
        if m1 < m2:
            return False
        
def multis(hand):

    nums = [x[0] for x in hand]
    distinct = set(nums)
    distinct_count = []

    for elem in distinct:
        distinct_count.append(nums.count(elem))

    if 4 in distinct_count:
        return "FK", max(nums, key=lambda x: nums.count(x))

    if 3 in distinct_count and 2 in distinct_count:
        return "FH", max(nums, key=lambda x: nums.count(x))
    
    if 3 in distinct_count:
        return "TK", max(nums, key=lambda x: nums.count(x))
    
    if distinct_count.count(2) == 2:
        return "TP", max(nums, key=lambda x: nums.count(x))
    
    if 2 in distinct_count:
        return "OP", max(nums, key=lambda x: nums.count(x))
    
    return "NA", 0


def straight_flush_straightflush(hand):

    nums = [x[0] for x in hand]
    suits = [x[1] for x in hand]

    if len(set(nums)) < 5:
        return "NA", 0
    
    if min(nums) + 4 == max(nums) or set(nums) == set([2, 3, 4, 5, 14]):

        if len(set(suits)) == 1:
            if 14 in nums:
                return "RF", 0
            return "SF", 0
        
        else:
            return "ST", 0
        
    if len(set(suits)) == 1:
        return "FL", 0
    
    return "NA", 0


@timer
def solve():

    hands = read_file("PE_54.txt")
    # hands = ["9S 9C 9H 9D TS 7C 8C 5C QD 6C"]
    count = 0

    for line in hands:
        
        hand1, hand2 = parse_line(line)

        score_1a, num1a = multis(hand1)
        score_1b, num1b = straight_flush_straightflush(hand1)
        num1 = max(num1a, num1b)
        score1 = max(hand_dict[score_1a], hand_dict[score_1b])

        score_2a, num2a = multis(hand2)
        score_2b, num2b = straight_flush_straightflush(hand2)
        num2 = max(num2a, num2b)
        score2 = max(hand_dict[score_2a], hand_dict[score_2b])

        print("=================================================")
        # print(line)
        print("")
        print("hand 1: ", hand1)
        print("score1: ", score1)
        print("scores: ", score_1a, score_1b)
        print("")
        print("hand 2: ", hand2)
        print("score2: ", score2)
        print("scores: ", score_2a, score_2b)

        if score1 == score2:
            if num1 > num2:
                count += 1
                print("player 1 wins!")

            elif num1 == num2:
                if high_card(hand1, hand2):
                    print("player 1 wins!")
                    count += 1
                else:
                    print("player 2 wins!")
            print("player 2 wins!")
        
        elif score1 > score2:
            print("player 1 wins!")
            count += 1

        else:
            print("player 2 wins!")

        print("count: ", count)

    return count
        

print(solve())
