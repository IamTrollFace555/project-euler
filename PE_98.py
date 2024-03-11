from utils import timer, read_file, flatten
from PE_98_words import WORDS

# print(len(WORDS))

def preprocess1(words):

    temp_dict = {}
    for word in words:

        key = list(word)
        key.sort()
        key = "".join(key)

        if key in temp_dict:
            temp_dict[key] += 1
        else:
            temp_dict[key] = 1

    
    anagrams = []

    for key in temp_dict:
        if temp_dict[key] > 1:
            anagrams.append(key)


    candidates = []
    
    for anag in anagrams:
        candidate = []
        for word in words:

            key = list(word)
            key.sort()
            key = "".join(key)

            if key == anag:
                candidate.append(word)

        candidates.append(candidate)


    return candidates


def squares(limit):

    return [x**2 for x in range(1, int(limit**.5) + 1)]

def map(word:str, num:int) -> bool:

    def find_next(s:str):
        idx = 0

        while s[idx] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            # print("s: ", s[idx])
            if idx < len(s) - 1:
                idx += 1
            else:
                break
        
        return idx

    str_num = str(num)
    letters = set(list(word))
    # print(letters)

    for letter in letters:

        # print(str_num)
        char = str_num[find_next(str_num)]
        # print("char: ", char)
        str_num = str_num.replace(char, letter)
    
    letters2 = set(list(str_num))

    if letters == letters2:
        return str_num
    
    return None
        

def preprocess2(words):

    candidates = preprocess1(words)
    print("Checkpoint 1!")

    sqs = squares(10**8)
    sqs = [str(x) for x in sqs]
    sqs = preprocess1(sqs)
    sqs = flatten(sqs)
    print("Checkpoint 2!")


    new_candidates = []
    sqr_candidates = []
    for cand_group in candidates:

        new_group = set()
        sqr_group = set()
        for word in cand_group:

            sqr_cands = [x for x in sqs if len(str(x)) == len(word)]
            for sq in sqr_cands:

                if map(word, sq) is not None:
                    new_group.add(word)
                    sqr_group.add(sq)
        
        new_candidates.append(new_group)
        sqr_candidates.append(sqr_group)

    return new_candidates, sqr_candidates


@timer
def analyze_results(words):

    cands, sqs = preprocess2(words)
    for cand, sq in zip(cands, sqs):

        print("===========================")
        print("Word Candidates: ", cand)

        anam_squares = preprocess1(list(sq))
        print("Anagramic Square Candidates ", anam_squares)




analyze_results(WORDS)

# EL resto salió a mano con DEMASIADA PACIENCIA (realmente fueron como 3 0 4 horas desde el inicio del problema, no estuvo tan mal)
# PALABRAS BROAD - BOARD --->  18769 17689