from utils import SieveOfEratosthenes, timer

def find_candidates(primes:list):

    # candidates = []
    candidates_set = set()

    candidate_pairs = []
    prime_set = set(primes)

    for p in primes:

        for i in range(1, len(str(p))):
            
            temp1 = str(p)[:i]
            temp2 = str(p)[i:]

            if temp1[0] == "0" or temp2[0] == "0":
                continue

            temp1 = int(temp1)
            temp2 = int(temp2)

            new_prime = int(str(temp2) + str(temp1))

            if temp1 in prime_set and temp2 in prime_set and new_prime in prime_set:
                
                if new_prime not in candidates_set:
                    # candidates.append(p)
                    candidates_set.add(p)
                    candidate_pairs.append((temp1, temp2))

    return list(candidates_set), candidate_pairs


def search_new_prime(candidate_pairs:list, prime_group:list):

    cond = True
    # print(prime_group)

    cands = []

    candidate_pairs_set = set(candidate_pairs)

    for p in prime_group:
        cands += [x for x in candidate_pairs_set if p in x]
    # print(candidate_pairs)

    cands_set = set(cands)

    for cand in cands:
        
        temp = [x for x in cand if x not in prime_group]
        if len(temp) == 0:
            continue
        
        new_prime = temp[0]  # Get the other number in the tuple

        
        cond = True
        for p in prime_group:
            
            # print(p, new_prime)
            if not((p, new_prime) in cands_set or (new_prime, p) in cands_set):
                # print("cond = False")
                cond = False

            # if new_prime == 109:
                    # print((new_prime, p) in cands)
                    # print("!!!!!", (new_prime, p))

        if new_prime not in prime_group and cond:

            # print("cand:", cand)
            # print("new_prime:", new_prime)
            return prime_group + [new_prime]
        
    print(prime_group)
    return []


@timer
def prime_pair_sets(n, mag):

    primes = SieveOfEratosthenes(10**mag)
    # primes.upto(10**mag)
    print("Checkpoint!")

    tested = set()

    _, candidate_pairs = find_candidates(primes)

    print("Checkpoint!")

    prime_group = []

    for pair in candidate_pairs:

        if len(str(pair[0])) + len(str(pair[1])) >= mag:
            continue

        prime_group.append(pair[0])
        prime_group.append(pair[1])

        while len(prime_group) < n and prime_group != []:

            prime_group = search_new_prime(candidate_pairs, prime_group)

        if prime_group != []:
            return prime_group
        
        # print(prime_group)

    return -1
        
        









# cands, primes = find_candidates(SieveOfEratosthenes(10**6))
# print(cands, primes)


# print(select_candidates(cands, primes))
# print(search_new_prime(primes, [7, 109]))

print(sum(prime_pair_sets(5, mag=8)))
# print(SieveOfEratosthenes(10**8))
# print(primes.upto(10**6))
